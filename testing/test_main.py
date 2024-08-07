"""
Main test methods for schema, etc.
"""
from abc import ABCMeta, abstractmethod
import json
import os
from unittest import TestCase

from jsonschema import validate, FormatChecker, RefResolver # pylint: disable = no-name-in-module

from .const import get_schema_path


class AbstractSchemaValidatorTest(object):
    """
    Main test class.
    """
    __metaclass__ = ABCMeta

    schema_id_path_pairs = [
        (
            "http://www.parcore.org/schema/format.json/#",
            get_schema_path("format.json")
        ),
        (
            "http://www.parcore.org/schema/preservation-action.json/#",
            get_schema_path("preservation-action.json")
        ),
        (
            "http://www.parcore.org/schema/tool.json/#",
            get_schema_path("tool.json")
        ),
        (
            "http://www.parcore.org/schema/business-rule.json/#",
            get_schema_path("business-rule.json")
        ),
        (
            "http://www.parcore.org/schema/preservation-action-type.json/#",
            get_schema_path("preservation-action-type.json")
        ),
        (
            "http://www.parcore.org/schema/types.json/#",
            get_schema_path("types.json")
        ),
        (
            "http://www.parcore.org/schema/par-property.json/#",
            get_schema_path("par-property.json")
        ),
        (
            "http://www.parcore.org/schema/representation-format.json/#",
            get_schema_path("representation-format.json")
        ),
        (
            "http://www.parcore.org/schema/result-list.json/#",
            get_schema_path("result-list.json")
        )
    ]

    dir_path = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))

    @abstractmethod
    def get_json_schema_file_name(self):
        """Return the file name for the JSON schema for the test case."""
        pass

    def validate_json(self, json_file_name):
        """Validate the JSON using the test classes schema file."""
        json_schema = get_json(self.get_json_schema_file_name())
        json_data = get_json(json_file_name)
        validate(
            json_data,
            json_schema,
            resolver=RefResolver('', {}, store={
                schema_id: get_json(schema_path)
                for schema_id, schema_path in self.schema_id_path_pairs
            }),
            format_checker=FormatChecker(),
        )

    def prepare_file_name(self, file_name):
        """Return the file name in a suitable format with the path."""
        return self.dir_path + '/' + file_name

def get_json(file_name):
    """Load JSON data from a file."""
    with open(file_name) as json_data:
        return json.load(json_data)


class FormatTest(AbstractSchemaValidatorTest, TestCase):
    """Test for format Schema."""
    def get_json_schema_file_name(self):
        """Return the format JSON schema file."""
        return 'schema/format.json'

    def test_validation(self):
        """ Test the example. """
        self.validate_json('examples/fmt-43.json')


class PreservationActionTest1(AbstractSchemaValidatorTest, TestCase):
    """Test for preservation action example."""
    def get_json_schema_file_name(self):
        return 'schema/preservation-action.json'

    def test_validation(self):
        """ Test the example. """
        self.validate_json('examples/md5check1.json')

class PreservationActionTest2(AbstractSchemaValidatorTest, TestCase):
    """Test for preservation action example."""
    def get_json_schema_file_name(self):
        return 'schema/preservation-action.json'

    def test_validation(self):
        """ Test the example. """
        self.validate_json('examples/md5check2.json')

class PreservationActionTest3(AbstractSchemaValidatorTest, TestCase):
    """Test for preservation action example."""
    def get_json_schema_file_name(self):
        return 'schema/preservation-action.json'

    def test_validation(self):
        """ Test the example."""
        self.validate_json('examples/mediaInfo2.json')

class Md5sumToolTest(AbstractSchemaValidatorTest, TestCase):
    """Test for preservation tool example."""
    def get_json_schema_file_name(self):
        return 'schema/tool.json'

    def test_validation(self):
        """ Test the example. """
        self.validate_json('examples/md5sum.json')


class FfmpegToolTest(AbstractSchemaValidatorTest, TestCase):
    """Test for preservation tool example."""
    def get_json_schema_file_name(self):
        return 'schema/tool.json'

    def test_validation(self):
        """ Test the example. """
        self.validate_json('examples/ffmpeg.json')


class BusinessRuleTest1(AbstractSchemaValidatorTest, TestCase):
    """Test for business rule example."""
    def get_json_schema_file_name(self):
        return 'schema/business-rule.json'

    def test_validation(self):
        """ Test the example. """
        self.validate_json('examples/br-1.json')

class BusinessRuleTest2(AbstractSchemaValidatorTest, TestCase):
    """Test for business rule example."""
    def get_json_schema_file_name(self):
        return 'schema/business-rule.json'

    def test_validation(self):
        """ Test the example. """
        self.validate_json('examples/br-2.json')

class BusinessRuleTest3(AbstractSchemaValidatorTest, TestCase):
    """Test for business rule example."""
    def get_json_schema_file_name(self):
        return 'schema/business-rule.json'

    def test_validation(self):
        """ Test the example. """
        self.validate_json('examples/br-3.json')


class Md5PropertyTest(AbstractSchemaValidatorTest, TestCase):
    """Test for PAR property example."""
    def get_json_schema_file_name(self):
        return 'schema/par-property.json'

    def test_validation(self):
        """ Test the example. """
        self.validate_json('examples/md5prop.json')


class PassFailPropertyTest(AbstractSchemaValidatorTest, TestCase):
    """Test for pass/fail property example."""
    def get_json_schema_file_name(self):
        return 'schema/par-property.json'

    def test_validation(self):
        """ Test the example. """
        self.validate_json('examples/passfailprop.json')


class AspectRatioPropertyTest(AbstractSchemaValidatorTest, TestCase):
    """Test for ration property example."""
    def get_json_schema_file_name(self):
        return 'schema/par-property.json'

    def test_validation(self):
        """ Test the example. """
        self.validate_json('examples/aspectratioprop.json')


class WidthPropertyTest(AbstractSchemaValidatorTest, TestCase):
    """Test for width property example."""
    def get_json_schema_file_name(self):
        return 'schema/par-property.json'

    def test_validation(self):
        """ Test the example. """
        self.validate_json('examples/ebucorewidthprop.json')

class RepresentationFormatTest(AbstractSchemaValidatorTest, TestCase):
    """Test for Representation Format example. """
    def get_json_schema_file_name(self):
        return 'schema/representation-format.json'

    def test_validation(self):
        """ Test the example. """
        self.validate_json('examples/repfmt-tweet.json')

class ResultListBusinessRulesTest(AbstractSchemaValidatorTest, TestCase):
    """Test for Result List Business Rules example. """
    def get_json_schema_file_name(self):
        return 'schema/result-list.json'

    def test_validation(self):
        """ Test the Business Rules example. """
        self.validate_json('examples/result-list-business-rules.json')

class ResultListToolsTest(AbstractSchemaValidatorTest, TestCase):
    """Test for Result List Tools example. """
    def get_json_schema_file_name(self):
        return 'schema/result-list.json'

    def test_validation(self):
        """ Test the Tools example. """
        self.validate_json('examples/result-list-tools.json')
