# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.format_families import FormatFamilies  # noqa: E501
from swagger_server.models.format_family import FormatFamily  # noqa: E501
from swagger_server.test import BaseTestCase


class TestFormatFamiliesController(BaseTestCase):
    """FormatFamiliesController integration test stubs"""

    def test_format_families_get(self):
        """Test case for format_families_get

        Get Format Families
        """
        query_string = [('modified_after', 'modified_after_example'),
                        ('modified_before', 'modified_before_example'),
                        ('offset', 0),
                        ('limit', 0)]
        headers = [('file_format', 'file_format_example'),
                   ('guid', 'guid_example')]
        response = self.client.open(
            '/par/format-families',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_format_families_guid_delete(self):
        """Test case for format_families_guid_delete

        Delete Format Family
        """
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/par/format-families/{guid}'.format(guid='guid_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_format_families_guid_get(self):
        """Test case for format_families_guid_get

        Get a Format Family
        """
        response = self.client.open(
            '/par/format-families/{guid}'.format(guid='guid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_format_families_guid_put(self):
        """Test case for format_families_guid_put

        Update Format Family
        """
        body = FormatFamily()
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/par/format-families/{guid}'.format(guid='guid_example'),
            method='PUT',
            data=json.dumps(body),
            content_type='application/json',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_format_families_post(self):
        """Test case for format_families_post

        Create Format Family
        """
        body = FormatFamily()
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/par/format-families',
            method='POST',
            data=json.dumps(body),
            content_type='application/json',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
