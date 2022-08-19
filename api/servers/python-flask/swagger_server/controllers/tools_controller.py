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
from swagger_server.models.tool import Tool  # noqa: E501
from swagger_server.models.tools import Tools  # noqa: E501
from swagger_server import util


def tools_get(guid=None, name=None, modified_after=None, modified_before=None, offset=None, limit=None):  # noqa: E501
    """Get Tools

    Returns an array of Tools that match all of the filter conditions supplied. Any number of filters can be used together. The date filters should be supplied as ISO-8601 date times or dates, i.e. yyyy-MM-ddThh:mm:ss.SZ or yyyy-MM-dd. If no time information is supplied, then 00:00:00 in UTC will be assumed. This means that if you supply modified-after and modified-before dates of 2019-01-01 and 2019-12-31, you will not match any Tools modified during the day of 31st December. # noqa: E501

    :param guid: A comma separated list of GUIDs of Tools. This filter matches only those Tools that are identified by one of the listed GUIDs.
    :type guid: str
    :param name: A comma separated list of names of Tools. This filter matches only those Tools that are identified by one of the listed names.
    :type name: str
    :param modified_after: This filter matches only those Tools whose local last modified date is after the specified date.
    :type modified_after: str
    :param modified_before: This filter matches only those Tools whose local last modified date is before the specified date.
    :type modified_before: str
    :param offset: Used for requesting paged responses, this defines the offset of the first Tool to return from the start of the list of all matching Tools.
    :type offset: int
    :param limit: Used for requesting paged responses, this defines the maximum number of Tools to return.
    :type limit: int

    :rtype: Tools
    """
    abort(FACT.method_not_implemented())


def tools_guid_delete(guid, Authorization):  # noqa: E501
    """Delete Tool

    Deletes the Tool specified by the GUID of the PAR Identifier # noqa: E501

    :param guid: 
    :type guid: str
    :param Authorization: HTTP Basic Auth header
    :type Authorization: str

    :rtype: None
    """
    abort(FACT.method_not_implemented())


def tools_guid_get(guid):  # noqa: E501
    """Get a Tool

    Returns the Tool specified by the GUID of the PAR Identifier # noqa: E501

    :param guid: 
    :type guid: str

    :rtype: Tool
    """
    abort(FACT.method_not_implemented())


def tools_guid_put(guid, Authorization, body=None):  # noqa: E501
    """Update Tool

    Updates the Tool specified by the GUID of the PAR Identifier and returns the tool as updated. # noqa: E501

    :param guid: 
    :type guid: str
    :param Authorization: HTTP Basic Auth header
    :type Authorization: str
    :param body: Serialised entity in request body
    :type body: dict | bytes

    :rtype: Tool
    """
    if connexion.request.is_json:
        body = Tool.from_dict(connexion.request.get_json())  # noqa: E501
    abort(FACT.method_not_implemented())


def tools_post(Authorization, body=None):  # noqa: E501
    """Create Tool

    Creates a new Tool and returns the tool as created. # noqa: E501

    :param Authorization: HTTP Basic Auth header
    :type Authorization: str
    :param body: Serialised entity in request body
    :type body: dict | bytes

    :rtype: Tool
    """
    if connexion.request.is_json:
        body = Tool.from_dict(connexion.request.get_json())  # noqa: E501
    abort(FACT.method_not_implemented())
