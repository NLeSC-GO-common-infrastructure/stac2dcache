import requests


class Authentication:
    """ Tools to authenticate the connection to the WebDAV server """
    def __init__(self, username=None, password=None, token=None):

        if username is not None or password is not None:
            if username is None or password is None:
                raise ValueError('Username or password not provided')

        if password is not None and token is not None:
            raise ValueError('Provide either token or username/password')

        self.username = username
        self.password = password
        self.token = token

    def get_headers(self):
        """
        Return HTTP headers

        :return (dictionary) headers with the token
        """
        headers = None
        if self.token is not None:
            headers = dict(Authorization=f'Bearer {self.token}')
        return headers

    def get_auth(self):
        """
        Return authentication credentials

        :return (tuple) username and password
        """
        auth = None
        if self.username is not None and self.password is not None:
            auth = (self.username, self.password)
        return auth

    def check(self, url):
        """
        Check connection to URL

        :param url: (string)
        """
        response = requests.head(url=url,
                                 auth=self.get_auth(),
                                 headers=self.get_headers())
        return response.status_code == 200
