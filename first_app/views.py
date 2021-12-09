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
