# RDSS - Preservation Action Registry
*Defining interoperability for Preservation Action Regisitries*

Data model and API definitions to facilitate sharing and exchange of digital preservation best practise within the community and between presevation systems.

## Open Source
The data model, APIs and associated software in this repository are open source, under the terms of the [Apache 2.0 licence](LICENCE).

## Status
Current JSON schemas and API definitions should be considered early drafts and subject to change.

## Getting started
### Project Layout
```
rdss-par
    |- api          The PAR API definitions and documentation.
    |- examples     Practical JSON examples of data model usage.
    |- schemas      The PAR data model defined as JSON schema.
    |- scripts      Helper scripts for testing, etc.
    |- testing      Pytests that validate the examples using the schema.
```

### Dependencies
To run the tests you'll need [Python](https://www.python.org/) 2.7 or higher with the following:
- [`pip`](https://pypi.org/project/pip/) to install Python dependencies;
- [`demjson`](https://pypi.org/project/demjson/) for command line JSON linting;
- [`jsonschema`](https://pypi.org/project/jsonschema/) for JSON schema validation;
- [`pytest`](https://pypi.org/project/pytest/) to run the schema validation tests.

Once you have Pythton and pip you can install the other dependencies so: `pip install -r requirements.txt`

### Testing
Automated testing currently consists of:
- [JSONLint](https://jsonlint.com/) validation of all JSON files in the `api`, `examples` and `schemas` directories; and
- validation of the example sets against the schema using these [Python tests](testing/test_main.py).

To run the tests locally, first run the JSON linting script:
```bash
./scripts/lint-json-dirs

JSONLINT - All files in dir schemas.
===================================
./rdss-par/scripts/../schemas/business_rule.json: ok
./rdss-par/scripts/../schemas/format.json: ok
./rdss-par/scripts/../schemas/par_property.json: ok
./rdss-par/scripts/../schemas/preservation_action.json: ok
./rdss-par/scripts/../schemas/preservation_action_type.json: ok
./rdss-par/scripts/../schemas/tool.json: ok
./rdss-par/scripts/../schemas/types.json: ok

JSONLINT - All files in dir api.
===================================
./rdss-par/scripts/../api/par-api.json: ok

JSONLINT - All files in dir examples.
===================================
./rdss-par/scripts/../examples/br-1.json: ok
./rdss-par/scripts/../examples/br-2.json: ok
./rdss-par/scripts/../examples/br-3.json: ok
./rdss-par/scripts/../examples/fmt-43.json: ok
./rdss-par/scripts/../examples/md5check.json: ok
./rdss-par/scripts/../examples/md5prop.json: ok
./rdss-par/scripts/../examples/md5sum.json: ok

```
then run the `pytest` tests

```bash
pytest

===================== test session starts ===============================
platform linux2 -- Python 2.7.12, pytest-3.6.2, py-1.5.3, pluggy-0.6.0
rootdir: /home/cfw/proj/JISC/rdss-par, inifile:
collected 7 items

testing/test_main.py .......                                                                                                                                                           [100%]

===================== 7 passed in 0.06 seconds ========================
```
## Documentation
Coming soon https://parcore.readme.io
