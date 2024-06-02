from django import template
from mzfinder.models import Menu

register = template.Library()


@register.filter
def odd(i):
    if i % 2 == 0:
        return 1
    else:
        return 0

@register.filter
def makeSrc(tag):
    return 'img/'+tag+'.jpg'

@register.filter
def findMenu(name):
    return Menu.objects.filter(restaurant_id=name)