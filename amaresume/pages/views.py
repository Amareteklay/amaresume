from django.shortcuts import render, redirect
from .forms import NewUserForm
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


### From https://ordinarycoders.com/blog/article/django-user-register-login-logout

def register_request(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("home")
        messages.error(request, "Registration failed. Invalid information.")
    form= NewUserForm()
    return render(request=request, template_name="pages/register.html", context={"register_form": form})


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}.")
                return redirect("home")
            else:
                messages.error(request, "Invalid username or password.")
        else:
            messages.error(request, "Invalid username or password.")
    form = AuthenticationForm()
    return render(request=request, template_name = "pages/login.html", context={"login_form":form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("pages:home")