from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('resume/', views.resume, name='resume'),
    path('about', views.about, name='about'),
    path('home/', views.home, name='home'),
    path('projects/', views.project_list, name='projects'),
    path('contact/', views.ContactView.as_view(), name='contact'),
]