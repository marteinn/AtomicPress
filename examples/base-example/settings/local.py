import os
from .base import *  # NOQA


DEBUG = True
SECRET_KEY = os.environ.get("SECRET_KEY")
FREEZER_BASE_URL = Path("/")
STATIC_URL = FREEZER_BASE_URL.child("static")
UPLOADS_URL = FREEZER_BASE_URL.child("uploads")
GIST_BACKEND_RENDERING = False
SITE_URL = "http://marteinn.se/blog"

FREEZER_DESTINATION = PROJECT_ROOT.child("blog")

GA_TRACKING = os.environ.get("GA_TRACKING")

AWS_ACCESS_KEY_ID = os.environ.get("AWS_ACCESS_KEY_ID")
AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY")
S3_BUCKET = os.environ.get("S3_BUCKET")
S3_DESTINATION = os.environ.get("S3_DESTINATION")
