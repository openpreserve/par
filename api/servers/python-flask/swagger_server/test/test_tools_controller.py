# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.tool import Tool  # noqa: E501
from swagger_server.models.tools import Tools  # noqa: E501
from swagger_server.test import BaseTestCase


class TestToolsController(BaseTestCase):
    """ToolsController integration test stubs"""

    def test_tools_get(self):
        """Test case for tools_get

        Get Tools
        """
        query_string = [('modified_after', 'modified_after_example'),
                        ('modified_before', 'modified_before_example'),
                        ('offset', 0),
                        ('limit', 0)]
        headers = [('guid', 'guid_example'),
                   ('name', 'name_example')]
        response = self.client.open(
            '/par/tools',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_tools_guid_delete(self):
        """Test case for tools_guid_delete

        Delete Tool
        """
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/par/tools/{guid}'.format(guid='guid_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_tools_guid_get(self):
        """Test case for tools_guid_get

        Get a Tool
        """
        response = self.client.open(
            '/par/tools/{guid}'.format(guid='guid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_tools_guid_put(self):
        """Test case for tools_guid_put

        Update Tool
        """
        body = Tool()
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/par/tools/{guid}'.format(guid='guid_example'),
            method='PUT',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json;charset=UTF-8')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_tools_post(self):
        """Test case for tools_post

        Create Tool
        """
        body = Tool()
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/par/tools',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json;charset=UTF-8')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
