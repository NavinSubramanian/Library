from django.db import models

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=100)
    password=models.CharField(max_length=100)

    def __str__(self):
        return self.username
    

class Book(models.Model):
    name = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    picture = models.CharField(max_length=500)
    genre = models.CharField(max_length=100,default=0)

    def __str__(self):
        return self.name