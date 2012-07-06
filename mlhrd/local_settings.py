# Django settings for mlhrd project.
# local-settings.py 
# environment specific settings

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'mlhrddev',                      # Or path to database file if using sqlite3.
        'USER': 'mlhrduser',                      # Not used with sqlite3.
        'PASSWORD': 'mlhrdtvetssp',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}
