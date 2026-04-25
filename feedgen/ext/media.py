# -*- coding: utf-8 -*-
'''
    feedgen.ext.media
    ~~~~~~~~~~~~~~~~~

    Extends the feedgen to produce media tags.

    :copyright: 2013-2017, Lars Kiesow <lkiesow@uos.de>

    :license: FreeBSD and LGPL, see license.* for more details.
'''

from feedgen.ext.base import BaseEntryExtension, BaseExtension
from feedgen.util import ensure_format, xml_elem

MEDIA_NS = 'http://search.yahoo.com/mrss/'


class MediaExtension(BaseExtension):
    '''FeedGenerator extension for torrent feeds.
    '''

    def extend_ns(self):
        pass


class MediaEntryExtension(BaseEntryExtension):
    '''FeedEntry extension for media tags.
    '''

    def __init__(self):
        self.__media_content = []
        self.__media_thumbnail = []

    def extend_atom(self, entry):
        '''Add additional fields to an RSS item.

        :param feed: The RSS item XML element to use.
        '''

        pass

    def extend_rss(self, item):
        pass

    def content(self, content=None, replace=False, group='default', **kwargs):
        '''Get or set media:content data.

        This method can be called with:
        - the fields of a media:content as keyword arguments
        - the fields of a media:content as a dictionary
        - a list of dictionaries containing the media:content fields

        <media:content> is a sub-element of either <item> or <media:group>.
        Media objects that are not the same content should not be included in
        the same <media:group> element. The sequence of these items implies
        the order of presentation. While many of the attributes appear to be
        audio/video specific, this element can be used to publish any type
        of media. It contains 14 attributes, most of which are optional.

        media:content has the following fields:
        - *url* should specify the direct URL to the media object.
        - *fileSize* number of bytes of the media object.
        - *type* standard MIME type of the object.
        - *medium* type of object (image | audio | video | document |
          executable).
        - *isDefault* determines if this is the default object.
        - *expression* determines if the object is a sample or the full version
          of the object, or even if it is a continuous stream (sample | full |
          nonstop).
        - *bitrate* kilobits per second rate of media.
        - *framerate* number of frames per second for the media object.
        - *samplingrate* number of samples per second taken to create the media
          object. It is expressed in thousands of samples per second (kHz).
        - *channels* number of audio channels in the media object.
        - *duration* number of seconds the media object plays.
        - *height* height of the media object.
        - *width* width of the media object.
        - *lang* is the primary language encapsulated in the media object.

        :param content: Dictionary or list of dictionaries with content data.
        :param replace: Add or replace old data.
        :param group: Media group to put this content in.

        :returns: The media content tag.
        '''
        # Handle kwargs
        pass

    def thumbnail(self, thumbnail=None, replace=False, group='default',
                  **kwargs):
        '''Get or set media:thumbnail data.

        This method can be called with:
        - the fields of a media:content as keyword arguments
        - the fields of a media:content as a dictionary
        - a list of dictionaries containing the media:content fields

        Allows particular images to be used as representative images for
        the media object. If multiple thumbnails are included, and time
        coding is not at play, it is assumed that the images are in order
        of importance. It has one required attribute and three optional
        attributes.

        media:thumbnail has the following fields:
        - *url* should specify the direct URL to the media object.
        - *height* height of the media object.
        - *width* width of the media object.
        - *time* specifies the time offset in relation to the media object.

        :param thumbnail: Dictionary or list of dictionaries with thumbnail
                          data.
        :param replace: Add or replace old data.
        :param group: Media group to put this content in.

        :returns: The media thumbnail tag.
        '''
        pass
