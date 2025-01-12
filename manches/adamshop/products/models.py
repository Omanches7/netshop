from django.db import models


class products (models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    stock = models.IntegerField()
    image_url = models.CharField(max_length=2101)


class offer (models.Model):
    Code = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    discount = models.FloatField(max_length=12)

