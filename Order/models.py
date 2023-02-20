from django.db import models
from Item.models import Items


# Create your models here.

class Order(models.Model):
    status_option = (
        ('paid', 'paid'),
        ('incomplete payment', 'incomplete payment'),
        ('unpaid', 'unpaid'),
    )
    status = models.CharField(max_length=20, choices=status_option, default='unpaid')
    order = models.CharField(max_length=200)
    pick_up_date = models.DateTimeField()
    order_time = models.DateTimeField()
    item = models.ForeignKey(Items, on_delete=models.CASCADE)
