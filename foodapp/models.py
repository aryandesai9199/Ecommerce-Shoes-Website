from django.db import models

# Create your models here.


class recipe(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='recipe')

    def __str__(self):
        return self.name

class cont_us(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(blank=True)
    contacts = models.IntegerField()
    massage = models.TextField(blank=True, null=True)


# class Register(models.Model):
#     name = models.CharField(max_length=100)
#     email = models.EmailField(blank=True)
#     password = models.CharField(max_length=100)
#     cpassword = models.CharField(max_length=100)

