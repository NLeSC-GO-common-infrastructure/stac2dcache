.. list-table::
   :widths: 25 25
   :header-rows: 1

   * - fair-software.nl recommendations
     - Badges
   * - \1. Code repository
     - |GitHub Badge|
   * - \2. License
     - |License Badge|
   * - \3. Community Registry
     - |PyPI Badge|
   * - \4. Enable Citation
     - |Zenodo Badge|
   * - \5. Checklist
     - |CII Best Practices Badge|
   * - **Other best practices**
     -
   * - Continuous integration
     - |Python Build| |PyPI Publish|
   * - Documentation
     - |Read the Docs|

.. |GitHub Badge| image:: https://img.shields.io/badge/github-repo-000.svg?logo=github&labelColor=gray&color=blue
   :target: https://github.com/NLeSC-GO-common-infrastructure/stac2dcache
   :alt: GitHub Badge

.. |License Badge| image:: https://img.shields.io/github/license/NLeSC-GO-common-infrastructure/stac2dcache
   :target: https://github.com/NLeSC-GO-common-infrastructure/stac2dcache
   :alt: License Badge

.. |PyPI Badge| image:: https://img.shields.io/pypi/v/stac2dcache.svg?colorB=blue
   :target: https://pypi.python.org/project/stac2dcache/
   :alt: PyPI Badge

.. |Zenodo Badge| image:: https://zenodo.org/badge/DOI/10.5281/zenodo.7268267.svg
   :target: https://doi.org/10.5281/zenodo.7268267
   :alt: Zenodo Badge

.. |CII Best Practices Badge| image:: https://bestpractices.coreinfrastructure.org/projects/6561/badge
   :target: https://bestpractices.coreinfrastructure.org/projects/6561
   :alt: CII Best Practices Badge

.. |Python Build| image:: https://github.com/NLeSC-GO-common-infrastructure/stac2dcache/workflows/Build/badge.svg
   :target: https://github.com/NLeSC-GO-common-infrastructure/stac2dcache/actions?query=workflow%3A%22Build%22
   :alt: Python Build

.. |PyPI Publish| image:: https://github.com/NLeSC-GO-common-infrastructure/stac2dcache/workflows/Publish/badge.svg
   :target: https://github.com/NLeSC-GO-common-infrastructure/stac2dcache/actions?query=workflow%3A%22Publish%22
   :alt: PyPI Publish

.. |Read the Docs| image:: https://readthedocs.org/projects/stac2dcache/badge/?version=latest
   :target: https://stac2dcache.readthedocs.io
   :alt: Read the Docs

################################################################################
STAC2dCache
################################################################################

STAC2dCache is a Python tool to create and manipulate STAC catalogs on a 
dCache storage system such as the 
`infrastructure available at SURF <http://doc.grid.surfsara.nl/en/latest/Pages/Advanced/grid_storage.html>`_. 
It is based on `PySTAC <https://github.com/stac-utils/pystac>`_ and it offers the 
following additional functionalities:

* download remote assets to the local filesystem or to a dCache storage;
* load assets using a set of predefined drivers (e.g. for raster data, and
  text files)

Installation
------------

STAC2dCache requires Python>=3.8. To install the package, do:

.. code-block:: console

  pip install stac2dcache

or:

.. code-block:: console

  git clone https://github.com/NLeSC-GO-common-infrastructure/stac2dcache.git
  cd stac2dcache
  pip install .


Run tests (including coverage) with:

.. code-block:: console

  python setup.py test


Documentation
-------------

The project's full documentation can be found `here`_, where a notebook tutorial (also available `in this repository`_)
illustrates how to use STAC2dCache.

.. _here: https://stac2dcache.readthedocs.io
.. _in this repository: notebooks/tutorial.ipynb

Contributing
------------

If you want to contribute to the development of STAC2dCache,
have a look at the `contribution guidelines <CONTRIBUTING.rst>`_.

License
-------

Copyright (c) 2020, Netherlands eScience Center

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

Credits
-------

This package was created with `Cookiecutter <https://github.com/audreyr/cookiecutter>`_ and the `NLeSC/python-template <https://github.com/NLeSC/python-template>`_.
