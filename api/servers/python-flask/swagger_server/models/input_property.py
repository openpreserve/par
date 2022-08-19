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
from swagger_server.models.par_property import ParProperty
from swagger_server import util


class InputProperty(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, description: str=None, name: str=None, par_property: ParProperty=None):  # noqa: E501
        """InputProperty - a model defined in Swagger

        :param description: The description of this InputProperty.  # noqa: E501
        :type description: str
        :param name: The name of this InputProperty.  # noqa: E501
        :type name: str
        :param par_property: The par_property of this InputProperty.  # noqa: E501
        :type par_property: ParProperty
        """
        self.swagger_types = {
            'description': str,
            'name': str,
            'par_property': ParProperty
        }

        self.attribute_map = {
            'description': 'description',
            'name': 'name',
            'par_property': 'parProperty'
        }

        self._description = description
        self._name = name
        self._par_property = par_property

    @classmethod
    def from_dict(cls, dikt) -> 'InputProperty':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InputProperty of this InputProperty.  # noqa: E501
        :rtype: InputProperty
        """
        return util.deserialize_model(dikt, cls)

    @property
    def description(self) -> str:
        """Gets the description of this InputProperty.


        :return: The description of this InputProperty.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this InputProperty.


        :param description: The description of this InputProperty.
        :type description: str
        """

        self._description = description

    @property
    def name(self) -> str:
        """Gets the name of this InputProperty.


        :return: The name of this InputProperty.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this InputProperty.


        :param name: The name of this InputProperty.
        :type name: str
        """

        self._name = name

    @property
    def par_property(self) -> ParProperty:
        """Gets the par_property of this InputProperty.


        :return: The par_property of this InputProperty.
        :rtype: ParProperty
        """
        return self._par_property

    @par_property.setter
    def par_property(self, par_property: ParProperty):
        """Sets the par_property of this InputProperty.


        :param par_property: The par_property of this InputProperty.
        :type par_property: ParProperty
        """

        self._par_property = par_property
