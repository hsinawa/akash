from typing_extensions import Required
from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.


class Users(models.Model):
    name = models.CharField(max_length=122, primary_key=True)
    email = models.CharField(max_length=122)
    phone = models.TextField(max_length=12)
    contacts = ArrayField(models.CharField(max_length=50), blank=True, null=True)
    



class Numbers(models.Model):
    phone = models.TextField(max_length=12, primary_key=True)
    is_spam = models.BooleanField(default=False, required =True)
    user =  models.CharField(max_length=122)