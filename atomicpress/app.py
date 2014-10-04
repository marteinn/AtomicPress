# -*- coding: utf-8 -*-

import os
import importlib
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
    GIST_BACKEND_RENDERING=True,
    THEME="atomicpress.themes.minimal"
))

settings_module = os.environ.get("ATOMICPRESS_SETTINGS")
app.config.from_object(settings_module)

db = SQLAlchemy()
db.init_app(app)

migrate = Migrate(app, db)

manager = Manager(app)


def setup(init_run=False):
    from atomicpress import models
    from atomicpress import views
    from atomicpress import filters
    from atomicpress import commands
    from atomicpress import context_processors
    from atomicpress.ext.importer import ImporterCommand
    from atomicpress.ext.exporter import ExporterCommand
    from atomicpress.ext.ftp import FtpSyncCommand
    from atomicpress.ext.s3 import S3SyncCommand
    from atomicpress.ext.prefill import PreFillCommand

    manager.add_command('db', MigrateCommand)
    manager.add_command('importer', ImporterCommand)
    manager.add_command('exporter', ExporterCommand)
    manager.add_command('ftp', FtpSyncCommand)
    manager.add_command('s3', S3SyncCommand)
    manager.add_command('prefill', PreFillCommand)

    # configure_logging(settings.LOGGING_CONFIG, settings.LOGGING)

    # Activate theme
    theme = importlib.import_module(app.config["THEME"])
    activate_theme(theme.theme)

    if init_run:
        run()


def run():
    manager.run()


def activate_theme(theme):
    app.register_blueprint(theme, url_prefix="")
