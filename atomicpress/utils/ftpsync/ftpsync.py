# -*- coding: utf-8 -*-

import ftplib
import logging
import os
from unipath import Path

logger = logging.getLogger(__name__)


class FtpSync():
    conn = None
    host = None
    username = None
    password = None

    def __init__(self, host=None, username=None, password=None):
        self.host = host
        self.username = username
        self.password = password

    def _login(self):
        self.conn = ftplib.FTP(self.host)
        self.conn.login(self.username, self.password)

    def _close(self):
        self.conn.close()

    def remove_dir(self, destination_path):
        """
        Remove folder. Based on https://gist.github.com/artlogic/2632647.
        """

        wd = self.conn.pwd()

        try:
            names = self.conn.nlst(destination_path)
        except ftplib.all_errors as e:
            # some FTP servers complain when you try and list non-existent paths
            logger.debug('FtpRmTree: Could not remove {0}: {1}'.format(
                destination_path, e))
            return

        for name in names:
            if os.path.split(name)[1] in ('.', '..'):
                continue

            try:
                self.conn.cwd(name)  # if we can cwd to it, it's a folder
                self.conn.cwd(wd)  # don't try a nuke a folder we're in
                self.remove_dir(name)
            except ftplib.all_errors:
                self.conn.delete(name)

        try:
            self.conn.rmd(destination_path)
        except ftplib.all_errors as e:
            logger.debug('remove_dir: Could not remove {0}: {1}'.format(
                destination_path, e))

    def sync_dir(self, local_path, destination_path, override=True):
        self._login()

        local_dir = Path(local_path)
        target_dir = Path(destination_path)

        if override:
            if self._file_exist(target_dir):
                self.remove_dir(target_dir)

        self._upload_dir(local_dir, target_dir)
        self._close()

    def _file_exist(self, destination_path):
        destination_name = destination_path.name
        parent_dir = destination_path.ancestor(1)

        return destination_path in self.conn.nlst(parent_dir)

    def _upload_dir(self, local_path, destination_path):
        logger.info("- Uploading dir %s" % (local_path.name,))

        local_files = os.listdir(local_path)

        if not self._file_exist(destination_path):
            self.conn.mkd(destination_path)

        self.conn.cwd(destination_path)

        # Upload files
        for file_name in local_files:
            file_path = local_path.child(file_name)

            if not os.path.isdir(file_path):
                self._upload_file(file_path, destination_path.child(file_name))

        # Upload dirs
        for dir_name in local_files:
            dir_path = local_path.child(dir_name)

            if os.path.isdir(dir_path):
                self._upload_dir(dir_path, destination_path.child(dir_name))

    def _upload_file(self, local_path, destination_path):
        logger.info("- Uploading file %s" % (local_path.name,))

        try:
            if local_path.ext in (".txt", ".htm", ".html"):
                self.conn.storlines("STOR " + local_path.name,
                                    open(local_path))
            else:
                self.conn.storbinary("STOR " + local_path.name,
                                     open(local_path, "rb"), 1024)

        except Exception as e:
            logger.warn("%s - %s" % (e, str(e)))
