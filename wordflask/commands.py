from subprocess import call
from flask_debugtoolbar import DebugToolbarExtension
from flask_script import prompt_bool
from wordflask.admin import create_admin
from wordflask.app import manager, db, app

__author__ = 'martinsandstrom'


@manager.command
def create_db(initial_data=False):
    db.create_all()


@manager.command
def drop_db(remove=False, force=False):
    if not force:
        if not prompt_bool("Are you sure?"):
            return

    db.drop_all()

    if remove:
        call(["rm", app.config["DB_PATH"]])


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