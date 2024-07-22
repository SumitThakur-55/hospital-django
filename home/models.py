from django.db import models
from django.contrib.auth.models import User


class Home(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
# Create your models here.
class Doc(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, default=None)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    username = models.CharField(max_length=100, unique=True)
    password = models.CharField(max_length=100)