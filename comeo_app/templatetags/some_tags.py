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
    if int(current) > 100:
        current = 100
    return current


@register.simple_tag
def plural_ru(digits, *forms):
    """
    Receives digits and three plural forms of russian word to determine which form to use in UI
    Template usage: {% plural_ru campaign.days_to_finish 'день' 'дня' 'дней' %}
    """
    digits = str(digits)

    if digits.endswith('1') and digits[-2:] != '11':
        return forms[0]  # Ex: 1 день, 51 день
    elif digits[-1:] in '234' and digits[-2:] not in ['12', '13', '14']:
        return forms[1]  # Ex: 2 дня
    else:
        return forms[2]  # Ex: 0 дней, 5 дней, 11 дней, 12 дней
