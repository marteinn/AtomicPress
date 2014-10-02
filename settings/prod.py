import os
from unipath import Path
import dotenv


PROJECT_ROOT = Path(__file__).ancestor(2)
DB_PATH = PROJECT_ROOT.child("blog.db")
UPLOADS_PATH = PROJECT_ROOT.child("uploads")

dotenv.load_dotenv(PROJECT_ROOT.child(".env"))

DEBUG = False
SECRET_KEY = os.environ.get("SECRET_KEY")
SQLALCHEMY_DATABASE_URI = "sqlite:////%s" % DB_PATH
STATIC_URL = "/static/"
UPLOADS_URL = "/uploads/"
GIST_BACKEND_RENDERING = False
THEME = "atomicpress.themes.minimal"

FREEZER_BASE_URL = "/blog/"
FREEZER_DESTINATION = PROJECT_ROOT.child("blog")

GA_TRACKING = os.environ.get("GA_TRACKING")

FTP_HOST = os.environ.get("FTP_HOST")
FTP_USERNAME = os.environ.get("FTP_USERNAME")
FTP_PASSWORD = os.environ.get("FTP_PASSWORD")
FTP_DESTINATION = os.environ.get("FTP_DESTINATION")

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY")
S3_BUCKET = os.environ.get("S3_BUCKET")
S3_DESTINATION = os.environ.get("S3_DESTINATION")

