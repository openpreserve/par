# MD5 Check Examples

These CWL files provide several examples of how to run md5sum for fixity checking of a file.

## md5check1.cwl 
This is a basic CWL wrapper around md5sum.  

Inputs:

* file to be checked (testfile.txt)
* manifest file (manifest.md5) containing the MD5 checksum for testfile.txt

Outputs:

* file containing the stdout from md5sum (fixity_report.txt)


## md5check2.cwl
This is a wrapper around md5sum that writes the input manifest file and also parses the output stdout to determine if the fixity check passed or failed.

Inputs:

* file to be checked (testfile.txt)
* MD5 checksum for testfile.txt

Outputs:

* PASS/FAIL for the file

## md5checkDocker.cwl

Same as md5check1.cwl but runs md5sum in a docker container.
