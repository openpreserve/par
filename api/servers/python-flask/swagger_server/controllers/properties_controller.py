import connexion
import six

from swagger_server.models.par_properties import ParProperties  # noqa: E501
from swagger_server.models.par_property import ParProperty  # noqa: E501
from swagger_server import util


def properties_get(guid=None, modified_after=None, modified_before=None, offset=None, limit=None):  # noqa: E501
    """Get Properties

    Returns an array of Properties that match all of the filter conditions supplied. Any number of filters can be used together. The date filters should be supplied as ISO-8601 date times or dates, i.e. yyyy-MM-ddThh:mm:ss.SZ or yyyy-MM-dd. If no time information is supplied, then 00:00:00 in UTC will be assumed. This means that if you supply modified-after and modified-before dates of 2019-01-01 and 2019-12-31, you will not match any Properties modified during the day of 31st December. # noqa: E501

    :param guid: A comma separated list of GUIDs of Properties. This filter matches only those Properties that are identified by one of the listed GUIDs.
    :type guid: str
    :param modified_after: This filter matches only those Properties whose local last modified date is after the specified date.
    :type modified_after: str
    :param modified_before: This filter matches only those Properties whose local last modified date is before the specified date.
    :type modified_before: str
    :param offset: Used for requesting paged responses, this defines the offset of the first Property to return from the start of the list of all matching Properties.
    :type offset: int
    :param limit: Used for requesting paged responses, this defines the maximum number of Properties to return.
    :type limit: int

    :rtype: ParProperties
    """
    return 'do some magic!'


def properties_guid_delete(guid, Authorization):  # noqa: E501
    """Delete Property

    Deletes the Property specified by the GUID of the PAR Identifier # noqa: E501

    :param guid: 
    :type guid: str
    :param Authorization: HTTP Basic Auth header
    :type Authorization: str

    :rtype: ParProperty
    """
    return 'do some magic!'


def properties_guid_get(guid):  # noqa: E501
    """Get a Property

    Returns the Property specified by the GUID of the PAR Identifier # noqa: E501

    :param guid: 
    :type guid: str

    :rtype: ParProperty
    """
    return 'do some magic!'


def properties_guid_put(guid, Authorization, body=None):  # noqa: E501
    """Update Property

    Updates the Property specified by the GUID of the PAR Identifier and returns the property as updated. # noqa: E501

    :param guid: 
    :type guid: str
    :param Authorization: HTTP Basic Auth header
    :type Authorization: str
    :param body: Serialised entity in request body
    :type body: dict | bytes

    :rtype: ParProperty
    """
    if connexion.request.is_json:
        body = ParProperty.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'


def properties_post(Authorization, body=None):  # noqa: E501
    """Create Property

    Creates a new Property and returns the property as created. # noqa: E501

    :param Authorization: HTTP Basic Auth header
    :type Authorization: str
    :param body: Serialised entity in request body
    :type body: dict | bytes

    :rtype: ParProperty
    """
    if connexion.request.is_json:
        body = ParProperty.from_dict(connexion.request.get_json())  # noqa: E501
    return 'do some magic!'
