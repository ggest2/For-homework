from django.urls import path

from . import views

app_name = 'mzfinder'

urlpatterns = [
    path('', views.index,name='main'),
    path('randomRecommend/',views.randomRecommend, name='randomRecommend'),
    path('map/<str:restaurantName>',views.map, name='map'),
    path('community/',views.community, name='community'),
    path('createCommunity/',views.createCommunity, name='createCommunity'),
    path('modifyCommunity/<str:commentId>',views.modifyComment, name='modifyComment'),
    path('deleteCommunity/<str:commentId>/', views.deleteComment, name='deleteComment'),
    path('<str:tag>/',views.restaurant,name='restaurants'),
    path('restaurant/find/',views.findRestaurants,name='findRestaurants'),
    path('restaurant/<str:restaurantName>/',views.detailRestaurant,name='detailRestaurant'),
    path('restaurant/create/<str:tag>/',views.createRestaurant,name='createRestaurant'),
    path('restaurants/review/<str:restaurantName>/',views.createReview,name='createReview'),
    path('restaurants/like/<str:restaurantName>/',views.addLike,name='addLike'),
    path('restaurants/modify/<str:reviewId>/',views.modifyReview,name='modifyReview'),
    path('restaurant/delete/<str:reviewId>/', views.deleteReview, name='deleteReview'),
    
]