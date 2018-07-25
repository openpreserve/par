# MediaInfo CWL Examples

The CWL examples run [MediaInfo](https://mediaarea.net/en/MediaInfo).  You will need this installed on your system.

To run the mediainfo examples you will also need a test video file.  The examples were tested using a short [NASA video on lunar eclipses](http://www.nasa.gov/downloadable/videos/sciencecasts-_total_eclipse_of_the_moon.mp4).  Download the file and rename it to lunar_eclipse.mp4

### mediaInfo1.cwl

This example runs MediaInfo on a video file and records the output to a file.  MediaInfo uses the --Output=EBUCore setting to produce [EBUCore](https://www.ebu.ch/metadata/ontologies/ebucore/index.html) XML that follows the EBUCore schema.

### mediaInfo2.cwl

This example runs MediaInfo on a video file but unlike MediaInfo1.cwl it parses the output and extracts some specific properties (height, width, bitrate).

The CWL wrapper around MediaInfo uses CWL's JavaScript support to parse the output.  The CWL reference implementation [cwltool](https://github.com/common-workflow-language/cwltool) uses the [Nodejs](https://nodejs.org/) JavaScript engine.  Using libraries that are not part of the core Nodejs software, e.g. through 'requires' statements is not supported in CWL.  Therefore, when parsing the EBUCore XML from MediaInfo, libraries such as [xmldom](https://www.npmjs.com/package/xmldom) are not available.  Instead, the JavaScript in the CWL examples extracts the values of XML elements by using simple string matching.  This is not a robust approach and is intended purely as an example of how CWL can be used to parse tool output and return specific properties.

