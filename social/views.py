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

def setup(request, template='social/setup.html',
    form_class=UserForm, extra_context=dict()):
    """
    Setup view to create a username & set email address after authentication
    """
    try:
        social_user = request.session['social_user']
        social_profile = request.session['social_profile']
    except KeyError:
        return render_to_response(
            template, dict(error=True), context_instance=RequestContext(request))

    if not GENERATE_USERNAME:
        # User can pick own username
        if not request.method == "POST":
            form = form_class(social_user, social_profile)
        else:
            form = form_class(social_user, social_profile, request.POST)
            
            if form.is_valid():
                form.save(request=request)
                user = form.profile.authenticate()
                login(request, user)

                del request.session['social_user']
                del request.session['social_profile']

                return HttpResponseRedirect(_get_next(request))

        extra_context.update(dict(form=form))

        return render_to_response(template, extra_context,
            context_instance=RequestContext(request))
        
    else:
        # Generate user and profile
        social_user.username = str(uuid.uuid4())[:30]
        social_user.save()

        social_profile.user = social_user
        social_profile.save()

        # Authenticate and login
        user = social_profile.authenticate()
        login(request, user)

        # Clear & Redirect
        del request.session['social_user']
        del request.session['social_profile']
        return HttpResponseRedirect(_get_next(request))

if has_csrf:
    setup = csrf_protect(setup)

