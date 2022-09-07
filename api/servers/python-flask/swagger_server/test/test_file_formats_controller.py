# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.file_format import FileFormat  # noqa: E501
from swagger_server.models.file_formats import FileFormats  # noqa: E501
from swagger_server.test import BaseTestCase


class TestFileFormatsController(BaseTestCase):
    """FileFormatsController integration test stubs"""

    def test_file_formats_get(self):
        """Test case for file_formats_get

        Get File Formats
        """
        query_string = [('modified_after', 'modified_after_example'),
                        ('modified_before', 'modified_before_example'),
                        ('offset', 0),
                        ('limit', 0)]
        headers = [('guid', 'guid_example'),
                   ('name', 'name_example')]
        response = self.client.open(
            '/par/file-formats',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_file_formats_guid_get(self):
        """Test case for file_formats_guid_get

        Get a File Format
        """
        response = self.client.open(
            '/par/file-formats/{guid}'.format(guid='a12d90c2-d42e-5cc9-a49a-8980ccde81aa'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_file_formats_guid_get_missing(self):
        """Test case for file_formats_guid_get

        Get a File Format
        """
        response = self.client.open(
            '/par/file-formats/{guid}'.format(guid='guid_example'),
            method='GET')
        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
