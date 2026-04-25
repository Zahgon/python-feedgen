# -*- coding: utf-8 -*-
'''
    feedgen
    ~~~~~~~

    :copyright: 2013-2016, Lars Kiesow <lkiesow@uos.de>

    :license: FreeBSD and LGPL, see license.* for more details.
'''

import sys

from feedgen.feed import FeedGenerator


USAGE = '''
Usage: python -m feedgen [OPTION]

Use one of the following options:

File options:
  <file>.atom      -- Generate ATOM test feed
  <file>.rss       -- Generate RSS test teed

Stdout options:
  atom             -- Generate ATOM test output
  rss              -- Generate RSS test output
  podcast          -- Generate Podcast test output
  dc.atom          -- Generate DC extension test output (atom format)
  dc.rss           -- Generate DC extension test output (rss format)
  syndication.atom -- Generate syndication extension test output (atom format)
  syndication.rss  -- Generate syndication extension test output (rss format)
  torrent          -- Generate Torrent test output

'''


def print_enc(s):
    '''Print function compatible with both python2 and python3 accepting
    strings and byte arrays.
    '''
    pass


def main():
    pass


if __name__ == '__main__':
    main()
