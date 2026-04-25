# -*- coding: utf-8 -*-
'''
    feedgen.util
    ~~~~~~~~~~~~

    This file contains helper functions for the feed generator module.

    :copyright: 2013, Lars Kiesow <lkiesow@uos.de>
    :license: FreeBSD and LGPL, see license.* for more details.
'''
import locale
import sys
import lxml  # nosec - we configure a safe parser below

# Configure a safe parser which does not allow XML entity expansion
parser = lxml.etree.XMLParser(
        attribute_defaults=False,
        dtd_validation=False,
        load_dtd=False,
        no_network=True,
        recover=False,
        remove_pis=True,
        resolve_entities=False,
        huge_tree=False)


def xml_fromstring(xmlstring):
    pass


def xml_elem(name, parent=None, **kwargs):
    pass


def ensure_format(val, allowed, required, allowed_values=None, defaults=None):
    '''Takes a dictionary or a list of dictionaries and check if all keys are
    in the set of allowed keys, if all required keys are present and if the
    values of a specific key are ok.

    :param val:            Dictionaries to check.
    :param allowed:        Set of allowed keys.
    :param required:       Set of required keys.
    :param allowed_values: Dictionary with keys and sets of their allowed
                           values.
    :param defaults:       Dictionary with default values.
    :returns:              List of checked dictionaries.
    '''
    pass


def formatRFC2822(date):
    '''Make sure the locale setting do not interfere with the time format.
    '''
    pass
