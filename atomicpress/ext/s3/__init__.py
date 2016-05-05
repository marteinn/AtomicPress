# -*- coding: utf-8 -*-

"""
atomicpress.ext.s3
----------
Deplys the generated static files to Amazon S3.
"""

import os

from unipath import Path
import boto
from boto.s3.key import Key
from flask_script import Manager

from atomicpress.app import app, manager


S3SyncCommand = Manager(usage='Sync files to s3')

logger = app.logger


@S3SyncCommand.command
def sync():
    params = {
        "aws_access_key_id": app.config["AWS_ACCESS_KEY_ID"],
        "aws_secret_access_key": app.config["AWS_ACCESS_KEY"],
    }

    if app.config.get('AWS_S3_CALLING_FORMAT'):
        params['calling_format'] = app.config['AWS_S3_CALLING_FORMAT']

    if app.config.get("AWS_REGION"):
        c = boto.s3.connect_to_region(app.config["AWS_REGION"], **params)
    else:
        c = boto.connect_s3(**params)

    b = c.get_bucket(app.config["S3_BUCKET"])
    k = Key(b)

    local_path = app.config["FREEZER_DESTINATION"]
    destination_path = app.config["S3_DESTINATION"]

    local_path = Path(local_path)
    destination_path = Path(destination_path)

    for path, file_dir, files in os.walk(local_path):
        for local_file in files:
            file_path = Path(path, local_file)
            rel_path = Path(destination_path,
                            local_path.rel_path_to(file_path))

            logger.info("- Uploading file %s" % (rel_path,))

            k.key = rel_path
            k.set_contents_from_filename(file_path)
            b.set_acl("public-read", k.key)

    logger.info("Sync complete!")


def setup():
    manager.add_command('s3', S3SyncCommand)
