from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from products.models import Product
# Create your models here.


class Comment(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE)
    comment = models.CharField(max_length=300)
    rating = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
    ])

    def __str__(self):
        return self.comment
