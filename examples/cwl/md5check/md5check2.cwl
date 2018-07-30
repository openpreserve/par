cwlVersion: v1.0
class: CommandLineTool
id: "md5check"
label: "Fixity check using md5sum"
baseCommand:
  - "md5sum" 
  - "-c" 
  - "manifest.md5"

requirements:
  - class: InlineJavascriptRequirement
  - class: InitialWorkDirRequirement
    listing:
      - entryname: manifest.md5
        entry: | 
          $(inputs.md5value)  $(inputs.input_file.basename)
      - $(inputs.input_file)

inputs:
  md5value: string
  input_file:    
    type: File

outputs:
  fixity_report:
    type: string
    outputBinding:
      glob: fixity_report.txt
      loadContents: true
      outputEval: |
        ${
          var toolOutput, pass;
          toolOutput = self[0].contents.split(" ");
          pass = "FAIL";
          if (toolOutput[toolOutput.length - 1] == "OK\n") {
            pass = "PASS";
          }
          return pass;
        }

stdout: fixity_report.txt
