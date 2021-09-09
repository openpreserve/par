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
        headers = [('guid', 'guid_example')]
        response = self.client.open(
            '/par/file-formats',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_file_formats_guid_delete(self):
        """Test case for file_formats_guid_delete

        Delete File Format
        """
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/par/file-formats/{guid}'.format(guid='guid_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_file_formats_guid_get(self):
        """Test case for file_formats_guid_get

        Get a File Format
        """
        response = self.client.open(
            '/par/file-formats/{guid}'.format(guid='guid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_file_formats_guid_put(self):
        """Test case for file_formats_guid_put

        Update File Format
        """
        body = FileFormat()
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/par/file-formats/{guid}'.format(guid='guid_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_file_formats_post(self):
        """Test case for file_formats_post

        Create FileFormat
        """
        body = FileFormat()
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/par/file-formats',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
