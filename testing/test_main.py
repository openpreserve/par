from abc import ABCMeta, abstractmethod
import json
import os
import sys
from unittest import TestCase

from jsonschema import validate, FormatChecker, RefResolver

from .const import get_schema_path


class AbstractSchemaValidatorTest(object):
    __metaclass__ = ABCMeta

    schema_id_path_pairs = [
        (
            "http://www.parcore.org/schema/format.json/#",
            get_schema_path("format.json")
        ),
        (
            "http://www.parcore.org/schema/preservation_action.json/#",
            get_schema_path("preservation_action.json")
        ),
        (
            "http://www.parcore.org/schema/tool.json/#",
            get_schema_path("tool.json")
        ),
        (
            "http://www.parcore.org/schema/business_rule.json/#",
            "schemas/business_rule.json"
        ),
        (
            "http://www.parcore.org/schema/preservation_action_type.json/#",
            "schemas/preservation_action_type.json"
        ),
        (
            "http://www.parcore.org/schema/types.json/#",
            "schemas/types.json"
        ),
                (
            "http://www.parcore.org/schema/par_property.json/#",
            "schemas/par_property.json"
        ),
    ]

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    @abstractmethod
    def get_json_schema_file_name(self):
        pass

    def validate_json(self, json_file_name):
        json_schema = self.get_json(self.get_json_schema_file_name())
        json_data = self.get_json(json_file_name)
        validate(
            json_data,
            json_schema,
            resolver=RefResolver('', {}, store={
                schema_id: self.get_json(schema_path)
                for schema_id, schema_path in self.schema_id_path_pairs
            }),
            format_checker=FormatChecker(),
        )

    def get_json(self, file_name):
        with open(file_name) as json_data:
            return json.load(json_data)

    def prepare_file_name(self, file_name):
        return self.dir_path + '/' + file_name


class FormatTest(AbstractSchemaValidatorTest, TestCase):
    def get_json_schema_file_name(self):
        return 'schemas/format.json'

    def runTest(self):
        self.validate_json('examples/fmt-43.json')


class PreservationActionTest(AbstractSchemaValidatorTest, TestCase):
    def get_json_schema_file_name(self):
        return 'schemas/preservation_action.json'

    def runTest(self):
        self.validate_json('examples/md5check.json')


class ToolTest(AbstractSchemaValidatorTest, TestCase):
    def get_json_schema_file_name(self):
        return 'schemas/tool.json'

    def runTest(self):
        self.validate_json('examples/md5sum.json')


class BusinessRuleTest1(AbstractSchemaValidatorTest, TestCase):
    def get_json_schema_file_name(self):
        return 'schemas/business_rule.json'

    def runTest(self):
        self.validate_json('examples/br-1.json')

class BusinessRuleTest2(AbstractSchemaValidatorTest, TestCase):
    def get_json_schema_file_name(self):
        return 'schemas/business_rule.json'

    def runTest(self):
        self.validate_json('examples/br-2.json')

class BusinessRuleTest3(AbstractSchemaValidatorTest, TestCase):
    def get_json_schema_file_name(self):
        return 'schemas/business_rule.json'

    def runTest(self):
        self.validate_json('examples/br-3.json')


class PropertyTest(AbstractSchemaValidatorTest, TestCase):
    def get_json_schema_file_name(self):
        return 'schemas/par_property.json'

    def runTest(self):
        self.validate_json('examples/md5prop.json')
