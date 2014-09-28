# -*- coding: utf-8 -*-

from flask_migrate import Migrate, MigrateCommand
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_script import Manager


app = Flask(__name__)
app.config.update(dict(
    SQLALCHEMY_DATABASE_URI="",
    DEBUG=True,
    SECRET_KEY='',
    USERNAME='admin',
    PASSWORD='default',
    STATIC_URL='/static/',
    UPLOADS_URL='/uploads/',
))

app.config.from_envvar('ATOMICPRESS_SETTINGS', silent=False)

db = SQLAlchemy()
db.init_app(app)

migrate = Migrate(app, db)

manager = Manager(app)


def run():
    from atomicpress import filters
    from atomicpress import commands
    from atomicpress.ext.importer import ImporterCommand

    manager.add_command('db', MigrateCommand)
    manager.add_command('importer', ImporterCommand)

    manager.run()


def activate_theme(theme):
    app.register_blueprint(theme, url_prefix="")