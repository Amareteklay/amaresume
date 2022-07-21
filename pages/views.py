from django.shortcuts import render
from django.views import View
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.db.models import Q
from blog.models import Post
from .forms import ContactForm
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


class ContactView(View):
    """ View for the contact form
     renders contact form and saves valid messages"""
    template_name = 'pages/contact.html'
    form_class = ContactForm
    initial = {'key': 'value'}

    def get(self, request, *args, **kwargs):
        form = self.form_class(initial=self.initial)
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            messages.success(self.request, 'Thank You for contacting us.\
             Your message has been submitted successfully.')
            return HttpResponseRedirect('/')
        else:
            errors = form.errors
            for error in errors:
                messages.error(self.request, 'Please, enter valid ' + error)
            return render(request, self.template_name, {'form': form})
