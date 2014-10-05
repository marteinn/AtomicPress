import os

PROJECT_ROOT = os.path.abspath(os.path.join(__file__, os.pardir))
DB_PATH = PROJECT_ROOT+"/blog.db"
UPLOADS_PATH = PROJECT_ROOT+"/uploads"

SQLALCHEMY_DATABASE_URI = "sqlite:////%s" % DB_PATH
THEME = "atomicpress.themes.minimal"

DEBUG = True
SECRET_KEY = "A secret key"
FREEZER_BASE_URL = "/"
FREEZER_DESTINATION = PROJECT_ROOT+"/blog"

STATIC_URL = FREEZER_BASE_URL+"/static"
UPLOADS_URL = FREEZER_BASE_URL+"/uploads"

# AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
# AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY")
# S3_BUCKET = os.environ.get("S3_BUCKET")
# S3_DESTINATION = os.environ.get("S3_DESTINATION")
