from datetime import datetime
import os
from flask import Blueprint
from flask_script import Manager
import wpparser
from wordflask.app import db, app
from wordflask.models import Blog, Author, Category, Tag, Post
from wordflask.utils.files import generate_image_from_url

__author__ = 'martinsandstrom'


importer = Blueprint("importer", __name__)
ImporterCommand = Manager(usage='Perform wordpress import')

@ImporterCommand.option('-f', '--file', dest='path', default=None,
                      help="Import wordpress file")
def import_blog(path=None):
    print "Parsing file..."
    parsed_data = wpparser.parse(path)

    print "Inserting data..."
    insert(parsed_data)


def insert(data):
    # Blog
    print "Adding blog..."

    blog_data = data["blog"]

    blog = Blog(
        title=blog_data["title"],
        tagline=blog_data["tagline"],
        language=blog_data["language"],
    )

    db.session.add(blog)

    # Authors
    print "Adding authors..."

    author_reference = {}
    for user_data in data["authors"]:
        author = Author(
            login=user_data["login"],
            nicename=user_data["display_name"],
            email=user_data["email"],
            display_name="%s %s" % (user_data["first_name"],
                                    user_data["last_name"])
        )
        author_reference[user_data["login"]] = author

        db.session.add(author)

    db.session.commit()

    # Categories
    print "Adding categories..."

    category_reference = _insert_categories(data["categories"])
    db.session.commit()

    # Tags
    print "Adding tags..."

    tag_reference = {}
    for tag_data in data["tags"]:
        tag = Tag(
            name=tag_data["name"],
            slug=tag_data["slug"],
        )
        db.session.add(tag)

        tag_reference[tag_data["slug"]] = tag

    db.session.commit()

    # Posts
    print "Inserting %s posts..." % len(data["posts"])

    created_posts = []
    post_id_reference = {}

    for post_data in data["posts"]:
        print "Adding %s..." % post_data["title"]

        author = author_reference[post_data["creator"]]

        if post_data["post_date"] == "0000-00-00 00:00:00":
            post_data["post_date"] = "1970-01-01 00:00:00"

        date = datetime.strptime(post_data["post_date"],
                                 '%Y-%m-%d %H:%M:%S')

        post = Post(
            title=post_data["title"],
            author=author,
            date=date,
            modified=date,
            name=post_data["post_name"],
            content=post_data["content"],
            excerpt=post_data["excerpt"],
            status=post_data["status"],
            order=post_data["menu_order"],
            type=post_data["post_type"],
        )

        # Save attachment
        if post_data["post_type"] == "attachment":
            guid = post_data["guid"]
            relative_path = guid.split("wp-content/uploads/")[1]
            file_name, image = generate_image_from_url(guid)
            file_path = app.config['UPLOADS_PATH'].child(relative_path)
            if not os.path.exists(os.path.dirname(file_path)):
                os.makedirs(os.path.dirname(file_path))

            image.save(file_path)
            post.guid = relative_path

        for name in post_data["categories"]:
            category = category_reference[name]
            post.categories.append(category)

        for name in post_data["tags"]:
            tag = tag_reference[name]
            post.tags.append(tag)

        created_posts.append(post)
        db.session.add(post)

        post_id_reference[post_data["post_id"]] = post

    db.session.commit()

    # Add parents
    for post_data in data["posts"]:
        created_post = post_id_reference[post_data["post_id"]]
        has_parent = int(post_data["post_parent"])

        if has_parent:
            parent_post = post_id_reference[post_data["post_parent"]]
            created_post.parent = parent_post

    db.session.commit()


def _insert_categories(categories, parent=None, reference=None):
    if not reference:
        reference = {}

    for category_data in categories:
        category = Category(
            name=category_data["name"],
            slug=category_data["nicename"],
        )

        if parent:
            category.parent = parent

        db.session.add(category)
        db.session.commit()

        reference[category_data["nicename"]] = category

        _insert_categories(category_data["children"], parent=category,
                           reference=reference)
    return reference


