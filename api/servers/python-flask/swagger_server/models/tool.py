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
from swagger_server.models.par_identifier import ParIdentifier
from swagger_server import util


class Tool(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, id: ParIdentifier=None, local_last_modified_date: str=None, tool_accepted_parameters: List[str]=None, tool_label: str=None, tool_name: str=None, tool_operating_environments: List[str]=None, tool_publisher: str=None, tool_version: str=None):  # noqa: E501
        """Tool - a model defined in Swagger

        :param id: The id of this Tool.  # noqa: E501
        :type id: ParIdentifier
        :param local_last_modified_date: The local_last_modified_date of this Tool.  # noqa: E501
        :type local_last_modified_date: str
        :param tool_accepted_parameters: The tool_accepted_parameters of this Tool.  # noqa: E501
        :type tool_accepted_parameters: List[str]
        :param tool_label: The tool_label of this Tool.  # noqa: E501
        :type tool_label: str
        :param tool_name: The tool_name of this Tool.  # noqa: E501
        :type tool_name: str
        :param tool_operating_environments: The tool_operating_environments of this Tool.  # noqa: E501
        :type tool_operating_environments: List[str]
        :param tool_publisher: The tool_publisher of this Tool.  # noqa: E501
        :type tool_publisher: str
        :param tool_version: The tool_version of this Tool.  # noqa: E501
        :type tool_version: str
        """
        self.swagger_types = {
            'id': ParIdentifier,
            'local_last_modified_date': str,
            'tool_accepted_parameters': List[str],
            'tool_label': str,
            'tool_name': str,
            'tool_operating_environments': List[str],
            'tool_publisher': str,
            'tool_version': str
        }

        self.attribute_map = {
            'id': 'id',
            'local_last_modified_date': 'localLastModifiedDate',
            'tool_accepted_parameters': 'toolAcceptedParameters',
            'tool_label': 'toolLabel',
            'tool_name': 'toolName',
            'tool_operating_environments': 'toolOperatingEnvironments',
            'tool_publisher': 'toolPublisher',
            'tool_version': 'toolVersion'
        }

        self._id = id
        self._local_last_modified_date = local_last_modified_date
        self._tool_accepted_parameters = tool_accepted_parameters
        self._tool_label = tool_label
        self._tool_name = tool_name
        self._tool_operating_environments = tool_operating_environments
        self._tool_publisher = tool_publisher
        self._tool_version = tool_version

    @classmethod
    def from_dict(cls, dikt) -> 'Tool':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The Tool of this Tool.  # noqa: E501
        :rtype: Tool
        """
        return util.deserialize_model(dikt, cls)

    @property
    def id(self) -> ParIdentifier:
        """Gets the id of this Tool.


        :return: The id of this Tool.
        :rtype: ParIdentifier
        """
        return self._id

    @id.setter
    def id(self, id: ParIdentifier):
        """Sets the id of this Tool.


        :param id: The id of this Tool.
        :type id: ParIdentifier
        """

        self._id = id

    @property
    def local_last_modified_date(self) -> str:
        """Gets the local_last_modified_date of this Tool.


        :return: The local_last_modified_date of this Tool.
        :rtype: str
        """
        return self._local_last_modified_date

    @local_last_modified_date.setter
    def local_last_modified_date(self, local_last_modified_date: str):
        """Sets the local_last_modified_date of this Tool.


        :param local_last_modified_date: The local_last_modified_date of this Tool.
        :type local_last_modified_date: str
        """

        self._local_last_modified_date = local_last_modified_date

    @property
    def tool_accepted_parameters(self) -> List[str]:
        """Gets the tool_accepted_parameters of this Tool.


        :return: The tool_accepted_parameters of this Tool.
        :rtype: List[str]
        """
        return self._tool_accepted_parameters

    @tool_accepted_parameters.setter
    def tool_accepted_parameters(self, tool_accepted_parameters: List[str]):
        """Sets the tool_accepted_parameters of this Tool.


        :param tool_accepted_parameters: The tool_accepted_parameters of this Tool.
        :type tool_accepted_parameters: List[str]
        """

        self._tool_accepted_parameters = tool_accepted_parameters

    @property
    def tool_label(self) -> str:
        """Gets the tool_label of this Tool.


        :return: The tool_label of this Tool.
        :rtype: str
        """
        return self._tool_label

    @tool_label.setter
    def tool_label(self, tool_label: str):
        """Sets the tool_label of this Tool.


        :param tool_label: The tool_label of this Tool.
        :type tool_label: str
        """

        self._tool_label = tool_label

    @property
    def tool_name(self) -> str:
        """Gets the tool_name of this Tool.


        :return: The tool_name of this Tool.
        :rtype: str
        """
        return self._tool_name

    @tool_name.setter
    def tool_name(self, tool_name: str):
        """Sets the tool_name of this Tool.


        :param tool_name: The tool_name of this Tool.
        :type tool_name: str
        """

        self._tool_name = tool_name

    @property
    def tool_operating_environments(self) -> List[str]:
        """Gets the tool_operating_environments of this Tool.


        :return: The tool_operating_environments of this Tool.
        :rtype: List[str]
        """
        return self._tool_operating_environments

    @tool_operating_environments.setter
    def tool_operating_environments(self, tool_operating_environments: List[str]):
        """Sets the tool_operating_environments of this Tool.


        :param tool_operating_environments: The tool_operating_environments of this Tool.
        :type tool_operating_environments: List[str]
        """

        self._tool_operating_environments = tool_operating_environments

    @property
    def tool_publisher(self) -> str:
        """Gets the tool_publisher of this Tool.


        :return: The tool_publisher of this Tool.
        :rtype: str
        """
        return self._tool_publisher

    @tool_publisher.setter
    def tool_publisher(self, tool_publisher: str):
        """Sets the tool_publisher of this Tool.


        :param tool_publisher: The tool_publisher of this Tool.
        :type tool_publisher: str
        """

        self._tool_publisher = tool_publisher

    @property
    def tool_version(self) -> str:
        """Gets the tool_version of this Tool.


        :return: The tool_version of this Tool.
        :rtype: str
        """
        return self._tool_version

    @tool_version.setter
    def tool_version(self, tool_version: str):
        """Sets the tool_version of this Tool.


        :param tool_version: The tool_version of this Tool.
        :type tool_version: str
        """

        self._tool_version = tool_version