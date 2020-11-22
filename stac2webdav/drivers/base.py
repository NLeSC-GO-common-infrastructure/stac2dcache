from abc import ABC, abstractmethod
from ..authentication import Authentication


class Driver(ABC):
    """ Driver base class """
    def __init__(self, uri):
        """

        :param uri: URI of the asset to be loaded
        """
        self.uri = uri
        self.authentication = None

    def set_authentication(self, authentication=None):
        """
        Configure driver authentication

        :param authentication: (optional, `~.authentication.Authentication`)
            object including authentication credentials
        """
        self.authentication = authentication or Authentication()

    @abstractmethod
    def get(self, **kwargs):
        """
        Load and return the asset

        :param kwargs: driver-specific arguments
        :return asset
        """
        return
