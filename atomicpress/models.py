# -*- coding: utf-8 -*-

import datetime

from .app import db
from sqlalchemy.orm import relationship


tag_association_table = db.Table(
    'tag_association', db.Model.metadata,
    db.Column('left_id', db.Integer, db.ForeignKey('post.id')),
    db.Column('right_id', db.Integer, db.ForeignKey('tag.id'))
)

category_association_table = db.Table(
    'category_association', db.Model.metadata,
    db.Column('left_id', db.Integer, db.ForeignKey('post.id')),
    db.Column('right_id', db.Integer, db.ForeignKey('category.id'))
)


class Blog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text())
    tagline = db.Column(db.Text())
    language = db.Column(db.String(5), default="en-US")

    def __unicode__(self):
        return self.title


class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(60))
    nicename = db.Column(db.String(50))
    email = db.Column(db.String(100))
    display_name = db.Column(db.String(250))
    bio = db.Column(db.Text())
    avatar = db.Column(db.String(255))

    def __unicode__(self):
        return self.login


class PostType():
    POST = "post"
    PAGE = "page"
    ATTACHMENT = "attachment"
    REVISION = "revision"
    NAVIGATION_MENU = "nav_menu_item"


class PostStatus():
    PUBLISH = "publish"
    DRAFT = "draft"
    FUTURE = "future"
    PENDING = "pending"
    PRIVATE = "private"
    TRASH = "trash"


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    parent_id = db.Column(db.Integer, db.ForeignKey('post.id'))
    parent = relationship("Post", remote_side=[id])

    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    author = relationship("Author")
    status = db.Column(db.String(20), default=PostStatus.DRAFT)
    type = db.Column(db.String(20), default=PostType.POST)
    guid = db.Column(db.String(255))
    name = db.Column(db.String(200))
    title = db.Column(db.Text())
    excerpt = db.Column(db.Text())
    content = db.Column(db.Text())
    modified = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    date = db.Column(db.DateTime, default=datetime.datetime.utcnow)
    template = db.Column(db.String(255))

    order = db.Column(db.Integer, default=0)
    markdown = db.Column(db.Boolean())
    mime_type = db.Column(db.String(100))
    tags = relationship("Tag",
                        secondary=tag_association_table,
                        backref="post")

    categories = relationship("Category",
                              secondary=category_association_table,
                              backref="post")

    def __unicode__(self):
        return self.title


class Tag(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    slug = db.Column(db.String(200))
    hidden = db.Column(db.Boolean(), default=False)

    def __unicode__(self):
        return self.name


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200))
    slug = db.Column(db.String(200))
    hidden = db.Column(db.Boolean(), default=False)
    parent_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    parent = relationship("Category", remote_side=[id])

    def __unicode__(self):
        return self.name
