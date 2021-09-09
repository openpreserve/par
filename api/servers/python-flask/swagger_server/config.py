#!/usr/bin/python
# coding=UTF-8
#
# WikiDP Wikidata Portal
# Copyright (C) 2020
# All rights reserved.
#
# This code is distributed under the terms of the GNU General Public
# License, Version 3. See the text file "COPYING" for further details
# about the terms of this license.
#
"""Configuration for WikiDP portal Flask app."""
import os
import tempfile

# Template these values for flexible install
HOST = 'localhost'
TEMP = tempfile.gettempdir()


# pylint: disable=R0903
class BaseConfig:
    """Base / default config, no debug logging and short log format."""

    DEBUG = True
    HOST = HOST
    LOG_FILE = os.path.join(TEMP, 'parserver.log')
    LOG_FORMAT = '[%(filename)-15s:%(lineno)-5d] %(message)s'

# pylint: disable=R0903
class DevConfig(BaseConfig):
    """Developer level config, with debug logging and long log format."""

    DEBUG = True
    LOG_FORMAT = '[%(asctime)s %(levelname)-8s %(filename)-15s:%(lineno)-5d ' +\
                 '%(funcName)-30s] %(message)s'

CONFIGS = {
    "dev": 'swagger_server.config.DevConfig',
    "default": 'swagger_server.config.BaseConfig'
}


def configure_app(app):
    """Grab the environment variable for app config or defaults to dev."""
    config_name = os.getenv('WIKIDP_CONFIG', 'dev')
    app.config.from_object(CONFIGS[config_name])
