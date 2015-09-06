import dotenv
from unipath import Path


PROJECT_ROOT = Path(__file__).ancestor(2)
DB_PATH = PROJECT_ROOT.child("blog.db")
UPLOADS_PATH = PROJECT_ROOT.child("uploads")

dotenv.load_dotenv(PROJECT_ROOT.child(".env"))

SQLALCHEMY_DATABASE_URI = "sqlite:////%s" % DB_PATH
THEME = "atomicpress.themes.minimal"

