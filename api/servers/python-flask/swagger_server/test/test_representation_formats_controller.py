# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.representation_format import RepresentationFormat  # noqa: E501
from swagger_server.models.representation_formats import RepresentationFormats  # noqa: E501
from swagger_server.test import BaseTestCase


class TestRepresentationFormatsController(BaseTestCase):
    """RepresentationFormatsController integration test stubs"""

    def test_representation_formats_get(self):
        """Test case for representation_formats_get

        Get Representation Formats
        """
        query_string = [('modified_after', 'modified_after_example'),
                        ('modified_before', 'modified_before_example'),
                        ('offset', 0),
                        ('limit', 0)]
        headers = [('file_format_guid', 'file_format_guid_example'),
                   ('file_format_name', 'file_format_name_example'),
                   ('format_family_guid', 'format_family_guid_example'),
                   ('format_family_name', 'format_family_name_example'),
                   ('guid', 'guid_example'),
                   ('name', 'name_example')]
        response = self.client.open(
            '/par/representation-formats',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_representation_formats_guid_delete(self):
        """Test case for representation_formats_guid_delete

        Delete Representation Format
        """
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/par/representation-formats/{guid}'.format(guid='guid_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_representation_formats_guid_get(self):
        """Test case for representation_formats_guid_get

        Get a Representation Format
        """
        response = self.client.open(
            '/par/representation-formats/{guid}'.format(guid='guid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_representation_formats_guid_put(self):
        """Test case for representation_formats_guid_put

        Update Representation Format
        """
        body = RepresentationFormat()
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/par/representation-formats/{guid}'.format(guid='guid_example'),
            method='PUT',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json;charset=UTF-8')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_representation_formats_post(self):
        """Test case for representation_formats_post

        Create Representation Format
        """
        body = RepresentationFormat()
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/par/representation-formats',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json;charset=UTF-8')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
