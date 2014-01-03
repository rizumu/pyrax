# -*- coding: utf-8 -*-
"""
pyrax._compat
~~~~~~~~~~~~~~

Some py2/py3 compatibility support based on a stripped down
version of six so we don't have to depend on a specific version
of it.

:copyright: Copyright 2013 by the Jinja team, see AUTHORS.
:license: BSD, see LICENSE for details.
"""
import sys

PY2 = sys.version_info[0] == 2


if not PY2:
    import configparser
    from http import client as httplib
    from urllib.parse import urlparse, urlunparse, quote

    unichr = chr
    range_type = range
    text_type = str
    string_types = (str,)

    iterkeys = lambda d: iter(d.keys())
    itervalues = lambda d: iter(d.values())
    iteritems = lambda d: iter(d.items())

    from io import BytesIO, StringIO
    NativeStringIO = StringIO

else:
    import ConfigParser as configparser
    import httplib
    from urllib import quote
    from urlparse import urlparse, urlunparse

    unichr = unichr
    text_type = unicode
    range_type = xrange
    string_types = (str, unicode)

    iterkeys = lambda d: d.iterkeys()
    itervalues = lambda d: d.itervalues()
    iteritems = lambda d: d.iteritems()

    from cStringIO import StringIO as BytesIO, StringIO
    NativeStringIO = BytesIO
