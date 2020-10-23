#!/usr/bin/env python
# -*- coding: utf-8 -*- #

AUTHOR = 'Hang Xu'
SITENAME = 'Hang Xu'
SITEURL = ''

PATH = 'content'
OUTPUT_PATH = '.'
STATIC_PATHS = ['images', 'extra', ]
EXTRA_PATH_METADATA = {
        'extra/favicon.ico': {'path': 'favicon.ico'}, 
        }


TIMEZONE = 'Asia/Hong_Kong'

DEFAULT_LANG = 'en'

LOCALE = ('usa',       # On Windows
          'en_US'      # On Unix/Linux
)

THEME = "simpleplus"

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True