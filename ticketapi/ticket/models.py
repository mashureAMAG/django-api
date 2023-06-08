from datetime import datetime
from datetime import timedelta
from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Ticket(models.Model):
    name = models.CharField(max_length=200)
    validity = models.DateTimeField(default=datetime.now() + timedelta(days=7))
    created_by = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="created_by", null=True
    )
    reserved = models.BooleanField(default=False)
    reserved_by = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        null=True,
        blank=True,
        related_name="reserved_by",
    )

    def __str__(self):
        return self.name
