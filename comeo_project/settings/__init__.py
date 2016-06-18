import os

# Load distinct settings files


# TODO: instead of code in this file use DJANGO_SETTINGS_MODULE in the Docker env file
OUTSIDE = os.environ.get('OUTSIDE')

if OUTSIDE == 'development':
    from .dev import *
elif OUTSIDE == 'production':
    from .prod import *
elif OUTSIDE == 'lab':
    from .lab import *

if not OUTSIDE:
    from .dev import *
