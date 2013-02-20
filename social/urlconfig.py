from django.conf import settings
from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url('^setup/$', 'social.views.setup',name='social_setup'),
    url('^logout/$', 'social.views.logout',name='social_logout'),
)

#Setup Twitter URLs if there's an API key specified
if getattr(settings, 'TWITTER_CONSUMER_KEY', None) is not None:
    urlpatterns = urlpatterns + patterns('',
        url('^twitter/redirect/$', 'social.views.oauth_redirect',
            dict(
                consumer_key=settings.TWITTER_CONSUMER_KEY,
                secret_key=settings.TWITTER_CONSUMER_SECRET_KEY,
                request_token_url=settings.TWITTER_REQUEST_TOKEN_URL,
                access_token_url=settings.TWITTER_ACCESS_TOKEN_URL,
                authorization_url=settings.TWITTER_AUTHORIZATION_URL,
                callback_url='twitter_callback'
            ),
            name='twitter_redirect'),

        url('^twitter/callback/$', 'social.views.oauth_callback',
            dict(
                consumer_key=settings.TWITTER_CONSUMER_KEY,
                secret_key=settings.TWITTER_CONSUMER_SECRET_KEY,
                request_token_url=settings.TWITTER_REQUEST_TOKEN_URL,
                access_token_url=settings.TWITTER_ACCESS_TOKEN_URL,
                authorization_url=settings.TWITTER_AUTHORIZATION_URL,
                callback_url='twitter'
            ),
            name='twitter_callback'
        ),
        url('^twitter/$', 'social.views.twitter', name='twitter'),
    )

urlpatterns = urlpatterns + patterns('',
    url('^openid/redirect/$', 'social.views.openid_redirect', name='openid_redirect'),
    url('^openid/callback/$', 'social.views.openid_callback', name='openid_callback')
)
