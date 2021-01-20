import dcachefs
import fsspec
import urlpath

from pystac import STAC_IO


class IO:
    """ Object to perform IO tasks with `fsspec` compatible file systems """
    def __init__(self, filesystem_from=None, filesystem_to=None):
        """
        :param filesystem_from: (`fsspec` compatible FileSystem instance)
            file system for input source
        :param filesystem_to: (`fsspec` compatible FileSystem instance)
            file system for output destination
        """
        self.filesystem_from = filesystem_from
        self.filesystem_to = filesystem_to

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
        fs = self.filesystem_from or fsspec
        with fs.open(uri) as f:
            return f.read()

    def write(self, uri, text):
        """
        Write to local or remote file system

        :param uri: (string) URI where to write to
        :param text: (string) text to be written
        """
        fs = self.filesystem_to or fsspec
        with fs.open(uri, "w") as f:
            return f.write(text)

    def copy(self, from_uri, to_uri):
        """
        Copy a file from the source to the destination file system

        :param from_uri: (str) URI of the file to copy
        :param to_uri: (str) URI of the folder where to save the file
        """
        from_uri = urlpath.URL(from_uri)
        to_uri = urlpath.URL(to_uri) / from_uri.name

        fs_from = self.filesystem_from or fsspec
        fs_to = self.filesystem_to or fsspec
        with fs_from.open(from_uri.as_uri(), "rb") as f_read:
            with fs_to.open(to_uri.as_uri(), "wb") as f_write:
                if isinstance(self.filesystem_to, dcachefs.dCacheFileSystem):
                    f_write.write(f_read)  # stream upload of file-like object
                else:
                    data = True
                    while data:
                        data = f_read.read(5*2**20)
                        f_write.write(data)

        return to_uri.as_uri()
