from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Favorite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.CharField(max_length=10)

    def __str__(self):
        return self.movie
