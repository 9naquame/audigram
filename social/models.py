from django.db import models

from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.sites.models import Site 

class TwitterProfile(models.Model):
    user = models.ForeignKey(User)
    site = models.ForeignKey(Site, default=Site.objects.get_current)
    twitter_id = models.PositiveIntegerField()
    
    def __unicode__(self):
        return u'%s: %s' % (self.user, self.twitter_id) 
    
    def authenticate(self):
        return authenticate(twitter_id=self.twitter_id)

