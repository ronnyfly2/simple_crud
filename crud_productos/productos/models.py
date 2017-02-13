from django.db import models

# Create your models here.

class Product(models.Model):
    sku = models.CharField(max_length=5)
    name = models.CharField(max_length=50)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)

    def __str__(self):
        return self.name
