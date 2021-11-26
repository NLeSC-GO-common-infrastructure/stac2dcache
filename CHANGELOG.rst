###########
Change Log
###########

All notable changes to this project will be documented in this file.
This project adheres to `Semantic Versioning <http://semver.org/>`_.


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
