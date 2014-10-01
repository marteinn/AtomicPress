# -*- coding: utf-8 -*-

"""
atomicpress.ext.s3
----------
Upload blog to a s3 bucket

"""
import os
import logging
from unipath import Path
import boto
from boto.s3.key import Key

from atomicpress.app import app

from flask_script import Manager


logger = logging.getLogger(__name__)

S3SyncCommand = Manager(usage='Sync files to s3')

@S3SyncCommand.command
def sync():
    c = boto.connect_s3(aws_access_key_id=app.config["AWS_ACCESS_KEY_ID"],
                        aws_secret_access_key=app.config["AWS_ACCESS_KEY"])
    b = c.get_bucket(app.config["S3_BUCKET"])
    k = Key(b)

    local_path = app.config["FREEZER_DESTINATION"]
    destination_path = app.config["S3_DESTINATION"]

    for path, file_dir, files in os.walk(local_path):
        for local_file in files:
            file_path = Path(path, local_file)
            rel_path = Path(destination_path,
                            local_path.rel_path_to(file_path))

            logger.info("- Uploading file %s" % (rel_path,))

            k.key = rel_path
            k.set_contents_from_filename(file_path)
            b.set_acl("public-read", k.key)

