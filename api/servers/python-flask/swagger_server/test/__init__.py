import logging
import os
import tempfile
import time

import connexion
from flask_testing import TestCase

from swagger_server.encoder import JSONEncoder
from swagger_server.encoder import JSONEncoder

# Template these values for flexible install
TEMP = tempfile.gettempdir()

# pylint: disable=R0903
class TestConfig:
    """Base / default config, no debug logging and short log format."""
    DEBUG = True
    LOG_FILE = os.path.join(TEMP, 'parserver.log')
    LOG_FORMAT = '[%(asctime)s %(levelname)-8s %(filename)-15s:%(lineno)-5d ' +\
                 '%(funcName)-30s] %(message)s'

CONFIGS = {
    'test': 'swagger_server.test.TestConfig'
}


def configure_app(app):
    """Grab the environment variable for app config or defaults to dev."""
    app.config.from_object(CONFIGS['test'])

class BaseTestCase(TestCase):

    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        app = connexion.App(__name__, specification_dir='../swagger/')
        app.app.json_encoder = JSONEncoder
        app.add_api('swagger.yaml')
        configure_app(app.app)
        return app.app
