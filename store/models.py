from typing import Any
from django.db import models
from django.core.validators import MinValueValidator
from decimal import Decimal

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.CharField(max_length=1000, null=True)
    value = models.DecimalField(max_digits=10,decimal_places=2, validators=[MinValueValidator(Decimal('0.01'))])
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    img_url = models.URLField(null=True)
    creation_date = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
    

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=500, null=True)
    creation_date = models.DateField(auto_now_add=True)
    last_update = models.DateField(auto_now=True)

    def __str__(self):
        return self.name
