from django.shortcuts import render, get_list_or_404, redirect
from django.utils import timezone

from .models import Restaurant
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator  

import random


def index(request):
    return render(request, 'mzfinder/mainPage.html')

def restaurant(request,tag):
    page = request.GET.get('page', '1')
    restaurants = get_list_or_404(Restaurant, tags=tag)
    paginator = Paginator(restaurants, 10)
    page_obj = paginator.get_page(page)
    context = {'tag':tag,'restaurants':page_obj}
    return render(request, 'mzfinder/restaurants.html',context)

def detailRestaurant(request,restaurantName):
    restaurant = Restaurant.objects.get(name=restaurantName);
    context = {'restaurant':restaurant}
    return render(request,'mzfinder/detailRestaurant.html',context)

def randomRecommend(request):
    restaurants = Restaurant.objects.all()
    index = random.randrange(0,len(restaurants))
    restaurant = restaurants[index]
    context = {'restaurant':restaurant}
    return render(request,'mzfinder/randomRecommend.html',context)

@login_required(login_url='common:login')
def createReview(request,restaurantName):
    restaurant = Restaurant.objects.get(name=restaurantName)
    restaurant.review_set.create(author = request.user, content=request.POST.get('content'), create_date=timezone.now())
    return redirect('mzfinder:detailRestaurant', restaurantName=restaurant.name)

@login_required(login_url='common:login')
def addLike(request,restaurantName):
    restaurant = Restaurant.objects.get(name=restaurantName)
    restaurant.rating = restaurant.rating + 1
    restaurant.save()
    return redirect('mzfinder:detailRestaurant', restaurantName=restaurant.name)