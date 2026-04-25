# -*- coding: utf-8 -*-
#
# Copyright 2015 Kenichi Sato <ksato9700@gmail.com>
#

'''
Extends FeedGenerator to support Syndication module

See below for details
http://web.resource.org/rss/1.0/modules/syndication/
'''

from feedgen.ext.base import BaseExtension
from feedgen.util import xml_elem

SYNDICATION_NS = 'http://purl.org/rss/1.0/modules/syndication/'
PERIOD_TYPE = ('hourly', 'daily', 'weekly', 'monthly', 'yearly')


def _set_value(channel, name, value):
    pass


class SyndicationExtension(BaseExtension):
    def __init__(self):
        self._update_period = None
        self._update_freq = None
        self._update_base = None

    def extend_ns(self):
        pass

    def extend_rss(self, rss_feed):
        pass

    def update_period(self, value):
        pass

    def update_frequency(self, value):
        pass

    def update_base(self, value):
        # the value should be in W3CDTF format
        pass


class SyndicationEntryExtension(BaseExtension):
    pass
