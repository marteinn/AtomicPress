# -*- coding: utf-8 -*-

from flask import current_app
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin import AdminIndexView, expose, Admin
from flask_admin.contrib.sqla import ModelView

from atomicpress import models
from atomicpress.app import db


class HomeView(AdminIndexView):
    @expose("/")
    def index(self):
        return self.render('admin/home.html')


class PostView(ModelView):
    column_default_sort = ('date', True)
    column_searchable_list = ('name', 'title', 'content')
    column_list = ('title', 'status', 'modified', 'date', 'type')


def create_admin():
    app = current_app._get_current_object()
    admin = Admin(app, "AtomicPress", index_view=HomeView(name='Home'))

    admin.add_view(ModelView(models.Blog, db.session, category="Blog"))
    admin.add_view(ModelView(models.Author, db.session, category="Blog"))

    admin.add_view(PostView(models.Post, db.session, category="Post"))
    admin.add_view(ModelView(models.Tag, db.session, category="Post"))
    admin.add_view(ModelView(models.Category, db.session, category="Post"))

    admin.add_view(FileAdmin(app.config["UPLOADS_PATH"],
                             app.config["UPLOADS_URL"],
                             name='Upload files'))
