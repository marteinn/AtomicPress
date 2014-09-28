import os
from flask import Blueprint
from flask_frozen import Freezer
from flask_script import Manager


exporter = Blueprint("exporter", __name__)
ExporterCommand = Manager(usage='Export blog as static files')


@ExporterCommand.option('-f', '--file', dest='path', default=None,
                      help="Export blog as html")
def export(path=None):
    from atomicpress.app import app

    freezer = Freezer(app)

    @freezer.register_generator
    def uploaded_file():
        file_list = os.listdir(app.config["UPLOADS_PATH"])
        for uploads_file in file_list:
            if uploads_file.find(".") > 0:
                yield {'filename': uploads_file}

    freezer.run()
