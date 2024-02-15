from django.db import models

# Create your models here.
class movie(models.Model):
    rdate=models.DateField()
    moviename=models.CharField(max_length=50)
    actor=models.CharField(max_length=35)
    actress=models.CharField(max_length=35)
    rating=models.IntegerField()
