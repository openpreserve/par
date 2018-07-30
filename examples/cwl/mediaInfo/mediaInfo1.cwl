cwlVersion: v1.0
class: CommandLineTool
id: "mediaInfo1"
label: "AV property extraction using mediainfo"
baseCommand: mediainfo
 

requirements:
  InitialWorkDirRequirement:
    listing:
      - $(inputs.input_file)

inputs:
  input_file:    
    type: File
    inputBinding: 
      position: 1
    
outputs: 
  mediainfo_report:
    type: stdout

arguments:
  - "--Output=EBUCore"

stdout: mediainfo_report.txt
