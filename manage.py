#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This module handles command library operations, such as db migrations.
"""

import os


os.environ.setdefault("ATOMICPRESS_SETTINGS", "manage")


PROJECT_ROOT = os.path.dirname(os.path.dirname(__file__))
DB_PATH = os.path.join(PROJECT_ROOT, "blog.db")
UPLOADS_PATH = os.path.join(PROJECT_ROOT, "uploads")

SQLALCHEMY_DATABASE_URI = "sqlite:////{0}".format(DB_PATH)
UPLOADS_PATH = "./"

if __name__ == "__main__":
    from atomicpress import app

    app.setup()
    app.run()
