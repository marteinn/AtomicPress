# -*- coding: utf-8 -*-

import calendar
import math
import datetime

from flask import render_template
from sqlalchemy import desc, asc, func

from atomicpress.themes.minimal import theme, PAGE_SIZE
from atomicpress.themes.minimal import helpers
from atomicpress.models import Blog, Post, PostType, Category, Tag
from atomicpress.utils import date as dateutils


@theme.route('/category/<string:category>/')  # TODO: Handle recursive names.
@theme.route('/category/<string:category>/page/<int:page>/')
@theme.route('/tag/<string:tag>/')
@theme.route('/tag/<string:tag>/page/<int:page>/')
@theme.route('/<int:year>/<int:month>/')
@theme.route('/<int:year>/<int:month>/page/<int:page>/')
@theme.route('/page/<int:page>/')
@theme.route("/")
def post_list(category=None, page=0, year=0, month=0, tag=None):
    blog = Blog.query.all()[0]

    posts = Post.query.order_by(desc(Post.date)).\
        filter(helpers.gen_post_status()).\
        filter(Post.type == PostType.POST)

    if category:
        category_obj = Category.query.filter(Category.slug == category)
        category_obj = category_obj.slice(0, 1)
        if category_obj.count() == 0:
            raise Exception("Category %s does not exist" % (category,))

        category_obj = category_obj[0]
        posts = posts.filter(Post.categories.contains(category_obj))

    if tag:
        tag_obj = Tag.query.filter(Tag.slug == tag)
        tag_obj = tag_obj.slice(0, 1)
        if tag_obj.count() == 0:
            raise Exception("Tag %s does not exist" % (tag,))

        tag_obj = tag_obj[0]
        posts = posts.filter(Post.tags.contains(tag_obj))

    if year and month:
        posts = posts.filter(func.strftime('%Y-%m', Post.date) ==
                             "%s-%02d" % (year, month))

    num_posts = posts.count()
    num_pages = math.ceil(num_posts/PAGE_SIZE)
    posts = posts.slice(page*PAGE_SIZE, (page+1)*PAGE_SIZE)

    return render_template("list.html",
                           blog=blog,
                           posts=posts,
                           page=page,
                           num_pages=num_pages,
                           menu_pages=_get_menu_pages()
                           )


@theme.route("/<string:slug>/")
def post_single(slug=None):
    blog = Blog.query.all()[0]

    posts = Post.query.order_by(desc(Post.date)).\
        filter(helpers.gen_post_status()).\
        filter((Post.type == PostType.POST) | (Post.type == PostType.PAGE)).\
        filter(Post.name == slug).\
        slice(0, 1)

    if not posts.count():
        return render_template("404.html")

    post = posts.all()[0]

    return render_template("single.html",
                           blog=blog,
                           post=post,
                           menu_pages=_get_menu_pages()
                           )


@theme.route("/archive/")
def menu():
    blog = Blog.query.all()[0]

    posts = Post.query.order_by(asc(Post.date)).\
        filter(helpers.gen_post_status()).\
        filter(Post.type == PostType.POST).\
        slice(0, 1)

    now = datetime.datetime.now()
    oldest_post = posts[0]

    month_list = dateutils.get_month_list(now, oldest_post.date)
    archive_data = []
    for month in month_list:
        year, real_month = month

        num_posts = Post.query.order_by(asc(Post.date)).\
            filter(helpers.gen_post_status()).\
            filter(Post.type == PostType.POST).\
            filter(func.strftime('%Y-%m', Post.date) ==
                   "%s-%02d" % (year, real_month)).\
            count()

        if not num_posts:
            continue

        month_name = calendar.month_name[real_month]
        archive_data.append({
            "name": "%s %s" % (month_name, year),
            "posts": num_posts,
            "year": year,
            "month": real_month,
        })

    archive_data = archive_data[::-1]

    pages = Post.query.order_by(desc(Post.date)).\
        filter(helpers.gen_post_status()).\
        filter(Post.type == PostType.PAGE).\
        all()

    categories = Category.query.filter(Category.hidden == False).all()  # NOQA
    tags = Tag.query.filter(Tag.hidden == False).all()  # NOQA

    return render_template("menu.html",
                           blog=blog,
                           pages=pages,
                           categories=categories,
                           archive=archive_data,
                           tags=tags,
                           menu_pages=_get_menu_pages()
                           )


def _get_menu_pages():
    slugs = ("about", )
    posts = Post.query.filter(Post.name.in_(slugs)).all()
    return posts
