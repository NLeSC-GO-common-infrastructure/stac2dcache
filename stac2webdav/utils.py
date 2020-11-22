import geopandas
import urlpath

from .authentication import Authentication
from .drivers import get_driver
from .io import IO


def catalog2geopandas(catalog):
    """
    Create a geopandas data-frame with the catalog items

    :param catalog: (:class:`~pystac.Catalog`) input catalog
    :return: :class:`~geopandas.GeoDataFrame`
    """
    items = catalog.get_all_items()
    return geopandas.GeoDataFrame.from_features((item.to_dict()
                                                 for item in items))


def download_asset(catalog, asset_key, update_catalog=False, item_id=None,
                   to_uri=None, authentication_from=None,
                   authentication_to=None):
    """
    Download an asset for (one of) the items of a catalog

    :param catalog: (:class:`~pystac.Catalog`) input catalog
    :param asset_key: (str) asset key
    :param update_catalog: (bool) update the catalog links to the new asset
        location (default: False)
    :param item_id: (optional, str) item ID (default: retrieve assets for all
        items of the catalog)
    :param to_uri: (optional, str) URI of the folder where to save the assets
        (default: the catalog's item directories)
    :param authentication_from: (optional) dictionary containing source
        authentication credentials or :class:`~.authentication.Authentication`
    :param authentication_to: (optional) dictionary containing destination
        authentication credentials or :class:`~.authentication.Authentication`
    """
    if isinstance(authentication_from, dict):
        authentication_from = Authentication(**authentication_from)
    if isinstance(authentication_to, dict):
        authentication_to = Authentication(**authentication_to)
    io = IO(authentication_from=authentication_from,
            authentication_to=authentication_to)

    root_href = catalog.get_self_href()
    if root_href is None and to_uri is None:
        raise ValueError('Provide URI where to save the assets '
                         '(or save the catalog to disk)')

    if item_id is not None:
        item = catalog.get_item(item_id, recursive=True)
        if item is not None:
            items = (item,)
        else:
            raise ValueError(f'Item not found: {item_id}')
    else:
        items = catalog.get_all_items()

    for item in items:
        asset = item.assets.get(asset_key)
        if asset is None:
            raise ValueError(f'Asset {asset_key} not found for item {item.id}')
        if to_uri is not None:
            destination = urlpath.URL(to_uri) / item.id
        else:
            destination = urlpath.URL(item.get_self_href()).parent
        new_href = io.download(from_uri=asset.href, to_uri=destination)
        if update_catalog:
            asset.href = new_href  # update link in catalog


def get_asset(catalog, asset_key, item_id, driver=None, authentication=None,
              **kwargs):
    """
    Get an asset from the catalog using one of the available drivers

    :param catalog: (:class:`~pystac.Catalog`) input catalog
    :param asset_key: (str) asset key
    :param item_id: (str) item ID
    :param driver: (optional, str) name of the driver to read the asset
        (default: guess the driver from the asset's extension)
    :param authentication: (optional) dictionary containing authentication
        credentials or :class:`~.authentication.Authentication`
    :param kwargs: (optional) keyword arguments passed on to the driver, e.g.
                   `chunks` for raster data or `blocksize` for text files.
    :return: asset read
    """
    item = catalog.get_item(item_id, recursive=True)
    asset = item.assets.get(asset_key)
    driver = get_driver(uri=asset.href, driver=driver)
    driver.set_authentication(authentication)
    return driver.get(**kwargs)
