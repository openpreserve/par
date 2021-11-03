#!/usr/bin/python
# coding: UTF-8
#
# PAR Consortium
# Copyright (C) 2020
# All rights reserved.
#
# This code is distributed under the terms of the GNU General Public
# License, Version 3. See the text file "COPYING" for further details
# about the terms of this license.
#
""" Setup for the WikiDP PAR API."""
from setuptools import setup, find_packages

NAME = "swagger_server"
VERSION = "0.1.0"

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

REQUIRES = ["connexion","sparqlwrapper"]

setup(
    name=NAME,
    version=VERSION,
    description="PAR API",
    author_email="",
    url="",
    keywords=["Swagger", "PAR API"],
    install_requires=REQUIRES,
    packages=find_packages(),
    package_data={'': ['swagger/swagger.yaml']},
    include_package_data=True,
    entry_points={
        'console_scripts': ['swagger_server=swagger_server.__main__:main']},
    long_description="""\
    API to retrieve and update Business Rules, Preservation Actions etc from a Preservation Action Registries compliant endpoint
    """
)
