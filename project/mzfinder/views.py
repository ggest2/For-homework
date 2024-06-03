from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone

from .models import Restaurant, Review, Comment
from django.db.models import Q

from django.contrib.auth.decorators import login_required
from django.contrib import messages

from django.core.paginator import Paginator  

from .forms import ReviewForm, CommentForm

import random

from selenium.common.exceptions import WebDriverException

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import time


def index(request):
    return render(request, 'mzfinder/mainPage.html')

def restaurant(request,tag):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    restaurants = Restaurant.objects.filter(tags=tag).order_by('-rating')
    if kw:
        restaurants = restaurants.filter(
            Q(name__icontains=kw) | 
            Q(tags__icontains=kw) |  
            Q(adress__icontains=kw) 
        ).distinct()
    paginator = Paginator(restaurants, 20)
    page_obj = paginator.get_page(page)
    context = {'tag':tag,'restaurants':page_obj, 'page': page, 'kw': kw}
    return render(request, 'mzfinder/restaurants.html',context)

def findRestaurants(request):
    page = request.GET.get('page', '1')
    kw = request.GET.get('kw', '')
    restaurants = Restaurant.objects.all()
    if kw:
        restaurants = restaurants.filter(
            Q(name__icontains=kw) | 
            Q(tags__icontains=kw) |  
            Q(adress__icontains=kw) 
        ).distinct()
    paginator = Paginator(restaurants, 20)
    page_obj = paginator.get_page(page)
    context = {'restaurants':page_obj, 'page': page, 'kw': kw}
    return render(request, 'mzfinder/restaurants.html',context)

def detailRestaurant(request,restaurantName):
    restaurant = Restaurant.objects.get(name=restaurantName)
    reviews = restaurant.review_set.all().order_by('-create_date')
    context = {'restaurant':restaurant, 'reviews':reviews}
    return render(request,'mzfinder/detailRestaurant.html',context)

def randomRecommend(request):
    restaurants = Restaurant.objects.all()
    index = random.randrange(0,len(restaurants))
    restaurant = restaurants[index]
    context = {'restaurant':restaurant}
    return render(request,'mzfinder/randomRecommend.html',context)

def community(request):
    comments = Comment.objects.all().order_by('-create_date')
    context = {'comments':comments}
    return render(request,'mzfinder/community.html',context)

def createCommunity(request):
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.create_date = timezone.now() 
            comment.author = request.user
            comment.save()
            return redirect('mzfinder:community')
    else:
        form = CommentForm()
    context = {'form': form}
    return render(request, 'mzfinder/createCommunity.html', context)

@login_required(login_url='common:login')
def createReview(request,restaurantName):
    restaurant = Restaurant.objects.get(name=restaurantName)
    restaurant.review_set.create(author = request.user, content=request.POST.get('content'), create_date=timezone.now())
    return redirect('mzfinder:detailRestaurant', restaurantName=restaurant.name)

@login_required(login_url='common:login')
def createRestaurant(request,tag):
    context = {'tag': tag}
    return render(request,'mzfinder/createRestaurant.html', context)

@login_required(login_url='common:login')
def addLike(request,restaurantName):
    restaurant = Restaurant.objects.get(name=restaurantName)
    restaurant.rating = restaurant.rating + 1
    restaurant.save()
    return redirect('mzfinder:detailRestaurant', restaurantName=restaurant.name)

@login_required(login_url='common:login')
def modifyReview(request, reviewId):
    review = get_object_or_404(Review, pk=reviewId)
    restaurantName = get_object_or_404(Restaurant, name=review.restaurant)
    if request.user != review.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('mzfinder:detailRestaurant', restaurantName = restaurantName)
    if request.method == "POST":
        form = ReviewForm(request.POST, instance=review)
        if form.is_valid():
            review = form.save(commit=False)
            review.create_date = timezone.now() 
            review.save()
            return redirect('mzfinder:detailRestaurant', restaurantName = restaurantName)
    else:
        form = ReviewForm(instance=review)
    context = {'form': form}
    return render(request, 'mzfinder/reviewForm.html', context)

@login_required(login_url='common:login')
def modifyComment(request, commentId):
    comment = get_object_or_404(Comment, pk=commentId)
    if request.user != comment.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('mzfinder:Community',)
    if request.method == "POST":
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.create_date = timezone.now() 
            comment.save()
            return redirect('mzfinder:community')
    else:
        form = CommentForm(instance=comment)
    context = {'form': form}
    return render(request, 'mzfinder/createCommunity.html', context)


@login_required(login_url='common:login')
def deleteReview(request, reviewId):
    review = get_object_or_404(Review, pk=reviewId)
    restaurant = get_object_or_404(Restaurant,name = review.restaurant)
    if request.user != review.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('mzfinder:detailRestaurant', restaurantName = restaurant)
    review.delete()
    return redirect('mzfinder:detailRestaurant', restaurantName = restaurant)

@login_required(login_url='common:login')
def deleteComment(request, commentId):
    comment = get_object_or_404(Comment, pk=commentId)
    if request.user != comment.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('mzfinder:community')
    comment.delete()
    return redirect('mzfinder:community')

def is_browser_closed(driver):
    try:
        handles = driver.window_handles
        if len(handles) == 0:
            return True
        else:
            return False
    except WebDriverException:
        return True
def map(request,restaurantName):
    
    driver = webdriver.Chrome()
    url = "https://m.map.kakao.com/"
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)
    searchBox = driver.find_element(By.XPATH,'//*[@id="innerQuery"]')
    searchBox.send_keys(restaurantName)
    searchBox.send_keys(Keys.ENTER)
    click = driver.find_element(By.XPATH,'//*[@id="placeList"]/li[1]/span[2]/a[2]')
    click.click()
    while True:
        if is_browser_closed(driver):
            break
        
    restaurant = Restaurant.objects.get(name=restaurantName)
    reviews = restaurant.review_set.all().order_by('-create_date')
    context = {'restaurant':restaurant, 'reviews':reviews}
    return render(request,'mzfinder/detailRestaurant.html',context)