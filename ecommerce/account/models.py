from django.db import models
from ecommerce.user.models import User


class Address(models.Model):
    user = models.OneToOneField(User)
    address_header = models.CharField(max_length=100)
    name_surname = models.CharField(max_length=150)
    address = models.TextField()
    city = models.CharField(max_length=100)
    county = models.CharField(max_length=100)
    post_code = models.IntegerField()
    cell_phone = models.IntegerField()
    phone = models.IntegerField(blank=True)
    identification_number = models.IntegerField()