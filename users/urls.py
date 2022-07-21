from django.contrib.auth import views as auth_views
from django.urls import path
from . import views


urlpatterns = [
    path('', views.profile, name='profile'),
    path('signup/', views.register, name='signup'),
    path('login/', auth_views.LoginView.as_view(
        template_name='account/login.html'),
        name='login'),
    path('logout/', auth_views.LogoutView.as_view(
        template_name='account/logout.html'),
        name='logout'
        ),
    path('<username>/update/', views.update_profile, name='update-profile'),
    path('<pk>/delete/', views.delete_profile, name='delete-profile')
]
