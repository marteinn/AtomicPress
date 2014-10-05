from atomicpress.app import app
from flask import send_from_directory


@app.route("/uploads/<filename>")
def uploaded_file(filename):
    return send_from_directory(app.config["UPLOADS_PATH"], filename)
