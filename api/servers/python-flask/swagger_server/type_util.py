#!/usr/bin/python3
# coding: UTF-8
#
# PAR Consortium
# Copyright (C) 2020
# All rights reserved.
#
# This code is distributed under the terms of the GNU General Public
# License, Version 3. See the text file "COPYING" for further details
# about the terms of this license.

import sys

if sys.version_info < (3, 7):
    import typing

    def is_generic(klass):
        """ Determine whether klass is a generic class """
        return type(klass) == typing.GenericMeta

    def is_dict(klass):
        """ Determine whether klass is a Dict """
        return klass.__extra__ == dict

    def is_list(klass):
        """ Determine whether klass is a List """
        return klass.__extra__ == list

else:

    def is_generic(klass):
        """ Determine whether klass is a generic class """
        return hasattr(klass, '__origin__')

    def is_dict(klass):
        """ Determine whether klass is a Dict """
        return klass.__origin__ == dict

    def is_list(klass):
        """ Determine whether klass is a List """
        return klass.__origin__ == list
