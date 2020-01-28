from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.

class Table(models.Model):
    Name_of_the_User = models.TextField(max_length='512', null="True", blank="True", default="False")
    Age = models.IntegerField(blank="True", null="True", default="False")
    Allowed = models.BooleanField(default=True)
