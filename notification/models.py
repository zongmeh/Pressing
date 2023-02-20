from django.db import models


# Create your models here.
class Notification(models.Model):
    heading = models.CharField(max_length=200)
    receiver = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    message = models.TextField()
    time_sent = models.DateTimeField()

    def __str__(self):
        return self.heading
