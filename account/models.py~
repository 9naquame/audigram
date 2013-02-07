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
    profile_picture = models.ImageField(upload_to='thumbpath', blank=True)
    user = models.OneToOneField(User)#user = models.ForeignKey(User, unique=True)
    def __unicode__(self):
         return unicode(self.user)

class UserProfileAdmin(admin.ModelAdmin):
	list_display = ('user','country','location','profile_picture')
	search_fields = ('user','country')
	list_filter = ('user','country','gender')
	def __unicode__(self):
		return self.list_display

admin.site.register(UserProfile,UserProfileAdmin)
