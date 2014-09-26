# -*- coding: utf-8 -*-

from flask import Module, render_template
from sqlalchemy import desc
from wordflask.models import Blog, Post, PostStatus, PostType


__author__ = 'martinsandstrom'

views = Module(__name__)


"""
2013/11/
2013/11/page/2/
/page/2/

category/action-script/
category/action-script/page/2/

tag/postgresql/
tag/postgresql/page/2/
"""

@views.route('/category/<string:category>')  # TODO: Handle recursive names.
@views.route('/category/<string:category>/page/<int:page>')
@views.route('/tag/<string:tag>')
@views.route('/tag/<string:tag>/page/<int:page>')
@views.route('/<int:year>/<int:month>')
@views.route('/<int:year>/<int:month>/page/<int:page>')
@views.route('/page/<int:page>')
@views.route("/")
def post_list(category=None, page=0, year=0, month=0):
    blog = Blog.query.all()[0]

    posts = Post.query.order_by(desc(Post.date)).\
        filter(Post.status == PostStatus.PUBLISH).\
        filter(Post.type == PostType.POST)

    return render_template("list.html",
                           blog=blog,
                           posts=posts,
                           )


@views.route("/<string:slug>")
def post_single(slug=None):
    blog = Blog.query.all()[0]

    post = Post.query.order_by(desc(Post.date)).\
        filter(Post.status == PostStatus.PUBLISH).\
        filter(Post.type == PostType.POST).\
        filter(Post.name == slug)

    return render_template("list.html",
                           blog=blog,
                           posts=[],
                           )
