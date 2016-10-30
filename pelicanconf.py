#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'levin'
SITENAME = u"bicky.me"
SITEURL = 'http://localhost:8000'

PATH = 'content'

TIMEZONE = 'Asia/Shanghai'

DEFAULT_LANG = u'zh-CN'

THEME = 'pelican-themes/elegant'
DISQUS_SITENAME = 'levinxo'
GOOGLE_ANALYTICS = 'UA-42652171-1'

PLUGIN_PATHS = ["pelican-plugins"]
PLUGINS = ["sitemap","neighbors",]

ARTICLE_URL = 'archive/{slug}/'
ARTICLE_SAVE_AS = 'archive/{slug}/index.html'
AUTHORS_SAVE_AS = False
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives', 'search', '404'))

SITEMAP = {
    "format": "xml",
    "priorities": {
        "articles": 0.5,
        "indexes": 0.5,
        "pages": 0.5,
    },
    "changefreqs": {
        "articles": "monthly",
        "indexes": "daily",
        "pages": "monthly",
    }
}


STATIC_PATHS = [
    #'static','img'
]
EXTRA_PATH_METADATA = {
    #'static/robots.txt': {'path': 'robots.txt'},
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

SITE_LICENSE = u'&copy; 2012-<script>(function(){var t = new Date(), y = t.getFullYear();document.write(y);})()</script> <a href="/">bicky.me</a>. <a rel="nofollow" href="https://creativecommons.org/licenses/by-sa/4.0/">Some Rights Reserved</a>. &#124; <a rel="nofollow" href="https://www.bicky.me:3000/">Redmine</a>. <a rel="nofollow" href="https://www.bicky.me:3000/gerrit/">Gerrit</a>. <a href="https://www.bicky.me/whois/">Whois</a>.'

SUMMARY_MAX_LENGTH = 8
DEFAULT_PAGINATION = None

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
