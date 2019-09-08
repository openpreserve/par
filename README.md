# RDSS - Preservation Action Registry
*Defining interoperability for Preservation Action Regisitries*

Data model and API definitions to facilitate sharing and exchange of digital preservation best practise within the community and between presevation systems.

## Open Source
The data model, APIs and associated software in this repository are open source, under the terms of the [Apache 2.0 licence](LICENCE).

## Status
Current JSON schemas and API definitions should be considered early drafts and subject to change.

## Getting started
To get started you'll need to clone this GitHub repository:
`git clone https://github.com/JiscRDSS/rdss-par.git`, move to the project
directory: `cd rdss-par/` and update the git submodule to download the examples
directory: `git submodule update --init --recursive`.

An example bash session under linux is shown below:

```bash
cfw@dm-wrkstn:/tmp$ git clone git@github.com:JiscRDSS/rdss-par.git
Cloning into 'rdss-par'...
remote: Enumerating objects: 661, done.
remote: Total 661 (delta 0), reused 0 (delta 0), pack-reused 661
Receiving objects: 100% (661/661), 1.53 MiB | 1.54 MiB/s, done.
Resolving deltas: 100% (358/358), done.

cfw@dm-wrkstn:/tmp$ cd rdss-par/

cfw@dm-wrkstn:/tmp/rdss-par$ git submodule update --init --recursive
Submodule 'examples' (https://github.com/JiscRDSS/rdss-par-examples.git) registered for path 'examples'
Cloning into '/tmp/rdss-par/examples'...
Submodule path 'examples': checked out 'edec3997b38e73d967e7ba1ba3c76345e02097f0'

cfw@dm-wrkstn:/tmp/rdss-par$
```

### Project Layout
```
rdss-par
    |- api          The PAR API definitions and documentation.
    |- docs         The contents of the GitHub pages parecore.org site.
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
```shell
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

```shell
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
