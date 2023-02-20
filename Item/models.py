from django.db import models


# Create your models here.

class Items(models.Model):
    name = models.CharField(max_length=200)
    price = models.FloatField()
    quantity = models.IntegerField()
    total = models.IntegerField()

    def __str__(self):
        return self.name
