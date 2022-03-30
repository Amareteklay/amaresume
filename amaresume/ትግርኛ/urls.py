from django.urls import path

from . import views 

urlpatterns = [
    path('', views.tiglog, name='tiglog'),
]