# Create your models here.
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from CountryField import CountryField

class UserProfile(models.Model):
    updated = models.DateField(auto_now=True)
    country = CountryField(default='',max_length=3)
    location = models.CharField(max_length=140)
    gender = models.CharField(max_length=140)  
    #profile_picture = models.ImageField(upload_to='thumbpath', blank=True)
    user = models.ForeignKey(User, unique=True)#user = models.OneToOneField(User)
    def __unicode__(self):
        return self.user

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('updated',)
	search_fields = ('updated',)
	list_filter = ('updated',)
	def __unicode__(self):
		return self.list_display

admin.site.register(UserProfile,UserProfileAdmin)
