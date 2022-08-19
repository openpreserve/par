#!/usr/bin/python3
# coding: UTF-8
#
# PAR Consortium
# Copyright (C) 2020
# All rights reserved.
#
# This code is distributed under the terms of the GNU General Public
# License, Version 3. See the text file "COPYING" for further details
# about the terms of this license.

import connexion

from swagger_server import encoder
from swagger_server.config import configure_app


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={'title': 'PAR API'}, pythonic_params=True)
    # Get the appropriate config
    configure_app(app.app)
    app.run(port=8080)


if __name__ == '__main__':
    main()
