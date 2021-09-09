# coding: utf-8

import uuid

from swagger_server.models.par_identifier import ParIdentifier

def par_id(namespace, name):
    """
    Create a ParIdentifier from a namespace and name.

    Uses the Python uuid library to generate consistent GUIDs
    """
    guid = uuid.uuid5(uuid.NAMESPACE_URL, '{}/{}'.format(namespace, name))
    return ParIdentifier(guid=guid, namespace=namespace, name=name)
