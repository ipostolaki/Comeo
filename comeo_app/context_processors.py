from django.conf import settings


def environment_processor(request):

    # For development or lab environment there are is_beta flag,
    # used to enable features intentionally disabled on production
    beta = (settings.OUTSIDE == 'development' or settings.OUTSIDE == 'lab')

    # settings.OUTSIDE determined by OS environment variable
    to_context = {'is_beta': beta, 'outside': settings.OUTSIDE}

    return to_context
