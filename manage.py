#!/usr/bin/env python
# -*- coding: utf-8 -*-
from flask_migrate import MigrateCommand
import os
import os.path as op

from flask.ext.debugtoolbar import DebugToolbarExtension
from flask.ext.script import Manager, prompt_bool
from flask.ext.frozen import Freezer
from wordflask.admin import create_admin
from wordflask.importer import ImporterCommand
from wordflask.app import app, db
from wordflask import models
from wordflask import views


manager = Manager(app)
manager.add_command('db', MigrateCommand)
manager.add_command('importer', ImporterCommand)

app.register_module(views.views, url_prefix="")


@manager.command
def create_db(initial_data=False):
    db.create_all()


@manager.command
def drop_db():
    if prompt_bool("Are you sure?"):
        db.drop_all()

@manager.command
def runserver(admin=False, toolbar=False, debug=False):
    if toolbar:
        bar = DebugToolbarExtension(app)

    if admin:
        create_admin()

    app.run(debug=debug)

@manager.command
def build():
    pass

@manager.command
def deploy():
    pass

if __name__ == "__main__":
    manager.run()