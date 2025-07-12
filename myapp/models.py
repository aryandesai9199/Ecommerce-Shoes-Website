from django.db import models

# Create your models here.

class student(models.Model):
    name = models.CharField(default = None, max_length=100)
    age = models.IntegerField(default=18)
    email = models.EmailField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    

class product(models.Model):
    name = models.CharField(max_length=100,default=True)
    price = models.IntegerField(default=0)
    email = models.ImageField(null=True)

    def __str__(self):
        return self.name

class detail(models.Model):
    name = models.CharField(max_length=80, default=None)
    address = models.TextField(null=True, blank=True)

class demo(models.Model):
    name = models.CharField(max_length=80, default=None)
    address = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    



# Django shell

# python manage.py shell





