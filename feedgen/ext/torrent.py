# -*- coding: utf-8 -*-
'''
    feedgen.ext.torrent
    ~~~~~~~~~~~~~~~~~~~

    Extends the FeedGenerator to produce torrent feeds.

    :copyright: 2016, Raspbeguy <raspbeguy@hashtagueule.fr>

    :license: FreeBSD and LGPL, see license.* for more details.
'''

from feedgen.ext.base import BaseEntryExtension, BaseExtension
from feedgen.util import xml_elem

TORRENT_NS = 'http://xmlns.ezrss.it/0.1/dtd/'


class TorrentExtension(BaseExtension):
    '''FeedGenerator extension for torrent feeds.
    '''
    def extend_ns(self):
        pass


class TorrentEntryExtension(BaseEntryExtension):
    '''FeedEntry extension for torrent feeds
    '''
    def __init__(self):
        self.__torrent_filename = None
        self.__torrent_infohash = None
        self.__torrent_contentlength = None
        self.__torrent_seeds = None
        self.__torrent_peers = None
        self.__torrent_verified = None

    def extend_rss(self, entry):
        '''Add additional fields to an RSS item.

        :param feed: The RSS item XML element to use.
        '''
        pass

    def filename(self, torrent_filename=None):
        '''Get or set the name of the torrent file.

        :param torrent_filename: The name of the torrent file.
        :returns: The name of the torrent file.
        '''
        pass

    def infohash(self, torrent_infohash=None):
        '''Get or set the hash of the target file.

        :param torrent_infohash: The target file hash.
        :returns: The target hash file.
        '''
        pass

    def contentlength(self, torrent_contentlength=None):
        '''Get or set the size of the target file.

        :param torrent_contentlength: The target file size.
        :returns: The target file size.
        '''
        pass

    def seeds(self, torrent_seeds=None):
        '''Get or set the number of seeds.

        :param torrent_seeds: The seeds number.
        :returns: The seeds number.
        '''
        pass

    def peers(self, torrent_peers=None):
        '''Get or set the number od peers

        :param torrent_infohash: The peers number.
        :returns: The peers number.
        '''
        pass

    def verified(self, torrent_verified=None):
        '''Get or set the number of verified peers.

        :param torrent_infohash: The verified peers number.
        :returns: The verified peers number.
        '''
        pass
