# Create your models here.
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from CountryField import CountryField

class UserProfile(models.Model):
    updated = models.DateField(auto_now=True)
    country = CountryField(default='',max_length=3)
    user = models.OneToOneField(User)
    def __unicode__(self):
        return self.user
