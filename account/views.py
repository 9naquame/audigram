from django.http import HttpResponse, HttpResponseRedirect
from django import forms
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render_to_response
from django.views.decorators.csrf import csrf_exempt
from blog.models import Audi 
from django.contrib.auth.decorators import login_required 
from django.contrib.auth.models import User
from django.contrib.auth.signals import user_logged_in, user_logged_out
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm

class LoginForm(forms.Form):
        username = forms.CharField(label='Username')
        password = forms.CharField(widget=forms.PasswordInput,max_length=8,label='Password')

class SignUpForm(forms.Form):
        username = forms.CharField(label='Username',max_length=10)
        first_name = forms.CharField(label='First Name',max_length=30,required=False)
        last_name = forms.CharField(label='Last Name',max_length=30,required=False)
        email = forms.EmailField(label='Email Address',required=False)
        password = forms.CharField(widget=forms.PasswordInput,max_length=8,label='Password')
        cpassword = forms.CharField(widget=forms.PasswordInput,max_length=8,label='Confirmation Password')


@csrf_exempt
def sign_up_view(request):
        audi_list = Audi.objects.all()[:3]
        if request.method == 'POST':
                form = SignUpForm(request.POST)
                if form.is_valid():
                        uname  = form.cleaned_data['username']
                        pword = form.cleaned_data['password']
                        fname = form.cleaned_data['first_name']
                        lname = form.cleaned_data['last_name']
                        emal = form.cleaned_data['email']
                        user = User.objects.create_user(username=uname,email=emal,password=pword)
                        user.first_name = fname
                        user.last_name = lname
                        name = fname + ' ' + lname
                        user.save()
                        return render_to_response('base.html', {'blog_list':audi_list,'request_user':request.user.username,'full_name':name })
        else:
                  form = SignUpForm()
        return render_to_response('account/signup.html', {'form': form,'audi_list':blog_list})

@csrf_exempt
def loginView(request):               
        audi_list = Audi.objects.all()[:3]
        if request.method == 'POST':
                form = LoginForm(request.POST)
                if form.is_valid():
                        uname  = form.cleaned_data['username']
                        pword = form.cleaned_data['password']
                        user = authenticate(username=uname, password=pword)
                        if user is not None:
                                if user.is_active:
                                        login(request,user)
                                        name = user.get_full_name()
                                        return HttpResponseRedirect("/audi/")
	else:
                form = LoginForm()
	return render_to_response('account/login.html', {'form': form,'audi_list':audi_list,'logged_in':request.user.is_authenticated()})

    
@csrf_exempt
def logoutView(request):
        logout(request)
        return render_to_response('account/logout.html',{'blog_list':Audi.objects.all()[:3]})

