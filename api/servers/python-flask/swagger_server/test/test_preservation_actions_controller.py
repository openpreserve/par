# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.preservation_action import PreservationAction  # noqa: E501
from swagger_server.models.preservation_actions import PreservationActions  # noqa: E501
from swagger_server.test import BaseTestCase


class TestPreservationActionsController(BaseTestCase):
    """PreservationActionsController integration test stubs"""

    def test_preservation_actions_get(self):
        """Test case for preservation_actions_get

        Get Preservation Actions
        """
        query_string = [('modified_after', 'modified_after_example'),
                        ('modified_before', 'modified_before_example'),
                        ('offset', 0),
                        ('limit', 0)]
        headers = [('preservation_action_type_guid', 'preservation_action_type_guid_example'),
                   ('preservation_action_type_name', 'preservation_action_type_name_example'),
                   ('tool_guid', 'tool_guid_example'),
                   ('tool_name', 'tool_name_example'),
                   ('guid', 'guid_example'),
                   ('name', 'name_example')]
        response = self.client.open(
            '/par/preservation-actions',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_preservation_actions_guid_delete(self):
        """Test case for preservation_actions_guid_delete

        Delete Preservation Action
        """
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/par/preservation-actions/{guid}'.format(guid='guid_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_preservation_actions_guid_get(self):
        """Test case for preservation_actions_guid_get

        Get a Preservation Action
        """
        response = self.client.open(
            '/par/preservation-actions/{guid}'.format(guid='guid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_preservation_actions_guid_put(self):
        """Test case for preservation_actions_guid_put

        Update Preservation Action
        """
        body = PreservationAction()
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/par/preservation-actions/{guid}'.format(guid='guid_example'),
            method='PUT',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json;charset=UTF-8')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_preservation_actions_post(self):
        """Test case for preservation_actions_post

        Create Preservation Action
        """
        body = PreservationAction()
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/par/preservation-actions',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json;charset=UTF-8')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
