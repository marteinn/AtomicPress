from unipath import Path

PROJECT_ROOT = Path(__file__).ancestor(2)

DEBUG = False
SECRET_KEY = "asdjhashjdhjasdhjsahjk"
DATABASE_PATH = "website.db"
DB_PATH = PROJECT_ROOT.child("blog.db")
SQLALCHEMY_DATABASE_URI = "sqlite:////%s" % DB_PATH
UPLOADS_PATH = PROJECT_ROOT.child("uploads")

STATIC_URL = '/static/'
UPLOADS_URL = '/uploads/'
