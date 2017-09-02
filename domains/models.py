from django.db import models

class Domain(models.Model):
    name = models.CharField(max_length=255, unique=True)

class Alias(models.Model):
    domain = models.ForeignKey('Domain')
    source = models.CharField(max_length=255)
    destination = models.CharField(max_length=255)
