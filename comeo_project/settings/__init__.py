import os

# Load distinct settings files

OUTSIDE = os.environ.get('OUTSIDE', None)

if OUTSIDE == 'development':
    from .dev import *
elif OUTSIDE == 'production':
    from .prod import *
elif OUTSIDE == 'lab':
    from .lab import *

if not OUTSIDE:
    from .dev import *
