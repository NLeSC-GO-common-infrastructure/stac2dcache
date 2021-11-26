#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))
version = {}
# To update the package version number, edit stac2dcache/__version__.py
with open(os.path.join(here, 'stac2dcache', '__version__.py')) as f:
    exec(f.read(), version)

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('requirements.txt') as requirements_file:
    requirements = requirements_file.read().split()

extras_require = {
    'test': [
        'pytest',
        'pytest-cov',
        'pycodestyle',
    ],
}

setup(
    name='stac2dcache',
    version=version['__version__'],
    description=('Python tool to create and manipulate '
                 'STAC catalogs on a dCache storage system'),
    long_description=readme + '\n\n',
    author="Team Atlas",
    author_email='team-atlas@esciencecenter.nl',
    url='https://github.com/NLeSC-GO-common-infrastructure/stac2dcache',
    packages=find_packages(),
    include_package_data=True,
    license="Apache Software License 2.0",
    zip_safe=False,
    keywords='stac2dcache',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires=">=3.7",
    install_requires=requirements,
    extras_require=extras_require,
)
