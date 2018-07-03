#!/usr/bin/env python
# coding=UTF-8
#
# JISC RDSS-PAR
#
#
#
"""Constants used across test modules"""
import os

TESTS_DIR = os.path.dirname(os.path.abspath(__file__))
SCHEMA_DIR = os.path.abspath(os.path.join(TESTS_DIR, os.pardir, "schemas"))

def get_schema_path(json_file_name):
    """Returns the full JSON schema path for the passed file name."""
    return os.path.join(SCHEMA_DIR, json_file_name)
