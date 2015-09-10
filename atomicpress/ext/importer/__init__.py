# -*- coding: utf-8 -*-

"""
atomicpress.ext.importer
----------
This module handles wordpress imports by exposing the import command.
"""

import re
import os
from datetime import datetime
from flask_script import Manager
from unipath import Path
import wpparser
from atomicpress.app import db, app, manager
from atomicpress.models import Blog, Author, Category, Tag, Post
from atomicpress.utils.files import generate_image_from_url


logger = app.logger

ImporterCommand = Manager(usage='Perform wordpress import')


@ImporterCommand.option('-f', '--file', dest='path', default=None,
                        help="Import wordpress file")
def import_blog(path=None):
    logger.info("Parsing file...")
    parsed_data = wpparser.parse(path)

    logger.info("Inserting data...")
    insert(parsed_data)


def insert(data):
    # Blog
    logger.info("Adding blog...")

    blog_data = data["blog"]

    blog = Blog(
        title=blog_data["title"],
        tagline=blog_data["tagline"],
        language=blog_data["language"],
    )

    db.session.add(blog)

    # Authors
    logger.info("Adding authors...")

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
    logger.info("Adding categories...")

    category_reference = _insert_categories(data["categories"])
    db.session.commit()

    # Tags
    logger.info("Adding tags...")

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
    logger.info("Inserting %s posts..." % len(data["posts"]))

    created_posts = []
    post_id_reference = {}

    data["posts"] = data["posts"][::-1]

    for post_data in data["posts"]:
        logger.info("Adding %s..." % post_data["title"])

        author = author_reference[post_data["creator"]]

        if post_data["post_date"] == "0000-00-00 00:00:00":
            post_data["post_date"] = "1970-01-01 00:00:00"

        date = datetime.strptime(post_data["post_date"],
                                 '%Y-%m-%d %H:%M:%S')

        post_content = None
        if post_data["content"]:
            post_content = _clean_post_content(blog_data["blog_url"],
                                               post_data["content"])

        post = Post(
            title=post_data["title"],
            author=author,
            date=date,
            modified=date,
            name=post_data["post_name"],
            content=post_content,
            excerpt=post_data["excerpt"],
            status=post_data["status"],
            order=post_data["menu_order"],
            type=post_data["post_type"],
        )

        # Save attachment
        if post_data["post_type"] == "attachment":
            file_url = post_data["guid"]
            site_url, relative_path = file_url.split("wp-content/uploads/")
            relative_path = Path(relative_path)

            _save_image(file_url)

            # Save thumbnails
            metadata = {}
            if "postmeta" in post_data:
                if "attachment_metadata" in post_data["postmeta"]:
                    metadata = post_data["postmeta"]["attachment_metadata"]

            if "sizes" in metadata:
                for size in metadata["sizes"]:
                    file_name = metadata["sizes"][size]["file"]
                    size_rel_path = relative_path.ancestor(1).child(file_name)
                    size_file_url = "/".join([site_url, "wp-content/uploads",
                                              size_rel_path])

                    _save_image(size_file_url)

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

    logger.info("Import complete!")


def _clean_post_content(blog_url, content):
    """
    Replace import path with something relative to blog.
    """

    content = re.sub(
        "<img.src=\"%s(.*)\"" % blog_url,
        lambda s: "<img src=\"%s\"" % _get_relative_upload(s.groups(1)[0]),
        content)

    return content


def _get_relative_upload(url):
    """
    Return relative upload path from url.
    """
    return app.config["UPLOADS_URL"]+url.split("wp-content/uploads/")[1]


def _save_image(url):
    site_url, relative_path = url.split("wp-content/uploads/")
    file_name, image = generate_image_from_url(url)
    file_path = app.config['UPLOADS_PATH'].child(relative_path)
    if not os.path.exists(os.path.dirname(file_path)):
        os.makedirs(os.path.dirname(file_path))

    image.save(file_path)


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


def setup():
    manager.add_command('importer', ImporterCommand)
