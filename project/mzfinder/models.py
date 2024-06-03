from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    name = models.TextField()
    tags = models.TextField()
    rating = models.IntegerField()
    adress = models.TextField(null=True, blank=True)
    callNumber = models.TextField(null=True, blank=True)
    imgSrc = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()


class Menu(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE)
    name = models.TextField(null=True, blank=True)
    price = models.TextField(null=True, blank=True)

class Comment(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.TextField()
    content = models.TextField()
    create_date = models.DateTimeField()
