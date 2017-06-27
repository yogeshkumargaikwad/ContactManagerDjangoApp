"""
Definition of models.
"""

from django.db import models

class Contact(models.Model):
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Email = models.CharField(max_length=50)
    MobileNo = models.CharField(max_length=15)

# Create your models here.
