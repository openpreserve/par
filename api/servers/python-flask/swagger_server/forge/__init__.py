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
"""
Handles creation of model instances from Wikidata queries.
"""
# flake8: noqa
from __future__ import absolute_import
# import models into model package
from swagger_server.models.author_information import AuthorInformation
from swagger_server.models.byte_sequence_information import ByteSequenceInformation
from swagger_server.models.developer_information import DeveloperInformation
from swagger_server.models.document_information import DocumentInformation
from swagger_server.models.external_signature_information import ExternalSignatureInformation
from swagger_server.models.file_format import FileFormat
from swagger_server.models.file_formats import FileFormats
from swagger_server.models.format_families import FormatFamilies
from swagger_server.models.format_family import FormatFamily
from swagger_server.models.identifier_information import IdentifierInformation
from swagger_server.models.internal_signature_information import InternalSignatureInformation
from swagger_server.models.par_identifier import ParIdentifier
from swagger_server.models.par_properties import ParProperties
from swagger_server.models.par_property import ParProperty
from swagger_server.models.provenance_information import ProvenanceInformation
from swagger_server.models.publisher_information import PublisherInformation
from swagger_server.models.registry_version_information import RegistryVersionInformation
from swagger_server.models.related_format_information import RelatedFormatInformation
