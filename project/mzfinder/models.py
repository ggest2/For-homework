from django.db import models
from django.contrib.auth.models import User

class Restaurant(models.Model):
    name = models.TextField()
    tags = models.TextField()
    rating = models.IntegerField()
    adress = models.TextField()
    callNumber = models.TextField()
    def __str__(self):
        return self.name
    
class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()