# Create your models here.
from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.CharField(max_length=100)
    date = models.DateTimeField(default=timezone.now)  # Automatically set current date

    # def __str__(self):
    #     return self.title
