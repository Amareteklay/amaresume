from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout 
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from .models import Contact
from .forms import ContactForm



# Create your views here.


def index(request):
    return render(request, 'pages/index.html')

def resume(request):
    return render(request, 'pages/resume.html')

def about(request):
    return render(request, 'pages/about.html')

def home(request):
    return render(request, 'pages/home.html')

def project_list(request):
    return render(request, 'pages/project_list.html')

def contact(request):
    form = ContactForm()
    context = {'form': form}
    return render(request, 'pages/contact.html', context)