import os

OUTSIDE = os.environ.get('OUTSIDE', None)

beta = (OUTSIDE == 'development')

def custom_processor(request):
    to_context = {'beta': beta}
    return to_context