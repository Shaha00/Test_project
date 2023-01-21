from django.db import models


# Create your models here.


class Product(models.Model):
    title = models.CharField(max_length=180)
    text = models.TextField(null=True, blank=True)
    price = models.FloatField(default=0)
    quantity = models.IntegerField(default=0)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    @property
    def product_quantity(self):
        if self.quantity < 1:
            return 'No product'
        return self.quantity
