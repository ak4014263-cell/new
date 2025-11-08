# Temporary local settings for running the dev server locally.
# This file is intentionally lightweight and only overrides DATABASES to use SQLite.
# It imports everything from the project's base settings so INSTALLED_APPS stays intact.
from config.settings.settings import *  # noqa

# Use local SQLite file DB for local runs to avoid remote MySQL connections
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'local_db.sqlite3',
    }
}

DEBUG = True
