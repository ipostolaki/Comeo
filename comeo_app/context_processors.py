from django.conf import settings

# for development or lab environment there are beta flag, used to enable features intentionally disabled on production
beta = (settings.OUTSIDE == 'development' or settings.OUTSIDE == 'lab')


def custom_processor(request):
    to_context = {'beta': beta}
    return to_context
