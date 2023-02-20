from django.db import models


# Create your models here.

class Address(models.Model):
    city = models.CharField(max_length=200)
    quarter = models.CharField(max_length=200)
    street_number = models.CharField(max_length=200)
    house_number = models.CharField(max_length=200)
    additional_info = models.TextField()

    def __str__(self):
        return self.city