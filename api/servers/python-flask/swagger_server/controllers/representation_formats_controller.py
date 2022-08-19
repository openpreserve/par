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
import six

from flask import abort

from swagger_server.forge import factory as FACT
from swagger_server.models.representation_format import RepresentationFormat  # noqa: E501
from swagger_server.models.representation_formats import RepresentationFormats  # noqa: E501
from swagger_server import util


def representation_formats_get(file_format_guid=None, file_format_name=None, format_family_guid=None, format_family_name=None, guid=None, name=None, modified_after=None, modified_before=None, offset=None, limit=None):  # noqa: E501
    """Get Representation Formats

    Returns an array of Representation Formats that match all of the filter conditions supplied. Any number of filters can be used together. The date filters should be supplied as ISO-8601 date times or dates, i.e. yyyy-MM-ddThh:mm:ss.SZ or yyyy-MM-dd. If no time information is supplied, then 00:00:00 in UTC will be assumed. This means that if you supply modified-after and modified-before dates of 2019-01-01 and 2019-12-31, you will not match any RepresentationFormats modified during the day of 31st December. # noqa: E501

    :param file_format_guid: A comma separated list of GUIDs of file formats. This filter matches  only those Business Rules that have been defined to apply to one of  the listed formats. This includes formats where the rule is  applicable indirectly through the format family.
    :type file_format_guid: str
    :param file_format_name: A comma separated list of names of file formats. This filter matches  only those Business Rules that have been defined to apply to one of  the listed formats. This includes formats where the rule is  applicable indirectly through the format family.
    :type file_format_name: str
    :param format_family_guid: A comma separated list of names of formats families. This filter  matches only those Business Rules that have been defined to apply to  one of the listed format families. 
    :type format_family_guid: str
    :param format_family_name: A comma separated list of names of formats families. This filter  matches only those Business Rules that have been defined to apply to  one of the listed format families. 
    :type format_family_name: str
    :param guid: A comma separated list of GUIDs of Representation Formats. This filter matches only those Representation Formats that are identified by one of the listed GUIDs.
    :type guid: str
    :param name: A comma separated list of names of Representation Formats. This filter matches only those Representation Formats that are identified by one of the listed names.
    :type name: str
    :param modified_after: This filter matches only those Representation Formats whose local last modified date is after the specified date.
    :type modified_after: str
    :param modified_before: This filter matches only those Representation Formats whose local last modified date is before the specified date.
    :type modified_before: str
    :param offset: Used for requesting paged responses, this defines the offset of the first RepresentationFormat to return from the start of the list of all matching Representation Formats.
    :type offset: int
    :param limit: Used for requesting paged responses, this defines the maximum number of RepresentationFormats to return.
    :type limit: int

    :rtype: RepresentationFormats
    """
    abort(FACT.method_not_implemented())


def representation_formats_guid_delete(guid, Authorization):  # noqa: E501
    """Delete Representation Format

    Deletes the Representation Format specified by the GUID of the PAR Identifier # noqa: E501

    :param guid: 
    :type guid: str
    :param Authorization: HTTP Basic Auth header
    :type Authorization: str

    :rtype: None
    """
    abort(FACT.method_not_implemented())


def representation_formats_guid_get(guid):  # noqa: E501
    """Get a Representation Format

    Returns the Representation Format specified by the GUID of the PAR Identifier # noqa: E501

    :param guid: 
    :type guid: str

    :rtype: RepresentationFormat
    """
    abort(FACT.method_not_implemented())


def representation_formats_guid_put(guid, Authorization, body=None):  # noqa: E501
    """Update Representation Format

    Updates the Representation Format specified by the GUID of the PAR Identifier and returns the Representation Format as updated. # noqa: E501

    :param guid: 
    :type guid: str
    :param Authorization: HTTP Basic Auth header
    :type Authorization: str
    :param body: Serialised entity in request body
    :type body: dict | bytes

    :rtype: RepresentationFormat
    """
    if connexion.request.is_json:
        body = RepresentationFormat.from_dict(connexion.request.get_json())  # noqa: E501
    abort(FACT.method_not_implemented())


def representation_formats_post(Authorization, body=None):  # noqa: E501
    """Create Representation Format

    Creates a new Representation Format and returns the Representation Format as updated. # noqa: E501

    :param Authorization: HTTP Basic Auth header
    :type Authorization: str
    :param body: Serialised entity in request body
    :type body: dict | bytes

    :rtype: RepresentationFormat
    """
    if connexion.request.is_json:
        body = RepresentationFormat.from_dict(connexion.request.get_json())  # noqa: E501
    abort(FACT.method_not_implemented())
