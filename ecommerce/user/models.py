from django.db import models


class User(models.Model):
    name = models.CharField(max_length=50)
    surname = models.CharField(max_length=50)
    email = models.EmailField(max_length=100)
    password = models.CharField(max_length=16)
    phone_number = models.IntegerField()
    gender = models.CharField(max_length=1, blank=True)
    birthday = models.CharField(max_length=20, blank=True)