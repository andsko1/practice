# Create your views here.
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.contrib.auth.forms import UserCreationForm
from django import forms

def login(request):
    form = UserCreationForm(request.POST)    
    return render(request, "login.html", {'form': form,})

def authentication(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = auth.authenticate(username=username, password=password)

    if user is not None:
        auth.login(request, user)
        return render_to_response('login_success.html', {'full_name': request.user.username})
    else:
	return render_to_response('login_error.html')

def registration(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect('/login/')
        else:
            return render_to_response('fail_reg.html')
    else:
	form = UserCreationForm()
    return render(request, "registration.html", {'form': form,})















