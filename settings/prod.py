import os
from .base import *


DEBUG = False
SECRET_KEY = os.environ.get("SECRET_KEY")
FREEZER_BASE_URL = Path("/blog/")
STATIC_URL = FREEZER_BASE_URL.child("static")
UPLOADS_URL = FREEZER_BASE_URL.child("uploads")
GIST_BACKEND_RENDERING = False

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

