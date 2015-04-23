from django import template
from django.core.urlresolvers import reverse, resolve
register = template.Library()


@register.simple_tag
def nav_active(request, urls):
    if request.path in ( reverse(url) for url in urls.split() ):
        return 'class="active"'
    return ''

@register.simple_tag
def url_name(request):
    return resolve(request.path).url_name