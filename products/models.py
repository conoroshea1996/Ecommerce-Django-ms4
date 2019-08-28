from django.db import models

# Create your models here.


class Catagory(models.Model):
    type = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.type


class Product(models.Model):
    name = models.CharField(max_length=254, default='', unique=True)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    image = models.ImageField(upload_to='images')
    catagory = models.ForeignKey(
        Catagory, on_delete=models.CASCADE, default='')

    def __str__(self):
        return self.name


class Photo(models.Model):
    product = models.ForeignKey('Product', on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='images')

    def __str__(self):
        return self.name
