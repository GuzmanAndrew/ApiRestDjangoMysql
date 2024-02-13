from django.db import models

class User(models.Model):
   name = models.CharField(max_length=50)
   lastaname = models.CharField(max_length=50)
   address = models.CharField(max_length=100)
   age = models.PositiveIntegerField()
