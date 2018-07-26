cwlVersion: v1.0
class: CommandLineTool
id: "md5check"
label: "Fixity check using md5sum"
baseCommand: md5sum

hints:
  DockerRequirement:
    dockerPull: ubuntu:16.04

requirements:
  InitialWorkDirRequirement:
    listing:
      - $(inputs.input_file)

inputs:
  manifest_file:    
    type: File
    inputBinding:
      prefix: -c
      separate: true
      position: 1 
  input_file:    
    type: File
    
outputs: 
  fixity_report:
    type: stdout
stdout: fixity_report.txt
