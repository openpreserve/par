#!/usr/bin/python
# coding: UTF-8
#
# PAR Consortium
# Copyright (C) 2020
# All rights reserved.
#
# This code is distributed under the terms of the GNU General Public
# License, Version 3. See the text file "COPYING" for further details
# about the terms of this license.
#
"""Factory and caching for PAR type."""
from datetime import datetime
import uuid

from flask import Response

import swagger_server.models as MODEL
from swagger_server.forge.const import WD_ENT_PRFX, WD_MAIN_NS, WD_ST_PRFX
import swagger_server.forge.queries as QUERY

def par_id(namespace, name):
    """
    Create a ParIdentifier from a namespace and name.

    Uses the Python uuid library to generate consistent GUIDs
    """
    guid = uuid.uuid5(uuid.NAMESPACE_URL, '{}/{}'.format(namespace, name))
    return MODEL.ParIdentifier(guid=str(guid), namespace=namespace, name=name)

def _pop_format_families():
    results_json = QUERY.get_format_families()
    ret_dict = {
        par_id(WD_MAIN_NS, family['id']['value'].replace(WD_ENT_PRFX, '')).name:MODEL.FormatFamily(
                   id=par_id(WD_MAIN_NS, family['id']['value'].replace(WD_ENT_PRFX, '')),
                   family_type=family['formatFamilyLabel']['value'],
                   file_formats=[
                       par_id(WD_MAIN_NS, format)
                       for format in family['file_formats']['value'].replace(WD_ENT_PRFX,
                                                                             '').split('|')
                     ] if family['file_formats']['value'] else [])
               for family in results_json['results']['bindings']}
    return ret_dict

FORMAT_FAMILIES = _pop_format_families()

def get_format_families():
    """Return the full list of all font families."""
    return list(FORMAT_FAMILIES.values())

def get_format_family(name):
    """Return a font family by GUID or None if no match."""
    return FORMAT_FAMILIES.get(name, None)

def identifiers(piped_mime_types, piped_puids):
    """
    Return a list of PAR IdentifierInformation for MIME and PUID ids
    """
    mime_ids = [MODEL.IdentifierInformation(mime, 'MIME')
        for mime in piped_mime_types.split('|')] if piped_mime_types else []
    ids = mime_ids + ([MODEL.IdentifierInformation(puid, "PUID")
        for puid in piped_puids.split('|')] if piped_puids else [])
    return ids if ids else None

def ext_sigs_extensions(piped_extensions):
    """
    Returns a list of ExternalSignatureInformation instances for the
    pipe separated string of file extensions passed as a parameter.
    """
    return [
        MODEL.ExternalSignatureInformation(signature=ext, signature_type='File Extension')
        for ext in piped_extensions.split('|')
    ] if piped_extensions else None

def _pop_formats():
    """Query Wikidata for formats and returns a list of FileFormat instances."""
    sig_lookup = _signatures()
    results_json = QUERY.get_formats()
    results = {
        par_id(WD_MAIN_NS,
               format['format']['value'].replace(WD_ENT_PRFX, '')).name:MODEL.FileFormat(
                  id=par_id(WD_MAIN_NS,
                            format['format']['value'].replace(WD_ENT_PRFX, '')),
                  name=format['name']['value'],
                  description=format['description']['value']
                      if 'description' in format else '',
                  developers=[
                    MODEL.DeveloperInformation(developer_id=format['developer']['value'],
                                               developer_id_namespace=WD_MAIN_NS,
                                               developer_name=format['developerLabel']['value'])
                  ] if 'developer' in format else None,
                  aliases=format['aliases']['value'].split('|')
                      if format['aliases']['value'] else None,
                  external_signatures=ext_sigs_extensions(format['file_extensions']['value']),
                  identifiers=identifiers(format['mime_types']['value']
                                            if format['mime_types']['value'] else None,
                                          format['pronom_ids']['value']
                                            if format['pronom_ids']['value'] else None),
                  internal_signatures=
                    sig_lookup.get(format['format']['value'].replace(WD_ENT_PRFX, ''),
                                   None),
                  local_last_modified_date=format['date_modified']['value'])
               for format in results_json['results']['bindings']}
    filtered_results = { k: v for k, v in results.items() if not k in FORMAT_FAMILIES }
    return filtered_results

def _bs(sig):
    return [
        MODEL.ByteSequenceInformation(
            byte_sequence_id=sig['signatureId']['value'].replace(WD_ST_PRFX, ''),
            byte_sequence_id_namespace=WD_MAIN_NS,
            byte_sequence_value=sig['signature']['value'],
            offset=sig['offsetLabel']['value'],
            position_type=sig['position_typeLabel']['value']
        )
    ]

def _signatures():
    """
        Cache for format sigs.
    """
    results_json = QUERY.get_signatures()
    sigs = {}
    for sig in results_json['results']['bindings']:
        key = sig['item']['value'].replace(WD_ENT_PRFX, '')
        byte_sequences = _bs(sig)
        int_sig = [
            MODEL.InternalSignatureInformation(
                signature_id=sig['signatureId']['value'],
                signature_id_namespace=WD_MAIN_NS,
                byte_sequences=byte_sequences
            )
        ]
        vals = sigs[ key ] + int_sig if key in sigs else int_sig
        sigs[key] = vals
    return sigs

FORMATS=_pop_formats()

def get_formats():
    """Return the full list of all fonts."""
    return list(FORMATS.values())

def get_format(name):
    """Return a font by id.name or None if no match."""
    return FORMATS.get(name, None)

def slice_list(to_slice, limit=None, offset=None):
    """Returns a slice list from the passed params accounting for None values."""
    if not limit and not offset:
        return to_slice
    if not offset:
        return to_slice[:limit+1]
    if not limit:
        return to_slice[offset:]
    return to_slice[offset:limit+offset]

def filter_by_guids(to_filter, guids):
    """Given a list, to_filter, of elements with property id.guid, this returns
    a list filtered where only items with id.guid contained in the filtered list."""
    return list(filter(lambda element: element.id.guid in guids, to_filter))

def filter_by_date_modified(to_filter, before=None, after=None):
    """Given a list, to_filter, of elements with property localLastModifiedDate, this returns
    a list filtered where only items with localLastModifiedDate before before and
    after after are contained in the filtered list."""
    if before:
        before_date = datetime.fromisoformat(before)
        to_filter = list(filter(lambda element:
                                    datetime.fromisoformat(element.local_last_modified_date[:-1]) <
                                                           before_date, to_filter))
    if after:
        after_date = datetime.fromisoformat(after)
        to_filter = list(filter(lambda element:
                                    datetime.fromisoformat(element.local_last_modified_date[:-1]) >
                                                           after_date, to_filter))
    return to_filter

def method_not_allowed():
    """Returns a method not allowed response with appropriate allow header."""
    response = Response(status=405)
    response.headers['Allow'] = "GET"
    return response
