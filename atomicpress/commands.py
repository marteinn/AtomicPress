# -*- coding: utf-8 -*-

from subprocess import call

from flask_debugtoolbar import DebugToolbarExtension
from flask_script import prompt_bool

from atomicpress.admin import create_admin
from atomicpress.app import manager, db, app


logger = app.logger


@manager.command
def create_db():
    db.create_all()
    logger.info("Database was created")


@manager.command
def drop_db(remove=False, force=False):
    if not force:
        if not prompt_bool("Are you sure?"):
            return

    db.drop_all()
    logger.info("Database was dropped")

    if remove:
        call(["rm", app.config["DB_PATH"]])
        logger.info("Database file was removed")


@manager.command
def runserver(admin=False, toolbar=False, debug=False):
    if toolbar:
        bar = DebugToolbarExtension(app)

    if admin:
        create_admin()

    app.run(debug=debug)
