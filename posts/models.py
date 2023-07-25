from django.db import models


class Product(models.Model):
    img = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=128)
    description = models.TextField(blank=True, null=True)
    rate = models.FloatField()
    create_data = models.DateTimeField(auto_now_add=True)
    modified_data = models.DateTimeField(auto_now=True)
