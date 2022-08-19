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
"""Wrapping for all format web methods."""

import connexion
import six

from flask import abort, request

from swagger_server.forge import factory as FACT
from swagger_server.models.file_format import FileFormat  # noqa: E501
from swagger_server.models.file_formats import FileFormats  # noqa: E501
from swagger_server import util


def file_formats_get(guid=None, name=None, modified_after=None, modified_before=None, offset=None, limit=None):  # noqa: E501
    """Get File Formats

    Returns an array of File Formats that match all of the filter conditions supplied. Any number of filters can be used together. The date filters should be supplied as ISO-8601 date times or dates, i.e. yyyy-MM-ddThh:mm:ss.SZ or yyyy-MM-dd. If no time information is supplied, then 00:00:00 in UTC will be assumed. This means that if you supply modified-after and modified-before dates of 2019-01-01 and 2019-12-31, you will not match any FileFormats modified during the day of 31st December. # noqa: E501

    :param guid: A comma separated list of the GUIDs of File Formats. This filter matches only those File Formats that are identified by one of the listed GUIDs.
    :type guid: str
    :param name: A comma separated list of the names of File Formats. This filter matches only those File Formats that are identified by one of the listed names.
    :type name: str
    :param modified_after: This filter matches only those File Formats whose local last modified date is after the specified date.
    :type modified_after: str
    :param modified_before: This filter matches only those File Formats whose local last modified date is before the specified date.
    :type modified_before: str
    :param offset: Used for requesting paged responses, this defines the offset of the first FileFormat to return from the start of the list of all matching File Formats.
    :type offset: int
    :param limit: Used for requesting paged responses, this defines the maximum number of FileFormats to return.
    :type limit: int

    :rtype: FileFormats
    """
    result_set = FACT.get_formats()
    guids = request.headers.get('guid', None)
    if guids:
        result_set = FACT.filter_by_guids(result_set, guids)
    if modified_before or modified_after:
        result_set = FACT.filter_by_date_modified(result_set, modified_before, modified_after)
    return FileFormats(FACT.slice_list(result_set, limit, offset))


def file_formats_guid_delete(guid, Authorization):  # noqa: E501
    """Delete File Format

    Deletes the File Format specified by the Name part of the PAR Identifier # noqa: E501

    :param guid: 
    :type guid: str
    :param Authorization: HTTP Basic Auth header
    :type Authorization: str

    :rtype: None
    """
    abort(FACT.method_not_implemented())


def file_formats_guid_get(guid):  # noqa: E501
    """Get a File Format

    Returns the File Format specified by the Name part of the PAR Identifier # noqa: E501

    :param guid: 
    :type guid: str

    :rtype: FileFormat
    """
    ret_val = FACT.get_format(guid)
    if not ret_val:
        abort(404)
    return ret_val


def file_formats_guid_put(guid, Authorization, body=None):  # noqa: E501
    """Update File Format

    Updates the File Format specified by the Name part of the PAR Identifier and returns the file format as updated. # noqa: E501

    :param guid: 
    :type guid: str
    :param Authorization: HTTP Basic Auth header
    :type Authorization: str
    :param body: Serialised entity in request body
    :type body: dict | bytes

    :rtype: FileFormat
    """
    if connexion.request.is_json:
        body = FileFormat.from_dict(connexion.request.get_json())  # noqa: E501
    abort(FACT.method_not_implemented())


def file_formats_post(Authorization, body=None):  # noqa: E501
    """Create File Format

    Creates a new File Format and returns the fileFormat as created. # noqa: E501

    :param Authorization: HTTP Basic Auth header
    :type Authorization: str
    :param body: Serialised entity in request body
    :type body: dict | bytes

    :rtype: FileFormat
    """
    if connexion.request.is_json:
        body = FileFormat.from_dict(connexion.request.get_json())  # noqa: E501
    abort(FACT.method_not_implemented())
