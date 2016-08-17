from django.conf import settings


def environment_processor(request):
    # settings.OUTSIDE determined by OS environment variable
    to_context = {'outside': settings.OUTSIDE}

    return to_context
