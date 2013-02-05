from django.template import Context, loader
from django.http import HttpResponse, HttpResponseRedirect
from models import Audi, Remark
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import auth
from django.shortcuts import render_to_response
from django import forms
#from django.contrib.auth.decorators import login_required
	
class UploadAudioForm(forms.Form):
    audio_file = forms.FileField()

def clean_audio_file(request):
	if request.method == 'POST':
		form = UploadAudioForm()
		if form.is_valid():
			files = form.cleaned_data.get('audio_file',False)
			return render_to_response('audi/try.html',{'form': form,'files': files})
	
	else:
		form = UploadAudioForm()
	return render_to_response('audi/try.html',{'form': form})

def home(request):
	audi_list = Audi.objects.all()[:3]
	return render_to_response('base.html', {'audi_list':audi_list,'request_user':request.user.username})
        if not request.user.is_authenticated():
                return render_to_response('base.html', {'audi_list':audi_list,'request_user':request.user.username})
        return render_to_response('base.html',
{'audi_list':audi_list})#'request_user':request.user.username,'full_name':request.user.get_full_name()})

        
