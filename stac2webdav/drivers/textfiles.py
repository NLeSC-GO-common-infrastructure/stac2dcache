import aiohttp
import dask.bag as db

from .base import Driver


class TextfilesDriver(Driver):
    """ Driver to parse text files """
    def get(self, **kwargs):
        """
        Load the text file using the read_text method from dask.bag

        :param kwargs: (optional) arguments to be passed to read_text
        :return :class:`~dask.bag.core.Bag`
        """
        auth = self.authentication.get_auth()
        if auth is not None:
            auth = aiohttp.BasicAuth(*auth)

        headers = self.authentication.get_headers() or {}

        storage_options = dict(auth=auth, headers=headers)
        return db.read_text(self.uri,
                            storage_options=storage_options,
                            **kwargs)
