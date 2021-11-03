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
"""Wrapping for all format family web methods."""
import connexion

from flask import abort

from swagger_server.models.format_families import FormatFamilies  # noqa: E501
from swagger_server.models.format_family import FormatFamily  # noqa: E501

from swagger_server.forge import factory as FACT

def format_families_get(file_format=None, guid=None, modified_after=None,
                        modified_before=None, offset=None, limit=None):  # noqa: E501
    """Get Format Families

    Returns an array of Format Families that match all of the filter conditions supplied.
    Any number of filters can be used together. The date filters should be supplied as
    ISO-8601 date times or dates, i.e. yyyy-MM-ddThh:mm:ss.SZ or yyyy-MM-dd. If no time
    information is supplied, then 00:00:00 in UTC will be assumed. This means that if you
    supply modified-after and modified-before dates of 2019-01-01 and 2019-12-31, you
    will not match any Format Families modified during the day of 31st December. # noqa: E501

    :param file_format: A comma separated list of NAMEs of file formats
    (i.e. fmt/1, x-fmt/2. This filter matches only those Format Families that include
    any of the specified formats.
    :type file_format: str
    :param guid: A comma separated list of GUIDs of Format Families. This filter matches
    only those Format Families that are identified by one of the listed GUIDs.
    :type guid: str
    :param modified_after: This filter matches only those Format Families whose local
    last modified date is after the specified date.
    :type modified_after: str
    :param modified_before: This filter matches only those Format Families whose local
    last modified date is before the specified date.
    :type modified_before: str
    :param offset: Used for requesting paged responses, this defines the offset of the
    first Format Family to return from the start of the list of all matching Format
    Families.
    :type offset: int
    :param limit: Used for requesting paged responses, this defines the maximum number
    of Format Families to return.
    :type limit: int

    :rtype: FormatFamilies
    """
    result_set = FACT.get_format_families()
    if guid:
        result_set = filter(lambda family: family.id.guid==guid, result_set)
    return FormatFamilies(FACT.slice_list(result_set, limit, offset))

def format_families_guid_delete(guid, Authorization):  # noqa: E501
    """Delete Format Family

    Deletes the Format Family specified by the GUID of the PAR Identifier # noqa: E501

    :param guid:
    :type guid: str
    :param Authorization: HTTP Basic Auth header
    :type Authorization: str

    :rtype: FormatFamily
    """
    abort(FACT.method_not_allowed())


def format_families_guid_get(guid):  # noqa: E501
    """Get a Format Family

    Returns the Format Family specified by the GUID of the PAR Identifier # noqa: E501

    :param guid:
    :type guid: str

    :rtype: FormatFamily
    """
    ret_val = FACT.get_format_family(guid)
    if not ret_val:
        abort(404)
    return ret_val


def format_families_guid_put(guid, Authorization, body=None):  # noqa: E501
    """Update Format Family

    Updates the Format Family specified by the GUID of the PAR Identifier and returns
    the family as updated. # noqa: E501

    :param guid:
    :type guid: str
    :param Authorization: HTTP Basic Auth header
    :type Authorization: str
    :param body: Serialised entity in request body
    :type body: dict | bytes

    :rtype: FormatFamily
    """
    if connexion.request.is_json:
        body = FormatFamily.from_dict(connexion.request.get_json())  # noqa: E501
    abort(FACT.method_not_allowed())


def format_families_post(Authorization, body=None):  # noqa: E501
    """Create Format Family

    Creates a new Format Family and returns the family as created. # noqa: E501

    :param Authorization: HTTP Basic Auth header
    :type Authorization: str
    :param body: Serialised entity in request body
    :type body: dict | bytes

    :rtype: FormatFamily
    """
    if connexion.request.is_json:
        body = FormatFamily.from_dict(connexion.request.get_json())  # noqa: E501
    abort(FACT.method_not_allowed())
