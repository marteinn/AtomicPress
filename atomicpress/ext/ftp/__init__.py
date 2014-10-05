# -*- coding: utf-8 -*-

"""
atomicpress.ext.ftp
----------
Deplys the generated static files to a ftp account.
"""

from atomicpress.utils import ftpsync
from atomicpress.app import app, manager
from flask_script import Manager


FtpSyncCommand = Manager(usage='Sync files against ftp')

logger = app.logger


@FtpSyncCommand.command
def sync():
    ftpsync.set_default(app.config["FTP_HOST"], app.config["FTP_USERNAME"],
                        app.config["FTP_PASSWORD"])

    ftpsync.sync_folder(app.config["FREEZER_DESTINATION"],
                        app.config["FTP_DESTINATION"])

    logger.info("Sync complete!")


def setup():
    manager.add_command('ftp', FtpSyncCommand)