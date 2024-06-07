from django.contrib import admin

from .models import Restaurant 
from .models import Comment


class RestaurantAdmin(admin.ModelAdmin):
    search_fields = ['name']
class CommentAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Restaurant,RestaurantAdmin)
