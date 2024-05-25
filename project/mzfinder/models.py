from django.db import models

class Restaurant(models.Model):
    name = models.TextField()
    tags = models.TextField()
    rating = models.IntegerField()
    adress = models.TextField()
    callNumber = models.TextField()
    def __str__(self):
        return self.subject