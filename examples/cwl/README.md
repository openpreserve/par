# Common Workflow Language Examples

The examples in the cwl directory are written in [Common Workflow Language] (https://github.com/common-workflow-language/common-workflow-language)

To run the Common Workflow Language (CWL) examples you will need a cwl-runner.  The examples have been tested using the [reference implementation] (https://github.com/common-workflow-language/cwltool)

The CWL spec for running command line tools is [here](https://www.commonwl.org/v1.0/CommandLineTool.html) and there is a simple user guide to CWL [here](http://www.commonwl.org/user_guide/)

The CWL can be run like this:

```
cwltool md5check.cwl md5check.yml
```

The .cwl file contains the CWL definition of how to run the tool.
The .yml file contains the input parameters.

The examples in the cwl directory include input and output files where appropriate.  For example, the md5check directory includes testfile.txt, which is a small text file to verify, and manifest.md5, which contains a MD5 checksum to verify testfile.txt against.

For the CWL to execute successfully you will need the relevant tool installed locally, e.g. md5sum.

Some of the examples include a docker version. For example, md5checkDocker will automatically download and use a ubuntu:16.04 container that has md5sum already installed.  You will need to install docker first.  CWL takes care of the plumbing so that command line inputs are passed into the container and command line outputs are extracted and saved to the host file system.
