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
from swagger_server.models.preservation_action_type import PreservationActionType  # noqa: E501
from swagger_server.models.preservation_action_types import PreservationActionTypes  # noqa: E501
from swagger_server import util


def preservation_action_types_get(guid=None, name=None, modified_after=None, modified_before=None, offset=None, limit=None):  # noqa: E501
    """Get Preservation Action Types

    Returns an array of Preservation Action Types that match all of the filter conditions supplied. Any number of filters can be used together. The date filters should be supplied as ISO-8601 date times or dates, i.e. yyyy-MM-ddThh:mm:ss.SZ or yyyy-MM-dd. If no time information is supplied, then 00:00:00 in UTC will be assumed. This means that if you supply modified-after and modified-before dates of 2019-01-01 and 2019-12-31, you will not match any Preservation Action Types modified during the day of 31st December. # noqa: E501

    :param guid: A comma separated list of GUIDs of Preservation Action Types. This filter matches only those Preservation Action Types that are identified by one of the listed GUIDs.
    :type guid: str
    :param name: A comma separated list of names of Preservation Action Types. This filter matches only those Preservation Action Types that are identified by one of the listed names.
    :type name: str
    :param modified_after: This filter matches only those Preservation Action Types whose local last modified date is after the specified date.
    :type modified_after: str
    :param modified_before: This filter matches only those Preservation Action Types whose local last modified date is before the specified date.
    :type modified_before: str
    :param offset: Used for requesting paged responses, this defines the offset of the first Preservation Action Type to return from the start of the list of all matching Preservation Action Types.
    :type offset: int
    :param limit: Used for requesting paged responses, this defines the maximum number of Preservation Action Types to return.
    :type limit: int

    :rtype: PreservationActionTypes
    """
    abort(FACT.method_not_implemented())


def preservation_action_types_guid_delete(guid, Authorization):  # noqa: E501
    """Delete Preservation Action Type

    Deletes the Preservation Action Type specified by the GUID of the PAR Identifier # noqa: E501

    :param guid: 
    :type guid: str
    :param Authorization: HTTP Basic Auth header
    :type Authorization: str

    :rtype: None
    """
    abort(FACT.method_not_implemented())


def preservation_action_types_guid_get(guid):  # noqa: E501
    """Get a Preservation Action Type

    Returns the Preservation Action Type specified by the GUID of the PAR Identifier # noqa: E501

    :param guid: 
    :type guid: str

    :rtype: PreservationActionType
    """
    abort(FACT.method_not_implemented())


def preservation_action_types_guid_put(guid, Authorization, body=None):  # noqa: E501
    """Update Preservation Action Type

    Updates the Preservation Action Type specified by the GUID of the PAR Identifier and returns the type as updated. # noqa: E501

    :param guid: 
    :type guid: str
    :param Authorization: HTTP Basic Auth header
    :type Authorization: str
    :param body: Serialised entity in request body
    :type body: dict | bytes

    :rtype: PreservationActionType
    """
    if connexion.request.is_json:
        body = PreservationActionType.from_dict(connexion.request.get_json())  # noqa: E501
    abort(FACT.method_not_implemented())


def preservation_action_types_post(Authorization, body=None):  # noqa: E501
    """Create Preservation Action Type

    Creates a new Preservation Action Type and returns the type as created. # noqa: E501

    :param Authorization: HTTP Basic Auth header
    :type Authorization: str
    :param body: Serialised entity in request body
    :type body: dict | bytes

    :rtype: PreservationActionType
    """
    if connexion.request.is_json:
        body = PreservationActionType.from_dict(connexion.request.get_json())  # noqa: E501
    abort(FACT.method_not_implemented())
