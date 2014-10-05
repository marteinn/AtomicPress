# -*- coding: utf-8 -*-

"""
atomicpress.ext.prefill
----------
This extensions makes it possible to generate dummy data, as a simple way to
try out the system and see how ut behaves.
"""

from atomicpress.app import db, app, manager
from atomicpress.models import (
    Blog, Author, Category, Tag, Post, PostStatus, PostType)
from flask_script import Manager


PreFillCommand = Manager(usage='Insert initial dummy data')

logger = app.logger


@PreFillCommand.command
def fill():
    # Blog
    blog = Blog(title="My Blog", tagline="Hi! And welcome to my blog")

    db.session.add(blog)
    db.session.commit()

    # Author
    author = Author(
        login="admin",
        nicename="johndoe",
        email="john@doe.com",
        display_name="John Doe"
    )

    db.session.add(author)
    db.session.commit()

    # Category
    main_category = Category(
        name="News",
        slug="news",
        hidden=False,
    )

    db.session.add(main_category)
    db.session.commit()

    category = Category(
        name="Economy",
        slug="economy",
        hidden=False,
        parent=main_category
    )

    db.session.add(category)
    db.session.commit()

    # Tags
    tag = Tag(
        name="2014",
        slug="2014",
        hidden=False
    )

    db.session.add(tag)
    db.session.commit()

    # Post
    post = Post(
        title="Hello world!",
        author=author,
        name="hello-world",
        content="This is an example text",
        status=PostStatus.PUBLISH,
        type=PostType.POST
    )

    post.categories.append(category)
    post.tags.append(tag)

    db.session.add(post)
    db.session.commit()

    # Page
    page = Post(
        title="About",
        author=author,
        name="about",
        content="This is a little page about something.",
        status=PostStatus.PUBLISH,
        type=PostType.PAGE
    )

    db.session.add(page)
    db.session.commit()

    logger.info("Prefill complete!")


def setup():
    manager.add_command('prefill', PreFillCommand)
