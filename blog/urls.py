from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.PostList.as_view(), name='blog'),
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('edit/<slug:slug>/', views.PostEditView.as_view(), name='edit_post'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
