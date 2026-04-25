# -*- coding: utf-8 -*-
'''
    feedgen.ext.geo_entry
    ~~~~~~~~~~~~~~~~~~~

    Extends the FeedGenerator to produce Simple GeoRSS feeds.

    :copyright: 2017, Bob Breznak <bob.breznak@gmail.com>

    :license: FreeBSD and LGPL, see license.* for more details.
'''
import numbers
import warnings

from feedgen.ext.base import BaseEntryExtension
from feedgen.util import xml_elem


class GeoRSSPolygonInteriorWarning(Warning):
    """
    Simple placeholder for warning about ignored polygon interiors.

    Stores the original geom on a ``geom`` attribute (if required warnings are
    raised as errors).
    """

    def __init__(self, geom, *args, **kwargs):
        pass

    def __str__(self):
        return '{:d} interiors of polygon ignored'.format(
            len(self.geom.__geo_interface__['coordinates']) - 1
        )  # ignore exterior in count


class GeoRSSGeometryError(ValueError):
    """
    Subclass of ValueError for a GeoRSS geometry error

    Only some geometries are supported in Simple GeoRSS, so if not raise an
    error. Offending geometry is stored on the ``geom`` attribute.
    """

    def __init__(self, geom, *args, **kwargs):
        pass

    def __str__(self):
        msg = "Geometry of type '{}' not in Point, Linestring or Polygon"
        return msg.format(
            self.geom.__geo_interface__['type']
        )


class GeoEntryExtension(BaseEntryExtension):
    '''FeedEntry extension for Simple GeoRSS.
    '''

    def __init__(self):
        '''Simple GeoRSS tag'''
        # geometries
        self.__point = None
        self.__line = None
        self.__polygon = None
        self.__box = None

        # additional properties
        self.__featuretypetag = None
        self.__relationshiptag = None
        self.__featurename = None

        # elevation
        self.__elev = None
        self.__floor = None

        # radius
        self.__radius = None

    def extend_file(self, entry):
        '''Add additional fields to an RSS item.

        :param feed: The RSS item XML element to use.
        '''

        pass

    def extend_rss(self, entry):
        pass

    def extend_atom(self, entry):
        pass

    def point(self, point=None):
        '''Get or set the georss:point of the entry.

        :param point: The GeoRSS formatted point (i.e. "42.36 -71.05")
        :returns: The current georss:point of the entry.
        '''
        pass

    def line(self, line=None):
        '''Get or set the georss:line of the entry

        :param point: The GeoRSS formatted line (i.e. "45.256 -110.45 46.46
                      -109.48 43.84 -109.86")
        :return: The current georss:line of the entry
        '''
        pass

    def polygon(self, polygon=None):
        '''Get or set the georss:polygon of the entry

        :param polygon: The GeoRSS formatted polygon (i.e. "45.256 -110.45
                        46.46 -109.48 43.84 -109.86 45.256 -110.45")
        :return: The current georss:polygon of the entry
        '''
        pass

    def box(self, box=None):
        '''
        Get or set the georss:box of the entry

        :param box: The GeoRSS formatted box (i.e. "42.943 -71.032 43.039
                    -69.856")
        :return: The current georss:box of the entry
        '''
        pass

    def featuretypetag(self, featuretypetag=None):
        '''
        Get or set the georss:featuretypetag of the entry

        :param featuretypetag: The GeoRSS feaaturertyptag (e.g. "city")
        :return: The current georss:featurertypetag
        '''
        pass

    def relationshiptag(self, relationshiptag=None):
        '''
        Get or set the georss:relationshiptag of the entry

        :param relationshiptag: The GeoRSS relationshiptag (e.g.
                                "is-centred-at")
        :return: the current georss:relationshiptag
        '''
        pass

    def featurename(self, featurename=None):
        '''
        Get or set the georss:featurename of the entry

        :param featuretypetag: The GeoRSS featurename (e.g. "Footscray")
        :return: the current georss:featurename
        '''
        pass

    def elev(self, elev=None):
        '''
        Get or set the georss:elev of the entry

        :param elev: The GeoRSS elevation (e.g. 100.3)
        :type elev: numbers.Number
        :return: the current georss:elev
        '''
        pass

    def floor(self, floor=None):
        '''
        Get or set the georss:floor of the entry

        :param floor: The GeoRSS floor (e.g. 4)
        :type floor: int
        :return: the current georss:floor
        '''
        pass

    def radius(self, radius=None):
        '''
        Get or set the georss:radius of the entry

        :param radius: The GeoRSS radius (e.g. 100.3)
        :type radius: numbers.Number
        :return: the current georss:radius
        '''
        pass

    def geom_from_geo_interface(self, geom):
        '''
        Generate a georss geometry from some Python object with a
        ``__geo_interface__`` property (see the `geo_interface specification by
        Sean Gillies`_geointerface )

        Note only a subset of GeoJSON (see `geojson.org`_geojson ) can be
        easily converted to GeoRSS:

        - Point
        - LineString
        - Polygon (if there are holes / donuts in the polygons a warning will
          be generated

        Other GeoJson types will raise a ``ValueError``.

        .. note:: The geometry is assumed to be x, y as longitude, latitude in
           the WGS84 projection.

        .. _geointerface: https://gist.github.com/sgillies/2217756
        .. _geojson: https://geojson.org/

        :param geom: Geometry object with a __geo_interface__ property
        :return: the formatted GeoRSS geometry
        '''
        pass
