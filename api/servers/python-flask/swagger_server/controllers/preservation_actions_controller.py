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
from swagger_server.models.preservation_action import PreservationAction  # noqa: E501
from swagger_server.models.preservation_actions import PreservationActions  # noqa: E501
from swagger_server import util


def preservation_actions_get(preservation_action_type_guid=None, preservation_action_type_name=None, tool_guid=None, tool_name=None, guid=None, name=None, modified_after=None, modified_before=None, offset=None, limit=None):  # noqa: E501
    """Get Preservation Actions

    Returns an array of Preservation Actions that match all of the filter conditions supplied. Any number of filters can be used together. The date filters should be supplied as ISO-8601 date times or dates, i.e. yyyy-MM-ddThh:mm:ss.SZ or yyyy-MM-dd. If no time information is supplied, then 00:00:00 in UTC will be assumed. This means that if you supply modified-after and modified-before dates of 2019-01-01 and 2019-12-31, you will not match any Preservation Actions modified during the day of 31st December. # noqa: E501

    :param preservation_action_type_guid: A comma separated list of GUIDs of Preservation Action Types. This filter matches only those Preservation Actions of one of the listed types of action.
    :type preservation_action_type_guid: str
    :param preservation_action_type_name: A comma separated list of names of Preservation Action Types. This filter matches only those Preservation Actions of one of the listed types of action.
    :type preservation_action_type_name: str
    :param tool_guid: A comma separated list of GUIDs of Tools. This filter matches only those Preservation Actions that use one of the listed tools.
    :type tool_guid: str
    :param tool_name: A comma separated list of names of Tools. This filter matches only those Preservation Actions that use one of the listed tools.
    :type tool_name: str
    :param guid: A comma separated list of GUIDs of Preservation Actions. This filter matches only those Preservation Actions that are identified by one of the listed GUIDs.
    :type guid: str
    :param name: A comma separated list of names of Preservation Actions. This filter matches only those Preservation Actions that are identified by one of the listed names.
    :type name: str
    :param modified_after: This filter matches only those Preservation Actions whose local last modified date is after the specified date.
    :type modified_after: str
    :param modified_before: This filter matches only those Preservation Actions whose local last modified date is before the specified date.
    :type modified_before: str
    :param offset: Used for requesting paged responses, this defines the offset of the first Preservation Action to return from the start of the list of all matching Preservation Actions.
    :type offset: int
    :param limit: Used for requesting paged responses, this defines the maximum number of Preservation Actions to return.
    :type limit: int

    :rtype: PreservationActions
    """
    abort(FACT.method_not_implemented())


def preservation_actions_guid_delete(guid, Authorization):  # noqa: E501
    """Delete Preservation Action

    Deletes the Preservation Action specified by the GUID of the PAR Identifier # noqa: E501

    :param guid: 
    :type guid: str
    :param Authorization: HTTP Basic Auth header
    :type Authorization: str

    :rtype: None
    """
    abort(FACT.method_not_implemented())


def preservation_actions_guid_get(guid):  # noqa: E501
    """Get a Preservation Action

    Returns the Preservation Action specified by the GUID of the PAR Identifier # noqa: E501

    :param guid: 
    :type guid: str

    :rtype: PreservationAction
    """
    abort(FACT.method_not_implemented())


def preservation_actions_guid_put(guid, Authorization, body=None):  # noqa: E501
    """Update Preservation Action

    Updates the Preservation Action specified by the GUID of the PAR Identifier and returns the action as updated. # noqa: E501

    :param guid: 
    :type guid: str
    :param Authorization: HTTP Basic Auth header
    :type Authorization: str
    :param body: Serialised entity in request body
    :type body: dict | bytes

    :rtype: PreservationAction
    """
    if connexion.request.is_json:
        body = PreservationAction.from_dict(connexion.request.get_json())  # noqa: E501
    abort(FACT.method_not_implemented())


def preservation_actions_post(Authorization, body=None):  # noqa: E501
    """Create Preservation Action

    Creates a new Preservation Action and returns the action as created. # noqa: E501

    :param Authorization: HTTP Basic Auth header
    :type Authorization: str
    :param body: Serialised entity in request body
    :type body: dict | bytes

    :rtype: PreservationAction
    """
    if connexion.request.is_json:
        body = PreservationAction.from_dict(connexion.request.get_json())  # noqa: E501
    abort(FACT.method_not_implemented())
