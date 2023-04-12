# RDSS - Preservation Action Registry

Defining interoperability for Preservation Action Regisitries

Data model and API definitions to facilitate sharing and exchange of digital preservation best practise within the community and between presevation systems.

## Open Source

The data model, APIs and associated software in this repository are open source, under the terms of the [Apache 2.0 licence](LICENCE).

## Status

Current v1.1 released Nov 2022.

## Getting started

To get started you'll need to clone this GitHub repository:
`git clone https://github.com/openpreserve/par.git`, move to the project
directory: `cd par/` and update the git submodule to download the examples
directory: `git submodule update --init --recursive`.

An example bash session under linux is shown below:

```bash
❯ git clone https://github.com/openpreserve/par.git
Cloning into 'par'...
remote: Enumerating objects: 1810, done.
remote: Counting objects: 100% (103/103), done.
remote: Compressing objects: 100% (68/68), done.
remote: Total 1810 (delta 34), reused 83 (delta 29), pack-reused 1707
Receiving objects: 100% (1810/1810), 9.12 MiB | 27.00 KiB/s, done.
Resolving deltas: 100% (939/939), done.
❯ cd par
❯ git submodule update --init --recursive
Submodule 'examples' (https://github.com/openpreserve/par-examples.git) registered for path 'examples'
Cloning into '/tmp/par/examples'...
Submodule path 'examples': checked out '0ea43f0a0484e02615515186d9e976d5f0ddf8ca'
```

### Project Layout

```shell
par
 |- api          The PAR API definitions and documentation.
 |- docs         The contents of the GitHub pages parecore.org site.
 |- examples     Practical JSON examples of data model usage.
 |- schema       The PAR data model defined as JSON schema.
 |- scripts      Helper scripts for testing, etc.
 |- testing      Pytests that validate the examples using the schema.
```

### Dependencies

To run the tests you'll need [Python](https://www.python.org/) 3.8 or higher with the following:

- [`pip`](https://pypi.org/project/pip/) to install Python dependencies;
- [`demjson`](https://pypi.org/project/demjson/) for command line JSON linting;
- [`jsonschema`](https://pypi.org/project/jsonschema/) for JSON schema validation;
- [`pytest`](https://pypi.org/project/pytest/) to run the schema validation tests.

Once you have Pythton and pip you can install the other dependencies so: `pip install -r requirements.txt`

If the installation of demjson fails with an error similar to the below:

```shell
Collecting demjson                                                                                                                                                                            
  Downloading demjson-2.2.4.tar.gz (131 kB)                                                                                                                                                   
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 131.5/131.5 kB 1.3 MB/s eta 0:00:00                                                                                                             
  Preparing metadata (setup.py) ... error                                                                                                                                                     
  error: subprocess-exited-with-error                                                                                                                                                         
                                                                                                                                                                                              
  × python setup.py egg_info did not run successfully.                                                                                                                                        
  │ exit code: 1                                                                                                                                                                              
  ╰─> [1 lines of output]                                                                                                                                                                     
      error in demjson setup command: use_2to3 is invalid.                                                                                                                                    
      [end of output]                                                                                                                                                                         
                                                                                                                                                                                              
  note: This error originates from a subprocess, and is likely not a problem with pip.                                                                                                        
error: metadata-generation-failed
```

then you will need to install a less recent version of `setuptools` as follows: `pip install "setuptools<58"`. See #55.

### Testing

Automated testing currently consists of:

- [JSONLint](https://jsonlint.com/) validation of all JSON files in the `api`, `examples` and `schemas` directories; and
- validation of the example sets against the schema using these [Python tests](testing/test_main.py).

To run the tests locally, first run the JSON linting script:

```shell
./scripts/lint-json-dirs

JSONLINT - All files in dir schemas.
===================================
./par/scripts/../schemas/business_rule.json: ok
./par/scripts/../schemas/format.json: ok
./par/scripts/../schemas/par_property.json: ok
./par/scripts/../schemas/preservation_action.json: ok
./par/scripts/../schemas/preservation_action_type.json: ok
./par/scripts/../schemas/tool.json: ok
./par/scripts/../schemas/types.json: ok

JSONLINT - All files in dir api.
===================================
./par/scripts/../api/par-api.json: ok

JSONLINT - All files in dir examples.
===================================
./par/scripts/../examples/br-1.json: ok
./par/scripts/../examples/br-2.json: ok
./par/scripts/../examples/br-3.json: ok
./par/scripts/../examples/fmt-43.json: ok
./par/scripts/../examples/md5check.json: ok
./par/scripts/../examples/md5prop.json: ok
./par/scripts/../examples/md5sum.json: ok

```

then run the `pytest` tests

```shell
pytest

===================== test session starts ===============================
platform linux2 -- Python 2.7.12, pytest-3.6.2, py-1.5.3, pluggy-0.6.0
rootdir: /par, inifile:
collected 7 items

testing/test_main.py .......                                                                                                                                                           [100%]

===================== 7 passed in 0.06 seconds ========================
```

## Documentation

Coming soon <https://parcore.readme.io>
