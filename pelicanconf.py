#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'levin'
SITENAME = u"Levin's blog"
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh-CN'

THEME = 'pelican-themes/gum'
DISQUS_SITENAME = 'levinxo'

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ["sitemap"]

ARCHIVES_SAVE_AS = 'archive.html'
ARTICLE_URL = 'archive/{slug}/'
ARTICLE_SAVE_AS = 'archive/{slug}/index.html'
AUTHORS_SAVE_AS = False
TAGS_SAVE_AS = False
CATEGORIES_SAVE_AS = False

SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.7,
        "indexes": 0.3,
        "pages": 0.3,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "monthly",
        "pages": "monthly",
    }
}


STATIC_PATHS = [
    'static','img'
]
EXTRA_PATH_METADATA = {
    'static/robots.txt': {'path': 'robots.txt'},
    'static/favicon.ico': {'path': 'favicon.ico'},
    'static/README': {'path': 'README.md'},
    'static/CNAME': {'path': 'CNAME'},
    'static/url': {'path': 'url.html'},
}


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
