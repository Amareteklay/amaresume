from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resume/', views.resume, name='resume'),
    path('about', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('register', views.register_request, name="register"),
    path('login', views.login_request, name="login"),
    path('logout', views.logout_request, name="logout"),
]