# -*- coding: utf-8 -*-
'''
    feedgen.ext.podcast
    ~~~~~~~~~~~~~~~~~~~

    Extends the FeedGenerator to produce podcasts.

    :copyright: 2013, Lars Kiesow <lkiesow@uos.de>

    :license: FreeBSD and LGPL, see license.* for more details.
'''

from feedgen.compat import string_types
from feedgen.ext.base import BaseExtension
from feedgen.util import ensure_format, xml_elem


class PodcastExtension(BaseExtension):
    '''FeedGenerator extension for podcasts.
    '''

    def __init__(self):
        # ITunes tags
        # http://www.apple.com/itunes/podcasts/specs.html#rss
        self.__itunes_author = None
        self.__itunes_block = None
        self.__itunes_category = None
        self.__itunes_image = None
        self.__itunes_explicit = None
        self.__itunes_complete = None
        self.__itunes_new_feed_url = None
        self.__itunes_owner = None
        self.__itunes_subtitle = None
        self.__itunes_summary = None
        self.__itunes_type = None

    def extend_ns(self):
        pass

    def extend_rss(self, rss_feed):
        '''Extend an RSS feed root with set itunes fields.

        :returns: The feed root element.
        '''
        pass

    def itunes_author(self, itunes_author=None):
        '''Get or set the itunes:author. The content of this tag is shown in
        the Artist column in iTunes. If the tag is not present, iTunes uses the
        contents of the <author> tag. If <itunes:author> is not present at the
        feed level, iTunes will use the contents of <managingEditor>.

        :param itunes_author: The author of the podcast.
        :returns: The author of the podcast.
        '''
        pass

    def itunes_block(self, itunes_block=None):
        '''Get or set the ITunes block attribute. Use this to prevent the
        entire podcast from appearing in the iTunes podcast directory.

        :param itunes_block: Block the podcast.
        :returns: If the podcast is blocked.
        '''
        pass

    def itunes_category(self, itunes_category=None, replace=False, **kwargs):
        '''Get or set the ITunes category which appears in the category column
        and in iTunes Store Browser.

        The (sub-)category has to be one from the values defined at
        http://www.apple.com/itunes/podcasts/specs.html#categories

        This method can be called with:

        - the fields of an itunes_category as keyword arguments
        - the fields of an itunes_category as a dictionary
        - a list of dictionaries containing the itunes_category fields

        An itunes_category has the following fields:

        - *cat* name for a category.
        - *sub* name for a subcategory, child of category

        If a podcast has more than one subcategory from the same category, the
        category is called more than once.

        Likei the parameter::

            [{"cat":"Arts","sub":"Design"},{"cat":"Arts","sub":"Food"}]

        …would become::

            <itunes:category text="Arts">
                <itunes:category text="Design"/>
                <itunes:category text="Food"/>
            </itunes:category>


        :param itunes_category: Dictionary or list of dictionaries with
                                itunes_category data.
        :param replace: Add or replace old data.
        :returns: List of itunes_categories as dictionaries.

        ---

        **Important note about deprecated parameter syntax:** Old version of
        the feedgen did only support one category plus one subcategory which
        would be passed to this ducntion as first two parameters. For
        compatibility reasons, this still works but should not be used any may
        be removed at any time.
        '''
        # Ensure old API still works for now. Note that the API is deprecated
        # and this fallback may be removed at any time.
        pass

    def itunes_image(self, itunes_image=None):
        '''Get or set the image for the podcast. This tag specifies the artwork
        for your podcast. Put the URL to the image in the href attribute.
        iTunes prefers square .jpg images that are at least 1400x1400 pixels,
        which is different from what is specified for the standard RSS image
        tag. In order for a podcast to be eligible for an iTunes Store feature,
        the accompanying image must be at least 1400x1400 pixels.

        iTunes supports images in JPEG and PNG formats with an RGB color space
        (CMYK is not supported). The URL must end in ".jpg" or ".png". If the
        <itunes:image> tag is not present, iTunes will use the contents of the
        RSS image tag.

        If you change your podcast’s image, also change the file’s name. iTunes
        may not change the image if it checks your feed and the image URL is
        the same. The server hosting your cover art image must allow HTTP head
        requests for iTS to be able to automatically update your cover art.

        :param itunes_image: Image of the podcast.
        :returns: Image of the podcast.
        '''
        pass

    def itunes_explicit(self, itunes_explicit=None):
        '''Get or the the itunes:explicit value of the podcast. This tag should
        be used to indicate whether your podcast contains explicit material.
        The three values for this tag are "yes", "no", and "clean".

        If you populate this tag with "yes", an "explicit" parental advisory
        graphic will appear next to your podcast artwork on the iTunes Store
        and in the Name column in iTunes. If the value is "clean", the parental
        advisory type is considered Clean, meaning that no explicit language or
        adult content is included anywhere in the episodes, and a "clean"
        graphic will appear. If the explicit tag is present and has any other
        value (e.g., "no"), you see no indicator — blank is the default
        advisory type.

        :param itunes_explicit: If the podcast contains explicit material.
        :returns: If the podcast contains explicit material.
        '''
        pass

    def itunes_complete(self, itunes_complete=None):
        '''Get or set the itunes:complete value of the podcast. This tag can be
        used to indicate the completion of a podcast.

        If you populate this tag with "yes", you are indicating that no more
        episodes will be added to the podcast. If the <itunes:complete> tag is
        present and has any other value (e.g. “no”), it will have no effect on
        the podcast.

        :param itunes_complete: If the podcast is complete.
        :returns: If the podcast is complete.
        '''
        pass

    def itunes_new_feed_url(self, itunes_new_feed_url=None):
        '''Get or set the new-feed-url property of the podcast. This tag allows
        you to change the URL where the podcast feed is located

        After adding the tag to your old feed, you should maintain the old feed
        for 48 hours before retiring it. At that point, iTunes will have
        updated the directory with the new feed URL.

        :param itunes_new_feed_url: New feed URL.
        :returns: New feed URL.
        '''
        pass

    def itunes_owner(self, name=None, email=None):
        '''Get or set the itunes:owner of the podcast. This tag contains
        information that will be used to contact the owner of the podcast for
        communication specifically about the podcast. It will not be publicly
        displayed.

        :param itunes_owner: The owner of the feed.
        :returns: Data of the owner of the feed.
        '''
        pass

    def itunes_subtitle(self, itunes_subtitle=None):
        '''Get or set the itunes:subtitle value for the podcast. The contents
        of this tag are shown in the Description column in iTunes. The subtitle
        displays best if it is only a few words long.

        :param itunes_subtitle: Subtitle of the podcast.
        :returns: Subtitle of the podcast.
        '''
        pass

    def itunes_summary(self, itunes_summary=None):
        '''Get or set the itunes:summary value for the podcast. The contents of
        this tag are shown in a separate window that appears when the "circled
        i" in the Description column is clicked. It also appears on the iTunes
        page for your podcast. This field can be up to 4000 characters. If
        `<itunes:summary>` is not included, the contents of the <description>
        tag are used.

        :param itunes_summary: Summary of the podcast.
        :returns: Summary of the podcast.
        '''
        pass

    def itunes_type(self, itunes_type=None):
        '''Get or set the itunes:type value of the podcast. This tag should
        be used to indicate the type of your podcast.
        The two values for this tag are "episodic" and "serial".

        If your show is Serial you must use this tag.

        Specify episodic when episodes are intended to be consumed without any
        specific order. Apple Podcasts will present newest episodes first and
        display the publish date (required) of each episode. If organized into
        seasons, the newest season will be presented first - otherwise,
        episodes will be grouped by year published, newest first.

         Specify serial when episodes are intended to be consumed in sequential
         order. Apple Podcasts will present the oldest episodes first and
         display the episode numbers (required) of each episode. If organized
         into seasons, the newest season will be presented first and
         <itunes:episode> numbers must be given for each episode.

        :param itunes_type: The type of the podcast
        :returns: type of the pdocast.
        '''
        pass

    _itunes_categories = {
            'Arts': [
                'Design', 'Fashion & Beauty', 'Food', 'Literature',
                'Performing Arts', 'Visual Arts'],
            'Business': [
                'Business News', 'Careers', 'Investing',
                'Management & Marketing', 'Shopping'],
            'Comedy': [],
            'Education': [
                'Education', 'Education Technology', 'Higher Education',
                'K-12', 'Language Courses', 'Training'],
            'Games & Hobbies': [
                'Automotive', 'Aviation', 'Hobbies', 'Other Games',
                'Video Games'],
            'Government & Organizations': [
                'Local', 'National', 'Non-Profit', 'Regional'],
            'Health': [
                'Alternative Health', 'Fitness & Nutrition', 'Self-Help',
                'Sexuality'],
            'Kids & Family': [],
            'Music': [],
            'News & Politics': [],
            'Religion & Spirituality': [
                'Buddhism', 'Christianity', 'Hinduism', 'Islam', 'Judaism',
                'Other', 'Spirituality'],
            'Science & Medicine': [
                'Medicine', 'Natural Sciences', 'Social Sciences'],
            'Society & Culture': [
                'History', 'Personal Journals', 'Philosophy',
                'Places & Travel'],
            'Sports & Recreation': [
                'Amateur', 'College & High School', 'Outdoor', 'Professional'],
            'Technology': [
                'Gadgets', 'Tech News', 'Podcasting', 'Software How-To'],
            'TV & Film': []}
