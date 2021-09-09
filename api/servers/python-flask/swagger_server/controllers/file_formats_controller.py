from swagger_server.models.file_format import FileFormat  # noqa: E501
# from swagger_server.models.file_formats import FileFormats  # noqa: E501
import pprint
from wikidp.models import FileFormat as WikiFormat
import swagger_server.models.factory as FACT

def file_formats_get(guid=None, modified_after=None, modified_before=None, offset=None, limit=None):  # noqa: E501
    """Get File Formats

    Returns an array of File Formats that match all of the filter conditions supplied. Any number of filters can be used together. The date filters should be supplied as ISO-8601 date times or dates, i.e. yyyy-MM-ddThh:mm:ss.SZ or yyyy-MM-dd. If no time information is supplied, then 00:00:00 in UTC will be assumed. This means that if you supply modified-after and modified-before dates of 2019-01-01 and 2019-12-31, you will not match any FileFormats modified during the day of 31st December. # noqa: E501

    :param guid: A comma separated list of GUIDs of FileFormats. This filter matches only those File Formats that are identified by one of the listed GUIDs.
    :type guid: str
    :param modified_after: This filter matches only those File Formats whose local last modified date is after the specified date.
    :type modified_after: str
    :param modified_before: This filter matches only those File Formats whose local last modified date is before the specified date.
    :type modified_before: str
    :param offset: Used for requesting paged responses, this defines the offset of the first FileFormat to return from the start of the list of all matching File Formats.
    :type offset: int
    :param limit: Used for requesting paged responses, this defines the maximum number of FileFormats to return.
    :type limit: int

    :rtype: FileFormats
    """
    formats = WikiFormat.list_formats()
    pprint.pprint("got formats")
    par_formats = []
    for format in formats:
        pprint.pprint(str(format))
        par_id = FACT.par_id("http://wikidata.org", format.qid)
        par_format = FileFormat(id=par_id, name=format.name, aliases=format.aliases)
        par_formats.append(par_format)
    return par_formats


def file_formats_guid_get(guid):  # noqa: E501
    """Get a File Format

    Returns the File Format specified by the GUID of the PAR Identifier # noqa: E501

    :param guid:
    :type guid: str

    :rtype: FileFormat
    """
    return 'do some magic!'
