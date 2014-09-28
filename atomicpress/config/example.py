from unipath import Path

PROJECT_ROOT = Path(__file__).ancestor(3)
DB_PATH = PROJECT_ROOT.child("blog.db")
UPLOADS_PATH = PROJECT_ROOT.child("uploads")

DEBUG = False
SECRET_KEY = "secret key"
SQLALCHEMY_DATABASE_URI = "sqlite:////%s" % DB_PATH
STATIC_URL = "/static/"
UPLOADS_URL = "/blog/uploads/"

FREEZER_DESTINATION = PROJECT_ROOT.child("build")
