#!/usr/bin/env python3

import connexion
from swagger_server.config import configure_app

from swagger_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'PAR API'})
    # Get the appropriate config
    configure_app(app.app)
    app.run(port=8080)


if __name__ == '__main__':
    main()
