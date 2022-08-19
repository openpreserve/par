# coding: utf-8

from __future__ import absolute_import

from flask import json
from six import BytesIO

from swagger_server.models.business_rule import BusinessRule  # noqa: E501
from swagger_server.models.business_rules import BusinessRules  # noqa: E501
from swagger_server.test import BaseTestCase


class TestBusinessRulesController(BaseTestCase):
    """BusinessRulesController integration test stubs"""

    def test_business_rules_get(self):
        """Test case for business_rules_get

        Get Business Rules
        """
        query_string = [('modified_after', 'modified_after_example'),
                        ('modified_before', 'modified_before_example'),
                        ('offset', 0),
                        ('limit', 0)]
        headers = [('preservation_action_guid', 'preservation_action_guid_example'),
                   ('preservation_action_name', 'preservation_action_name_example'),
                   ('preservation_action_type_guid', 'preservation_action_type_guid_example'),
                   ('preservation_action_type_name', 'preservation_action_type_name_example'),
                   ('file_format_guid', 'file_format_guid_example'),
                   ('file_format_name', 'file_format_name_example'),
                   ('format_family_guid', 'format_family_guid_example'),
                   ('format_family_name', 'format_family_name_example'),
                   ('guid', 'guid_example'),
                   ('name', 'name_example')]
        response = self.client.open(
            '/par/business-rules',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_business_rules_guid_delete(self):
        """Test case for business_rules_guid_delete

        Delete Business Rule
        """
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/par/business-rules/{guid}'.format(guid='guid_example'),
            method='DELETE',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_business_rules_guid_get(self):
        """Test case for business_rules_guid_get

        Get a Business Rule
        """
        response = self.client.open(
            '/par/business-rules/{guid}'.format(guid='guid_example'),
            method='GET')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_business_rules_guid_put(self):
        """Test case for business_rules_guid_put

        Update Business Rule
        """
        body = BusinessRule()
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/par/business-rules/{guid}'.format(guid='guid_example'),
            method='PUT',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json;charset=UTF-8')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_business_rules_post(self):
        """Test case for business_rules_post

        Create Business Rule
        """
        body = BusinessRule()
        headers = [('Authorization', 'Authorization_example')]
        response = self.client.open(
            '/par/business-rules',
            method='POST',
            data=json.dumps(body),
            headers=headers,
            content_type='application/json;charset=UTF-8')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()
