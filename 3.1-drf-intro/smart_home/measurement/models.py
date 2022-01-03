from django.db import models

from django.db.models import FloatField, DateTimeField


class Sensor(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=50)


class Measurement(models.Model):
    temperature = FloatField()
    created_at = DateTimeField(auto_now_add=True)
