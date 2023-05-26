from django.db import models

# Create your models here.


class Ticket(models.Model):
    name = models.CharField(max_length=200)
    validity = models.CharField(max_length=500)
    objects = models.Manager()

    def __str__(self):
        return self.name
