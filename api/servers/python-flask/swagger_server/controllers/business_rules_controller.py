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
from swagger_server.models.business_rule import BusinessRule  # noqa: E501
from swagger_server.models.business_rules import BusinessRules  # noqa: E501
from swagger_server import util


def business_rules_get(preservation_action_guid=None, preservation_action_name=None, preservation_action_type_guid=None, preservation_action_type_name=None, file_format_guid=None, file_format_name=None, format_family_guid=None, format_family_name=None, guid=None, name=None, modified_after=None, modified_before=None, offset=None, limit=None):  # noqa: E501
    """Get Business Rules

    Returns an array of Business Rules that match all of the filter conditions supplied. Any number of fitlers can be used together. The date filters should be supplied as ISO-8601 date times or dates, i.e. yyyy-MM-ddThh:mm:ss.SZ or yyyy-MM-dd. If no time information is supplied, then 00:00:00 in UTC will be assumed. This means that if you supply modified-after and modified-before dates of 2019-01-01 and 2019-12-31, you will not match any Business Rules modified during the day of 31st December. # noqa: E501

    :param preservation_action_guid: A comma separated list of GUIDs of Preservation Actions. This filter matches only those Business Rules whose purpose is to perform one of the listed actions.
    :type preservation_action_guid: str
    :param preservation_action_name: A comma separated list of names of Preservation Actions. This filter matches only those Business Rules whose purpose is to perform one of the listed actions.
    :type preservation_action_name: str
    :param preservation_action_type_guid: A comma separated list of GUIDs of Preservation Action Types. This filter matches only those Business Rules whose purpose is to perform one of the listed types of action.
    :type preservation_action_type_guid: str
    :param preservation_action_type_name: A comma separated list of name of Preservation Action Types. This filter matches only those Business Rules whose purpose is to perform one of the listed types of action.
    :type preservation_action_type_name: str
    :param file_format_guid: A comma separated list of GUIDs of file formats. This filter matches  only those Business Rules that have been defined to apply to one of  the listed formats. This includes formats where the rule is  applicable indirectly through the format family.
    :type file_format_guid: str
    :param file_format_name: A comma separated list of names of file formats. This filter matches  only those Business Rules that have been defined to apply to one of  the listed formats. This includes formats where the rule is  applicable indirectly through the format family.
    :type file_format_name: str
    :param format_family_guid: A comma separated list of names of formats families. This filter  matches only those Business Rules that have been defined to apply to  one of the listed format families. 
    :type format_family_guid: str
    :param format_family_name: A comma separated list of names of formats families. This filter  matches only those Business Rules that have been defined to apply to  one of the listed format families. 
    :type format_family_name: str
    :param guid: A comma separated list of GUIDs of Business Rules. This filter matches only those Business Rules that are identified by one of the listed GUIDs.
    :type guid: str
    :param name: A comma separated list of names of Business Rules. This filter matches only those Business Rules that are identified by one of the listed names.
    :type name: str
    :param modified_after: This filter matches only those Business Rules whose local last modified date is after the specified date.
    :type modified_after: str
    :param modified_before: This filter matches only those Business Rules whose local last modified date is before the specified date.
    :type modified_before: str
    :param offset: Used for requesting paged responses, this defines the offset of the first Business Rule to return from the start of the list of all matching Business Rules.
    :type offset: int
    :param limit: Used for requesting paged responses, this defines the maximum number of Business Rules to return.
    :type limit: int

    :rtype: BusinessRules
    """
    abort(FACT.method_not_implemented())


def business_rules_guid_delete(guid, Authorization):  # noqa: E501
    """Delete Business Rule

    Deletes the Business Rule specified by the GUID of the PAR Identifier # noqa: E501

    :param guid: 
    :type guid: str
    :param Authorization: HTTP Basic Auth header
    :type Authorization: str

    :rtype: None
    """
    abort(FACT.method_not_implemented())


def business_rules_guid_get(guid):  # noqa: E501
    """Get a Business Rule

    Returns the Business Rule specified by the GUID of the PAR Identifier # noqa: E501

    :param guid: 
    :type guid: str

    :rtype: BusinessRule
    """
    abort(FACT.method_not_implemented())


def business_rules_guid_put(guid, Authorization, body=None):  # noqa: E501
    """Update Business Rule

    Updates the Business Rule specified by the GUID of the PAR Identifier and returns the rule as updated. # noqa: E501

    :param guid: 
    :type guid: str
    :param Authorization: HTTP Basic Auth header
    :type Authorization: str
    :param body: Serialised entity in request body
    :type body: dict | bytes

    :rtype: BusinessRule
    """
    if connexion.request.is_json:
        body = BusinessRule.from_dict(connexion.request.get_json())  # noqa: E501
    abort(FACT.method_not_implemented())


def business_rules_post(Authorization, body=None):  # noqa: E501
    """Create Business Rule

    Creates a new Business Rule and returns the rule as created. # noqa: E501

    :param Authorization: HTTP Basic Auth header
    :type Authorization: str
    :param body: Serialised entity in request body
    :type body: dict | bytes

    :rtype: BusinessRule
    """
    if connexion.request.is_json:
        body = BusinessRule.from_dict(connexion.request.get_json())  # noqa: E501
    abort(FACT.method_not_implemented())
