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
        headers = [('file_format_guid', 'file_format_guid_example'),
                   ('file_format_name', 'file_format_name_example'),
                   ('guid', 'guid_example'),
                   ('name', 'name_example')]
        response = self.client.open(
            '/par/format-families',
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_format_families_guid_get(self):
        """Test case for format_families_guid_get

        Get a Format Family
        """
        response = self.client.open(
            '/par/format-families/{guid}'.format(guid='guid_example'),
            method='GET')
        self.assert404(response,
                       'Response body is : ' + response.data.decode('utf-8'))

if __name__ == '__main__':
    import unittest
    unittest.main()
