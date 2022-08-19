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
# pip install sparqlwrapper
# https://rdflib.github.io/sparqlwrapper/
"""Wikidata SPARQL queries and the like."""
import sys
from SPARQLWrapper import SPARQLWrapper, JSON
from swagger_server.forge.const import WD_SPARQL

USER_AGENT='Wikidata PAR Endpoint/%s.%s' % (sys.version_info[0], sys.version_info[1])


FORMAT_FAMILY_QUERY = """SELECT DISTINCT (?formatFamily AS ?id)
?formatFamilyLabel ?date_modified ?parentClass
(GROUP_CONCAT(DISTINCT ?part; SEPARATOR = "|") AS ?file_formats )
WHERE {
  { ?formatFamily (wdt:P31/(wdt:P279*)) wd:Q26085352. }
  { ?formatFamily schema:dateModified ?date_modified. }
  OPTIONAL { ?formatFamily wdt:P527 ?part. }
   SERVICE wikibase:label {
     bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en,fr,be,bn,ca,cs,da,de,en,es,fi,hu,it,nl,eo,pl,pt,ro,ru,sk,sv,sw,uk".
   }
} GROUP BY ?formatFamily ?formatFamilyLabel ?date_modified ?parentClass
"""

def get_format_families():
    """Return the JSON format family query results."""
    return _get_results(FORMAT_FAMILY_QUERY)


FORMAT_QUERY = """SELECT DISTINCT ?format
(GROUP_CONCAT(DISTINCT ?instance_types_item; SEPARATOR = "|") AS ?types)
(GROUP_CONCAT(DISTINCT ?file_extensions_item; SEPARATOR = "|") AS ?file_extensions)
(GROUP_CONCAT(DISTINCT ?media_types_item; SEPARATOR = "|") AS ?mime_types)
(GROUP_CONCAT(DISTINCT ?pronom_ids_item; SEPARATOR = "|") AS ?pronom_ids)
(?formatLabel AS ?name)
(?formatDescription AS ?description)
?developer
?developerLabel
?date_modified
(GROUP_CONCAT(DISTINCT ?format_alt_label; SEPARATOR = "|") AS ?aliases)
WHERE {
  {
    SELECT DISTINCT ?format ?instance_types_item ?file_extensions_item ?media_types_item ?pronom_ids_item ?internal_sigs_item ?developer ?date_modified WHERE {
      { ?format wdt:P31/wdt:P279* wd:Q235557. }
      { ?format schema:dateModified ?date_modified.  }
      OPTIONAL { ?format wdt:P31 ?instance_types_item. }
      OPTIONAL { ?format wdt:P1195 ?file_extensions_item. }
      OPTIONAL { ?format wdt:P1163 ?media_types_item. }
      OPTIONAL { ?format wdt:P2748 ?pronom_ids_item. }
    }
    ORDER BY (?format)
  }
  OPTIONAL {
    ?format skos:altLabel ?format_alt_label.
    FILTER((LANG(?format_alt_label)) = "en")
  }
  OPTIONAL {
    ?format wdt:P178 ?developer.
  }
  SERVICE wikibase:label {
    bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en,fr,be,ca,cs,da,de,es,fi,hu,it,nl,pt,sw,uk".
    ?format rdfs:label ?formatLabel.
    ?developer rdfs:label ?developerLabel;
      schema:description ?formatDescription.
  }
}
GROUP BY ?format ?formatLabel ?formatDescription ?developer ?developerLabel ?date_modified"""

def get_formats():
    """Return the JSON format query results."""
    return _get_results(FORMAT_QUERY)


SIG_QUERY = """SELECT ?item ?signatureId ?signature ?encodingLabel
?offsetLabel ?position_typeLabel
WHERE {
  ?item (wdt:P31/(wdt:P279*)) wd:Q235557;
    p:P4152 ?signatureId.
  ?signatureId ps:P4152 ?signature;
    pq:P3294 ?encoding;
    pq:P4153 ?offset;
    pq:P2210 ?position_type.
  SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
}"""

def get_signatures():
    """Return the JSON sig query results."""
    return _get_results(SIG_QUERY)

def _get_results(query):
    sparql = SPARQLWrapper(WD_SPARQL, agent=USER_AGENT)
    sparql.setQuery(query)
    sparql.setReturnFormat(JSON)
    return sparql.query().convert()
