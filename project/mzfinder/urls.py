from django.urls import path

from . import views

app_name = 'mzfinder'

urlpatterns = [
    path('', views.index,name='main'),
    path('randomRecommend/',views.randomRecommend, name='randomRecommend'),
    path('<str:tag>/',views.restaurant,name='restaurants'),
    path('restaurant/<str:restaurantName>/',views.detailRestaurant,name='detailRestaurant'),
    path('restaurants/<str:restaurantName>/review/',views.createReview,name='createReview'),
    path('restaurants/<str:restaurantName>/like/',views.addLike,name='addLike'),
    
]