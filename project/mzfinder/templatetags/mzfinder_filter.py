from django import template
from mzfinder.models import Restaurant, Menu

from django.contrib.auth.models import User

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

@register.filter
def findRestaurant(name):
    restaurant = Restaurant.objects.get(id=name)
    return restaurant

@register.filter
def findUser(name):
    user = User.objects.get(id=name)
    return user
@register.filter
def returnRestaurant(name):
    return name.id