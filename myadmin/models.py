from django.db import models

# Create your models here.
class AdminUserMaster(models.Model):
    mstName = models.CharField(max_length=100, unique=True)
    mstEmail = models.EmailField(unique=True)
    mstPassword = models.CharField(max_length=100)
    mstStatus = models.BooleanField(default=True)

class CategoryMaster(models.Model):
    catName = models.CharField(max_length=100)
    catImage = models.ImageField(upload_to="catImage")
    catStatus = models.BooleanField(default=True, null=False)
    catSlug = models.SlugField()

class Product(models.Model):
    prdName = models.CharField(max_length=100)
    prdDescription = models.TextField()
    prdPrice = models.DecimalField(max_digits=10, decimal_places=2)
    prdIsoffer = models.BooleanField(default=False)
    prdOfferPrice = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    prdImage = models.ImageField(upload_to="prdImage")
    prdLatest = models.BooleanField(default=False)
    prdFeature = models.BooleanField(default=False)
    prdBlog = models.BooleanField(default=False)
    prdMailDes = models.TextField()