from django.shortcuts import render
from .models import Restaurant

def index(request):
    return render(request, 'mzfinder/mainPage.html')
def restaurant(request,tag):
    restaurants = Restaurant.objects.filter(tags=tag)
    context = {'tag':tag,'restaurants':restaurants}
    return render(request, 'mzfinder/restaurants.html',context)