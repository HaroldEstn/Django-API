from django.db import models

# Create your models here.

class Person(models.Model):
    document_type = models.CharField(max_length=20)
    document_num = models.PositiveIntegerField()
    names = models.CharField(max_length=100)
    lastnames = models.CharField(max_length=100)
    hobbie = models.CharField(max_length=255)

