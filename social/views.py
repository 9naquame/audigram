from django.conf import settings
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.utils.translation import gettext as _
from django.http import HttpResponseRedirect, HttpResponse

from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout as auth_logout
from django.contrib.sites.models import Site

from social.form import UserForm
from social.models import TwitterProfile

GENERATE_USERNAME = bool(getattr(settings, 'SOCIAL_GENERATE_USERNAME', False))

def get_next(request):
    if 'next' in request.session:
        next = request.session['next']
        del request.session['next']
        return next
    elif 'next' in request.GET:
        return request.GET.get('next')
    elif 'next' in request.POST:
        return request.POST.get('next')
    else:
        return HttpResponse("Error")#return getattr(settings, 'LOGIN_REDIRECT_URL', '/')
