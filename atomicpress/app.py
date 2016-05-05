# -*- coding: utf-8 -*-

import os
import importlib

from flask_migrate import Migrate, MigrateCommand
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_script import Manager


DEFAULT_EXTENSIONS = (
    "atomicpress.ext.importer",
    "atomicpress.ext.exporter",
    "atomicpress.ext.ftp",
    "atomicpress.ext.s3",
    "atomicpress.ext.prefill",
)

DEFAULT_MARKDOWN_EXTENSIONS = [
    "markdown.extensions.tables",
    "markdown.extensions.nl2br",
    "markdown.extensions.fenced_code",
    "markdown.extensions.headerid"
]

app = Flask(__name__)
app.config.update(dict(
    SQLALCHEMY_DATABASE_URI="",
    DEBUG=True,
    SECRET_KEY='',
    STATIC_URL='/static/',
    UPLOADS_URL='/uploads/',
    GIST_BACKEND_RENDERING=True,
    THEME="atomicpress.themes.minimal",
    EXTENSIONS=DEFAULT_EXTENSIONS,
    MARKDOWN_EXTENSIONS=DEFAULT_MARKDOWN_EXTENSIONS
))

settings_module = os.environ.get("ATOMICPRESS_SETTINGS")

if not settings_module:
    app.logger.warning("ATOMICPRESS_SETTINGS is empty, please specify a "
                       "settings file")

app.config.from_object(settings_module)

if "UPLOADS_PATH" not in app.config or \
        not os.path.isdir(app.config["UPLOADS_PATH"]):

    app.logger.error("UPLOADS_PATH is empty or is not a folder")
    exit()

db = SQLAlchemy()
db.init_app(app)

migrate = Migrate(app, db)

manager = Manager(app)


def setup(init_run=False):
    from atomicpress import models  # NOQA
    from atomicpress import views  # NOQA
    from atomicpress import filters  # NOQA
    from atomicpress import commands  # NOQA
    from atomicpress import context_processors  # NOQA

    manager.add_command('db', MigrateCommand)

    activate_extensions()

    # Activate theme
    theme = importlib.import_module(app.config["THEME"])
    activate_theme(theme.theme)

    if init_run:
        run()


def activate_extensions():
    for extension_module in app.config["EXTENSIONS"]:
        extension = importlib.import_module(extension_module)
        extension.setup()


def activate_theme(theme):
    app.register_blueprint(theme, url_prefix="")


def run():
    manager.run()
