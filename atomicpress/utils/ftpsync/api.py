from .ftpsync import FtpSync


__default = {
    "host": "",
    "username": None,
    "password": None,
}


def set_default(host=None, username=None, password=None,
                **kwargs):

    __default["host"] = host
    __default["username"] = username
    __default["password"] = password


def sync_folder(local_path, destination_path, **kwargs):
    client = _create_client()
    client.sync_dir(local_path, destination_path, **kwargs)


def _create_client():
    client = FtpSync(**__default)
    return client