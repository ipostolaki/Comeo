from django import template
from django.core.urlresolvers import reverse

register = template.Library()


@register.simple_tag
def nav_active(request, urls):
    if request.path in (reverse(url) for url in urls.split()):
        return "active"
    return ""


@register.filter
def max100(current):
    """
    Used for progress bar percentage UI
    """
    if int(current) > 100:
        current = 100
    return current
