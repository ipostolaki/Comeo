from django import template
from django.core.urlresolvers import reverse, resolve
register = template.Library()


@register.simple_tag
def nav_active(request, urls):
    if request.path in (reverse(url) for url in urls.split()):
        return 'class="active"'
    return ''


@register.simple_tag
def url_name(request):
    return resolve(request.path).url_name


@register.filter
def max100(current):
    if int(current) > 100:
        current = 100
    return current


@register.filter
def days_ru(digits):

    digits = str(digits)
    forms = ['день', 'дня', 'дней']

    if digits.endswith('1') and digits[-2:] != '11':
        return digits + ' ' + forms[0]
    elif digits[-1:] in '234' and digits[-2:] not in ['12','13','14']:
        return digits + ' ' + forms[1]
    else:
        return digits + ' ' + forms[2]


@register.simple_tag
def plural_ru(digits, *forms):

    digits = str(digits)

    if digits.endswith('1') and digits[-2:] != '11':
        return forms[0]
    elif digits[-1:] in '234' and digits[-2:] not in ['12','13','14']:
        return forms[1]
    else:
        return forms[2]