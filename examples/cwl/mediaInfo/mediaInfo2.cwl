cwlVersion: v1.0
class: CommandLineTool
id: "mediaInfo2"
label: "AV property extraction using mediainfo"
baseCommand: mediainfo
 

requirements:
  - class: InlineJavascriptRequirement
  - class: InitialWorkDirRequirement
    listing:
      - $(inputs.input_file)

inputs:
  input_file:    
    type: File
    inputBinding: 
      position: 1

arguments:
  - "--Output=EBUCore"

outputs: 
  bitrate:
    type: string
    outputBinding:
      glob: mediainfo_report.txt
      loadContents: true
      outputEval: |
        ${
          var tag = "ebucore:bitRate";
          var value, XML;  
          var startTag, endTag;
          var start, end;
          XML = self[0].contents;
          startTag = "<"+tag+">";
          endTag = "</"+tag+">";
          start = XML.search(startTag) + startTag.length;
          end = XML.search(endTag);
          value = XML.slice(start,end);
          return value;
        }
  width:
    type: string
    outputBinding:
      glob: mediainfo_report.txt
      loadContents: true
      outputEval: |
        ${
          var startTag = "<"+"ebucore:width unit=\"pixel\""+">";
          var endTag = "</"+"ebucore:width"+">";
          var value, XML;  
          var startTag, endTag;
          var start, end;
          XML = self[0].contents;
          start = XML.search(startTag) + startTag.length;
          end = XML.search(endTag);
          value = XML.slice(start,end);
          return value;
        }
  height:
    type: string
    outputBinding:
      glob: mediainfo_report.txt
      loadContents: true
      outputEval: |
        ${
          var startTag = "<"+"ebucore:height unit=\"pixel\""+">";
          var endTag = "</"+"ebucore:height"+">";
          var value, XML;  
          var startTag, endTag;
          var start, end;
          XML = self[0].contents;
          start = XML.search(startTag) + startTag.length;
          end = XML.search(endTag);
          value = XML.slice(start,end);
          return value;
        } 
      
stdout: mediainfo_report.txt
