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
"""
All constants for forge methods, wikidata queries and namespaces, etc.
"""
WD_ROOT_URL = 'http://www.wikidata.org/'
WD_ENT_PRFX = WD_ROOT_URL + 'entity/'
WD_ST_PRFX = WD_ENT_PRFX + 'statement/'
WD_SPARQL = "https://query.wikidata.org/sparql"
WD_MAIN_NS = WD_ROOT_URL + 'wiki/'
WD_NS = {
    'main': WD_MAIN_NS,
    'prop': WD_MAIN_NS + 'Property:'
}
