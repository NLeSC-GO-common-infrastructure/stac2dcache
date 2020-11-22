import configparser
import pathlib

from .authentication import Authentication
from .io import IO


def configure(username=None, password=None, token_filename=None):
    """
    Configure the custom PySTAC's reader and writer using the server's
    authentication credentials (username/password or bearer-token)

    :param username: (optional, str)
    :param password: (optional, str)
    :param token_filename: (optional, str) Path to config file with the token
    """
    token = _get_token(token_filename)
    authentication = Authentication(username=username,
                                    password=password,
                                    token=token)
    io = IO(authentication_from=authentication,
            authentication_to=authentication)
    io.set_custom_reader_and_writer()
    return authentication


def _get_token(filename=None):
    """
    Read the token from a config file

    :param filename: (optional, str) name of the file
    """
    token = None
    if filename is not None:
        filepath = pathlib.Path(filename)
        assert filepath.exists(), f'Token file {filepath.as_posix()} not found'
        config = configparser.ConfigParser()
        config.read(filepath)
        token = config[filepath.stem]['bearer_token']
    return token
