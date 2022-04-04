from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import Friend



# Create your views here.


def index(request):
    return render(request, 'pages/index.html')

context = {}

context['dataset'] = Friend.objects.all()

def resume(request):
    return render(request, 'pages/resume.html', context)

def about(request):
    return render(request, 'pages/about.html')

def home(request):
    return render(request, 'pages/home.html')