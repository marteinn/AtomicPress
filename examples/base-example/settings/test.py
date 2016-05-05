import os

from .base import *  # NOQA

# Base
PROJECT_ROOT = Path(__file__).ancestor(2)
DB_PATH = PROJECT_ROOT.child("blog-test.db")
UPLOADS_PATH = PROJECT_ROOT.child("uploads-test")

# dotenv.load_dotenv(PROJECT_ROOT.child(".env"))

SQLALCHEMY_DATABASE_URI = "sqlite:////%s" % DB_PATH
THEME = "atomicpress.themes.minimal"

# Config
DEBUG = True
SECRET_KEY = "SECRET KEY"
FREEZER_BASE_URL = Path("/")
STATIC_URL = FREEZER_BASE_URL.child("static")
UPLOADS_URL = FREEZER_BASE_URL.child("uploads")
GIST_BACKEND_RENDERING = False
SITE_URL = "http://marteinn.se/blog"

# TODO: Move this logic
if not os.path.exists(UPLOADS_PATH):
    os.makedirs(UPLOADS_PATH)
