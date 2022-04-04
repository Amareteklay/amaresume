from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resume/', views.resume, name='resume'),
    path('about', views.about, name='about'),
    path('home/', views.home, name='home'),
]