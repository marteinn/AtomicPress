import os
from unipath import Path

PROJECT_ROOT = Path(__file__).ancestor(2)

DEBUG = False
SECRET_KEY = "asdjhashjdhjasdhjsahjk"
DATABASE_PATH = "website.db"
SQLALCHEMY_DATABASE_URI = "sqlite:////%s" % (PROJECT_ROOT.child("blog.db"),)
UPLOADS_PATH = PROJECT_ROOT.child("uploads")