from django.conf import settings

beta = (settings.OUTSIDE == 'development')

def custom_processor(request):
    to_context = {'beta': beta}
    return to_context