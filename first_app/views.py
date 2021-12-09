from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from first_app.forms import Userform
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from first_app.models import Fine, User
from datetime import date
# Create your views here.

def index(request):
    return render(request, 'first_app/index.html')

def register(request):
    registered  = False
    if request.method == "POST":
        user_form=Userform(data=request.POST)
        if user_form.is_valid():
            user=user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = Userform()
    return render(request,'first_app/registration.html',{'user_form':user_form,
                                                         'registered':registered})
