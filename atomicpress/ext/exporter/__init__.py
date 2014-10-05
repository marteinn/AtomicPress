# -*- coding: utf-8 -*-

"""
atomicpress.ext.exporter
----------
This module takes the blog data and makes deployable static files from it.
"""

import os
from flask_frozen import Freezer
from flask_script import Manager
from atomicpress.app import app, manager


ExporterCommand = Manager(usage='Export blog as static files')

logger = app.logger


@ExporterCommand.command
def export():
    freezer = Freezer(app)
    logger.info("Starting export...")

    @freezer.register_generator
    def uploaded_file():
        file_list = os.listdir(app.config["UPLOADS_PATH"])
        for uploads_file in file_list:
            if uploads_file.find(".") > 0:
                yield {'filename': uploads_file}

    freezer.freeze()
    logger.info("Blog was successfully exported!")


def setup():
    manager.add_command('exporter', ExporterCommand)
