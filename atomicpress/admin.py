# -*- coding: utf-8 -*-

from flask import current_app
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin import AdminIndexView, expose, Admin
from flask_admin.contrib.sqla import ModelView
from wtforms.validators import Required

from atomicpress import models
from atomicpress.app import db


class HomeView(AdminIndexView):
    @expose("/")
    def index(self):
        return self.render('admin/home.html')


class PostView(ModelView):
    column_default_sort = ('date', True)
    column_searchable_list = ('name', 'title', 'content')
    column_filters = ('type', 'status')
    column_list = ('title', 'status', 'modified', 'date', 'type')
    can_export = True

    form_choices = {
        'status': [
            (models.PostStatus.PUBLISH, 'Publish'),
            (models.PostStatus.DRAFT, 'Draft'),
            (models.PostStatus.FUTURE, 'Future'),
            (models.PostStatus.PENDING, 'Pending'),
            (models.PostStatus.PENDING, 'Private'),
            (models.PostStatus.TRASH, 'Trash'),
        ],
        'type': [
            (models.PostType.POST, "Post"),
            (models.PostType.PAGE, "Page"),
            (models.PostType.ATTACHMENT, "Attachment"),
            (models.PostType.REVISION, "Revision"),
            (models.PostType.NAVIGATION_MENU, "Nav Menu Item"),
        ]
    }

    form_widget_args = {
        'title': {
            'class': 'input-xxlarge'
        },
        'excerpt': {
            'class': 'input-xxlarge'
        },
        'content': {
            'rows': 10,
            'class': 'input-xxlarge'
        }
    }

    form_args = {
        'guid': {
            'validators': [Required()]
        },
        'title': {
            'validators': [Required()]
        },
        'name': {
            'validators': [Required()]
        }
    }


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
