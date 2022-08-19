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

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from swagger_server.models.base_model_ import Model
from swagger_server.models.preservation_action import PreservationAction
from swagger_server import util


class PreservationActions(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, preservation_actions: List[PreservationAction]=None):  # noqa: E501
        """PreservationActions - a model defined in Swagger

        :param preservation_actions: The preservation_actions of this PreservationActions.  # noqa: E501
        :type preservation_actions: List[PreservationAction]
        """
        self.swagger_types = {
            'preservation_actions': List[PreservationAction]
        }

        self.attribute_map = {
            'preservation_actions': 'preservationActions'
        }

        self._preservation_actions = preservation_actions

    @classmethod
    def from_dict(cls, dikt) -> 'PreservationActions':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PreservationActions of this PreservationActions.  # noqa: E501
        :rtype: PreservationActions
        """
        return util.deserialize_model(dikt, cls)

    @property
    def preservation_actions(self) -> List[PreservationAction]:
        """Gets the preservation_actions of this PreservationActions.


        :return: The preservation_actions of this PreservationActions.
        :rtype: List[PreservationAction]
        """
        return self._preservation_actions

    @preservation_actions.setter
    def preservation_actions(self, preservation_actions: List[PreservationAction]):
        """Sets the preservation_actions of this PreservationActions.


        :param preservation_actions: The preservation_actions of this PreservationActions.
        :type preservation_actions: List[PreservationAction]
        """

        self._preservation_actions = preservation_actions
