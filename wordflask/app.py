# -*- coding: utf-8 -*-
from flask_migrate import Migrate
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

__author__ = 'martinsandstrom'


app = Flask(__name__)
app.config.update(dict(
    SQLALCHEMY_DATABASE_URI="",
    DEBUG=True,
    SECRET_KEY='',
    USERNAME='admin',
    PASSWORD='default'
))

app.config.from_envvar('WORDFLASK_SETTINGS', silent=False)

db = SQLAlchemy()
db.init_app(app)

migrate = Migrate(app, db)
