from django.db import models
from Address.models import Address


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=200)
    gender = models.CharField(max_length=200)
    language = models.CharField(max_length=200)
    email = models.EmailField()
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone = models.IntegerField()
    age = models.IntegerField()

    def __str__(self):
        return self.name
