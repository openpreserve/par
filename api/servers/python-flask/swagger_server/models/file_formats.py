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
from swagger_server.models.file_format import FileFormat
from swagger_server import util


class FileFormats(Model):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    def __init__(self, file_formats: List[FileFormat]=None):  # noqa: E501
        """FileFormats - a model defined in Swagger

        :param file_formats: The file_formats of this FileFormats.  # noqa: E501
        :type file_formats: List[FileFormat]
        """
        self.swagger_types = {
            'file_formats': List[FileFormat]
        }

        self.attribute_map = {
            'file_formats': 'fileFormats'
        }

        self._file_formats = file_formats

    @classmethod
    def from_dict(cls, dikt) -> 'FileFormats':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The FileFormats of this FileFormats.  # noqa: E501
        :rtype: FileFormats
        """
        return util.deserialize_model(dikt, cls)

    @property
    def file_formats(self) -> List[FileFormat]:
        """Gets the file_formats of this FileFormats.


        :return: The file_formats of this FileFormats.
        :rtype: List[FileFormat]
        """
        return self._file_formats

    @file_formats.setter
    def file_formats(self, file_formats: List[FileFormat]):
        """Sets the file_formats of this FileFormats.


        :param file_formats: The file_formats of this FileFormats.
        :type file_formats: List[FileFormat]
        """

        self._file_formats = file_formats