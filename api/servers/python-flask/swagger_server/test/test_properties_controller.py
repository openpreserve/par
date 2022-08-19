# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.par_properties import ParProperties  # noqa: E501
from swagger_server.models.par_property import ParProperty  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPropertiesController(BaseTestCase):
    """PropertiesController integration test stubs"""

    def test_properties_get(self):
        """Test case for properties_get

        Get Properties
        """
        query_string = [('modified_after', 'modified_after_example'),
                        ('modified_before', 'modified_before_example'),
                        ('offset', 0),
                        ('limit', 0)]
        headers = [('guid', 'guid_example'),
                   ('name', 'name_example')]
        response = self.client.open(
            '/par/properties',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_properties_guid_delete(self):
        """Test case for properties_guid_delete

        Delete Property
        """
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/par/properties/{guid}'.format(guid='guid_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_properties_guid_get(self):
        """Test case for properties_guid_get

        Get a Property
        """
        response = self.client.open(
            '/par/properties/{guid}'.format(guid='guid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_properties_guid_put(self):
        """Test case for properties_guid_put

        Update Property
        """
        body = ParProperty()
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/par/properties/{guid}'.format(guid='guid_example'),
            method='PUT',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json;charset=UTF-8')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_properties_post(self):
        """Test case for properties_post

        Create Property
        """
        body = ParProperty()
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/par/properties',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json;charset=UTF-8')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
