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
from swagger_server.models.input_file import InputFile
from swagger_server.models.input_property import InputProperty
from swagger_server.models.input_tool_argument import InputToolArgument
from swagger_server.models.output_file import OutputFile
from swagger_server.models.output_property import OutputProperty
from swagger_server.models.output_raw import OutputRaw
from swagger_server.models.par_identifier import ParIdentifier
from swagger_server.models.preservation_action_constraints import PreservationActionConstraints
from swagger_server.models.preservation_action_type import PreservationActionType
from swagger_server.models.tool import Tool
from swagger_server import util


class PreservationAction(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, constraints: List[PreservationActionConstraints]=None, description: str=None, example: str=None, id: ParIdentifier=None, input_files: List[InputFile]=None, input_properties: List[InputProperty]=None, input_tool_arguments: List[InputToolArgument]=None, local_last_modified_date: str=None, output_files: List[OutputFile]=None, output_properties: List[OutputProperty]=None, raw_outputs: List[OutputRaw]=None, tool: Tool=None, type: PreservationActionType=None):  # noqa: E501
        """PreservationAction - a model defined in Swagger

        :param constraints: The constraints of this PreservationAction.  # noqa: E501
        :type constraints: List[PreservationActionConstraints]
        :param description: The description of this PreservationAction.  # noqa: E501
        :type description: str
        :param example: The example of this PreservationAction.  # noqa: E501
        :type example: str
        :param id: The id of this PreservationAction.  # noqa: E501
        :type id: ParIdentifier
        :param input_files: The input_files of this PreservationAction.  # noqa: E501
        :type input_files: List[InputFile]
        :param input_properties: The input_properties of this PreservationAction.  # noqa: E501
        :type input_properties: List[InputProperty]
        :param input_tool_arguments: The input_tool_arguments of this PreservationAction.  # noqa: E501
        :type input_tool_arguments: List[InputToolArgument]
        :param local_last_modified_date: The local_last_modified_date of this PreservationAction.  # noqa: E501
        :type local_last_modified_date: str
        :param output_files: The output_files of this PreservationAction.  # noqa: E501
        :type output_files: List[OutputFile]
        :param output_properties: The output_properties of this PreservationAction.  # noqa: E501
        :type output_properties: List[OutputProperty]
        :param raw_outputs: The raw_outputs of this PreservationAction.  # noqa: E501
        :type raw_outputs: List[OutputRaw]
        :param tool: The tool of this PreservationAction.  # noqa: E501
        :type tool: Tool
        :param type: The type of this PreservationAction.  # noqa: E501
        :type type: PreservationActionType
        """
        self.swagger_types = {
            'constraints': List[PreservationActionConstraints],
            'description': str,
            'example': str,
            'id': ParIdentifier,
            'input_files': List[InputFile],
            'input_properties': List[InputProperty],
            'input_tool_arguments': List[InputToolArgument],
            'local_last_modified_date': str,
            'output_files': List[OutputFile],
            'output_properties': List[OutputProperty],
            'raw_outputs': List[OutputRaw],
            'tool': Tool,
            'type': PreservationActionType
        }

        self.attribute_map = {
            'constraints': 'constraints',
            'description': 'description',
            'example': 'example',
            'id': 'id',
            'input_files': 'inputFiles',
            'input_properties': 'inputProperties',
            'input_tool_arguments': 'inputToolArguments',
            'local_last_modified_date': 'localLastModifiedDate',
            'output_files': 'outputFiles',
            'output_properties': 'outputProperties',
            'raw_outputs': 'rawOutputs',
            'tool': 'tool',
            'type': 'type'
        }

        self._constraints = constraints
        self._description = description
        self._example = example
        self._id = id
        self._input_files = input_files
        self._input_properties = input_properties
        self._input_tool_arguments = input_tool_arguments
        self._local_last_modified_date = local_last_modified_date
        self._output_files = output_files
        self._output_properties = output_properties
        self._raw_outputs = raw_outputs
        self._tool = tool
        self._type = type

    @classmethod
    def from_dict(cls, dikt) -> 'PreservationAction':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The PreservationAction of this PreservationAction.  # noqa: E501
        :rtype: PreservationAction
        """
        return util.deserialize_model(dikt, cls)

    @property
    def constraints(self) -> List[PreservationActionConstraints]:
        """Gets the constraints of this PreservationAction.


        :return: The constraints of this PreservationAction.
        :rtype: List[PreservationActionConstraints]
        """
        return self._constraints

    @constraints.setter
    def constraints(self, constraints: List[PreservationActionConstraints]):
        """Sets the constraints of this PreservationAction.


        :param constraints: The constraints of this PreservationAction.
        :type constraints: List[PreservationActionConstraints]
        """

        self._constraints = constraints

    @property
    def description(self) -> str:
        """Gets the description of this PreservationAction.


        :return: The description of this PreservationAction.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description: str):
        """Sets the description of this PreservationAction.


        :param description: The description of this PreservationAction.
        :type description: str
        """

        self._description = description

    @property
    def example(self) -> str:
        """Gets the example of this PreservationAction.


        :return: The example of this PreservationAction.
        :rtype: str
        """
        return self._example

    @example.setter
    def example(self, example: str):
        """Sets the example of this PreservationAction.


        :param example: The example of this PreservationAction.
        :type example: str
        """

        self._example = example

    @property
    def id(self) -> ParIdentifier:
        """Gets the id of this PreservationAction.


        :return: The id of this PreservationAction.
        :rtype: ParIdentifier
        """
        return self._id

    @id.setter
    def id(self, id: ParIdentifier):
        """Sets the id of this PreservationAction.


        :param id: The id of this PreservationAction.
        :type id: ParIdentifier
        """

        self._id = id

    @property
    def input_files(self) -> List[InputFile]:
        """Gets the input_files of this PreservationAction.


        :return: The input_files of this PreservationAction.
        :rtype: List[InputFile]
        """
        return self._input_files

    @input_files.setter
    def input_files(self, input_files: List[InputFile]):
        """Sets the input_files of this PreservationAction.


        :param input_files: The input_files of this PreservationAction.
        :type input_files: List[InputFile]
        """

        self._input_files = input_files

    @property
    def input_properties(self) -> List[InputProperty]:
        """Gets the input_properties of this PreservationAction.


        :return: The input_properties of this PreservationAction.
        :rtype: List[InputProperty]
        """
        return self._input_properties

    @input_properties.setter
    def input_properties(self, input_properties: List[InputProperty]):
        """Sets the input_properties of this PreservationAction.


        :param input_properties: The input_properties of this PreservationAction.
        :type input_properties: List[InputProperty]
        """

        self._input_properties = input_properties

    @property
    def input_tool_arguments(self) -> List[InputToolArgument]:
        """Gets the input_tool_arguments of this PreservationAction.


        :return: The input_tool_arguments of this PreservationAction.
        :rtype: List[InputToolArgument]
        """
        return self._input_tool_arguments

    @input_tool_arguments.setter
    def input_tool_arguments(self, input_tool_arguments: List[InputToolArgument]):
        """Sets the input_tool_arguments of this PreservationAction.


        :param input_tool_arguments: The input_tool_arguments of this PreservationAction.
        :type input_tool_arguments: List[InputToolArgument]
        """

        self._input_tool_arguments = input_tool_arguments

    @property
    def local_last_modified_date(self) -> str:
        """Gets the local_last_modified_date of this PreservationAction.


        :return: The local_last_modified_date of this PreservationAction.
        :rtype: str
        """
        return self._local_last_modified_date

    @local_last_modified_date.setter
    def local_last_modified_date(self, local_last_modified_date: str):
        """Sets the local_last_modified_date of this PreservationAction.


        :param local_last_modified_date: The local_last_modified_date of this PreservationAction.
        :type local_last_modified_date: str
        """

        self._local_last_modified_date = local_last_modified_date

    @property
    def output_files(self) -> List[OutputFile]:
        """Gets the output_files of this PreservationAction.


        :return: The output_files of this PreservationAction.
        :rtype: List[OutputFile]
        """
        return self._output_files

    @output_files.setter
    def output_files(self, output_files: List[OutputFile]):
        """Sets the output_files of this PreservationAction.


        :param output_files: The output_files of this PreservationAction.
        :type output_files: List[OutputFile]
        """

        self._output_files = output_files

    @property
    def output_properties(self) -> List[OutputProperty]:
        """Gets the output_properties of this PreservationAction.


        :return: The output_properties of this PreservationAction.
        :rtype: List[OutputProperty]
        """
        return self._output_properties

    @output_properties.setter
    def output_properties(self, output_properties: List[OutputProperty]):
        """Sets the output_properties of this PreservationAction.


        :param output_properties: The output_properties of this PreservationAction.
        :type output_properties: List[OutputProperty]
        """

        self._output_properties = output_properties

    @property
    def raw_outputs(self) -> List[OutputRaw]:
        """Gets the raw_outputs of this PreservationAction.


        :return: The raw_outputs of this PreservationAction.
        :rtype: List[OutputRaw]
        """
        return self._raw_outputs

    @raw_outputs.setter
    def raw_outputs(self, raw_outputs: List[OutputRaw]):
        """Sets the raw_outputs of this PreservationAction.


        :param raw_outputs: The raw_outputs of this PreservationAction.
        :type raw_outputs: List[OutputRaw]
        """

        self._raw_outputs = raw_outputs

    @property
    def tool(self) -> Tool:
        """Gets the tool of this PreservationAction.


        :return: The tool of this PreservationAction.
        :rtype: Tool
        """
        return self._tool

    @tool.setter
    def tool(self, tool: Tool):
        """Sets the tool of this PreservationAction.


        :param tool: The tool of this PreservationAction.
        :type tool: Tool
        """

        self._tool = tool

    @property
    def type(self) -> PreservationActionType:
        """Gets the type of this PreservationAction.


        :return: The type of this PreservationAction.
        :rtype: PreservationActionType
        """
        return self._type

    @type.setter
    def type(self, type: PreservationActionType):
        """Sets the type of this PreservationAction.


        :param type: The type of this PreservationAction.
        :type type: PreservationActionType
        """

        self._type = type
