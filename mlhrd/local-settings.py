# Django settings for mlhrd project.
# local-settings.py 
# environment specific settings
import sys
import os

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'mlhrd',                      # Or path to database file if using sqlite3.
        'USER': 'mlhrduser',                      # Not used with sqlite3.
        'PASSWORD': 'mlhrdtvetssp',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

INSTALLED_APPS += ('haystack',)

HAYSTACK_SITECONF = 'mlhrd.search_sites'
HAYSTACK_SEARCH_ENGINE = 'solr'
HAYSTACK_SOLR_URL = 'http://127.0.0.1:8983/solr'
