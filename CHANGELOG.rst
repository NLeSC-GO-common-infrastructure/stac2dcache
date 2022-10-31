###########
Change Log
###########

All notable changes to this project will be documented in this file.
This project adheres to `Semantic Versioning <http://semver.org/>`_.


Unreleased
**********


[0.4.0]
*******

Added
-----

* documentation is rendered on readthedocs

Fixed
-----

* rasterio driver updated to work with newer rasterio, pinned version to 1.3.2 until issue #29 is solved
* solved issues with configuration when a configuration file is present

Removed
-------

* catalog2geopandas dropped

Changed
-------

* minor refactoring in stac_io module

[0.3.0]
*******

Added
-----

* filesystems are now set up by default from the URIs' protocols, so no need to use stac_io/filesystem anymore if config files are available.

Changed
-------

* The rasterio driver does not support load=False anymore - at least until raster=1.3 is out. fsspec now takes care of downloading the assets.
* Relative HREFs are used for the assets if possible, making Catalogs more self-contained.


[0.2.1]
*******

Fixed
-----

* Process pool in copy_asset always spawn processes, avoiding issues with async filesystems

Added
-----

* Global configure function


[0.2.0]
*******

Fixed
-----

* Fixed compatibility with PySTAC after refactoring of I/O structure
* Tutorial updated to use the most recent STAC tools and the new NASA CMR ASF namings.

Changed
-------

* Configuration of STAC IO has been updated following changes in PySTAC

[0.1.1]
*******

Fixed
-----

* Bug fix in `copy_asset`, code was executed twice
* Rasterio driver improved (possibility to load data directly)


[0.1.0]
*******

Added
-----

* Empty Python project directory structure
