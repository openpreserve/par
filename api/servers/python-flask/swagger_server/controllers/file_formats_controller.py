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
"""Wrapping for all format web methods."""
from flask import abort, request
from swagger_server.models.file_formats import FileFormats  # noqa: E501
import swagger_server.forge.factory as FACT

def file_formats_get(guid=None, modified_after=None, modified_before=None,
                     offset=None, limit=None):  # noqa: E501
    """Get File Formats

    Returns an array of File Formats that match all of the filter conditions supplied.
    Any number of filters can be used together. The date filters should be supplied as
    ISO-8601 date times or dates, i.e. yyyy-MM-ddThh:mm:ss.SZ or yyyy-MM-dd.
    f no time information is supplied, then 00:00:00 in UTC will be assumed.
    This means that if you supply modified-after and modified-before dates of
    2019-01-01 and 2019-12-31, you will not match any FileFormats modified during
    the day of 31st December. # noqa: E501

    :param guid: A comma separated list of GUIDs of FileFormats.This filter matches
    only those File Formats that are identified by one of the listed GUIDs.
    :type guid: str
    :param modified_after: This filter matches only those File Formats whose local
    last modified date is after the specified date.
    :type modified_after: str
    :param modified_before: This filter matches only those File Formats whose local
    last modified date is before the specified date.
    :type modified_before: str
    :param offset: Used for requesting paged responses, this defines the offset of
    the first FileFormat to return from the start of the list of all matching File Formats.
    :type offset: int
    :param limit: Used for requesting paged responses, this defines the maximum number
    of FileFormats to return.
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


def file_formats_guid_get(name):  # noqa: E501
    """Get a File Format

    Returns the File Format specified by the name of the PAR Identifier # noqa: E501

    :param name:
    :type guid: str

    :rtype: FileFormat
    """
    ret_val = FACT.get_format(name)
    if not ret_val:
        abort(404)
    return ret_val
