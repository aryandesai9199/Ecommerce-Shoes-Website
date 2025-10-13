from django.db import models
from myadmin.models import Product
# Create your models here.


class con_us(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    message = models.TextField(max_length=500)

# class cartItem(models.Model):
#     name = models.CharField(Product.prdName)
#     price = models.DecimalField(Product.prdPrice)
#     quantity = models.PositiveIntegerField(default=1)
