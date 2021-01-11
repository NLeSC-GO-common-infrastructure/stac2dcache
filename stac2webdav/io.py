import pathlib
import urlpath
import requests

from tqdm import tqdm
from pystac import STAC_IO

from .authentication import Authentication


class IO:
    """ Object to perform IO tasks with a local or remote file system """

    def __init__(self, authentication_from=None, authentication_to=None):
        """

        :param authentication_from: (:class:`~.authentication.Authentication`)
            authentication for input source
        :param authentication_to: (:class:`~.authentication.Authentication`)
            authentication for output destination
        """
        self.authentication_from = authentication_from or Authentication()
        self.authentication_to = authentication_to or Authentication()

    def set_custom_reader_and_writer(self):
        """
        Configure PySTAC to use the custom read/write methods
        """
        STAC_IO.read_text_method = self.read
        STAC_IO.write_text_method = self.write

    @staticmethod
    def set_default_reader_and_writer():
        """
        Revert to default PySTAC reader and writer
        """
        STAC_IO.read_text_method = STAC_IO.default_read_text_method
        STAC_IO.write_text_method = STAC_IO.default_write_text_method

    def read(self, uri):
        """
        Read from local or remote file system

        :param uri: (string) URI where to read from
        """
        url = urlpath.URL(uri)
        if url.scheme.startswith('http'):
            r = url.get(auth=self.authentication_from.get_auth(),
                        headers=self.authentication_from.get_headers())
            r.raise_for_status()
            text = r.text
        else:
            text = STAC_IO.default_read_text_method(uri)
        return text

    def write(self, uri, text):
        """
        Write to local or remote file system

        :param uri: (string) URI where to write to
        :param text: (string) text to be written
        """
        url = urlpath.URL(uri)
        if url.scheme.startswith('http'):
            r = url.put(data=text,
                        auth=self.authentication_to.get_auth(),
                        headers=self.authentication_to.get_headers())
            r.raise_for_status()
        else:
            STAC_IO.default_write_text_method(uri, text)

    def download(self, from_uri, to_uri):
        """
        Download a file and write it to a local or remote file system

        :param from_uri: (str) URI of the file to download
        :param to_uri: (str) URI of the folder where to save the file
        """
        from_uri = urlpath.URL(from_uri)
        to_uri = urlpath.URL(to_uri) / from_uri.name

        # Build session and get data trunks
        session = requests.session()
        if self.authentication_from.get_auth() is not None:
            auth = requests.auth.HTTPBasicAuth(
                self.authentication_from.get_auth()[0],
                self.authentication_from.get_auth()[1])
            session.auth = auth
        s = session.get(from_uri.as_uri(), stream=True)
        filesize = int(s.headers['Content-length'])
        chunks = (chunk for chunk in s.iter_content(chunk_size=1024)
                  if chunk)

        if to_uri.scheme.startswith('http'):  # save to remote destination
            with from_uri.get(auth=self.authentication_from.get_auth(),
                              headers=self.authentication_from.get_headers(),
                              stream=True) as r_get:
                r_put = to_uri.put(
                    data=chunks,
                    auth=self.authentication_to.get_auth(),
                    headers=self.authentication_to.get_headers()
                )
                r_put.raise_for_status()
        else:  # save to local
            path = pathlib.Path(to_uri)
            path.parent.mkdir(parents=True, exist_ok=True)
            with open(path, 'wb') as f:
                for chunk in tqdm(chunks,
                                  desc='Downloading',
                                  unit='KB',
                                  total=filesize/1024):
                    f.write(chunk)
        return to_uri.as_uri()
