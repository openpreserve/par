# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.preservation_action_type import PreservationActionType  # noqa: E501
from swagger_server.models.preservation_action_types import PreservationActionTypes  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPreservationActionTypesController(BaseTestCase):
    """PreservationActionTypesController integration test stubs"""

    def test_preservation_action_types_get(self):
        """Test case for preservation_action_types_get

        Get Preservation Action Types
        """
        query_string = [('modified_after', 'modified_after_example'),
                        ('modified_before', 'modified_before_example'),
                        ('offset', 0),
                        ('limit', 0)]
        headers = [('guid', 'guid_example'),
                   ('name', 'name_example')]
        response = self.client.open(
            '/par/preservation-action-types',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_preservation_action_types_guid_delete(self):
        """Test case for preservation_action_types_guid_delete

        Delete Preservation Action Type
        """
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/par/preservation-action-types/{guid}'.format(guid='guid_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_preservation_action_types_guid_get(self):
        """Test case for preservation_action_types_guid_get

        Get a Preservation Action Type
        """
        response = self.client.open(
            '/par/preservation-action-types/{guid}'.format(guid='guid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_preservation_action_types_guid_put(self):
        """Test case for preservation_action_types_guid_put

        Update Preservation Action Type
        """
        body = PreservationActionType()
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/par/preservation-action-types/{guid}'.format(guid='guid_example'),
            method='PUT',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json;charset=UTF-8')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_preservation_action_types_post(self):
        """Test case for preservation_action_types_post

        Create Preservation Action Type
        """
        body = PreservationActionType()
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/par/preservation-action-types',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json;charset=UTF-8')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
