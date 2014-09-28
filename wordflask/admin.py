import os.path as op
from flask import current_app
from flask_admin.contrib.fileadmin import FileAdmin
from flask_admin import AdminIndexView, expose, Admin
from flask_admin.contrib.sqla import ModelView
from wordflask import models
from wordflask.app import db


class HomeView(AdminIndexView):
    @expose("/")
    def index(self):
        return self.render('admin/home.html')


def create_admin():
    app = current_app._get_current_object()
    admin = Admin(app, "WordFlask", index_view=HomeView(name='Home'))

    admin.add_view(ModelView(models.Blog, db.session, category="Blog"))
    admin.add_view(ModelView(models.Author, db.session, category="Blog"))
    admin.add_view(ModelView(models.Post, db.session, category="Post"))
    admin.add_view(ModelView(models.Tag, db.session, category="Post"))
    admin.add_view(ModelView(models.Category, db.session, category="Post"))

    # TODO: Rewrite with unipath
    path = op.join(op.dirname(__file__), '../wordflask/uploads')
    admin.add_view(FileAdmin(path, '/uploads/', name='Upload files'))
