from django.conf.urls.defaults import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'audigram.views.home', name='home'),
    # url(r'^audigram/', include('audigram.foo.urls')),
    url(r'^audi/', include('audigram.audi.urlconfig')),
    url(r'^account/', include('audigram.account.urlconfig')),
	url(r'^social/', include('audigram.social.urlconfig')),
    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
