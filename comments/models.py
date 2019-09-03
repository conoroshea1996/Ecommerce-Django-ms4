from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from products.models import Product
from django.contrib.auth.models import User
from django.utils.timezone import datetime
# Create your models here.


class Comment(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE)
    comment = models.TextField(max_length=1000)
    rating = models.IntegerField(validators=[
        MaxValueValidator(5),
        MinValueValidator(1)
    ])
    date_posted = models.DateTimeField(default=datetime.now, blank=True)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.comment
