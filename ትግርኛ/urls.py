from django.urls import path
from . import views

app_name = 'ትግርኛ'

urlpatterns = [
    path('', views.TigPostList.as_view(), name='tig_blog'),
    path('create/', views.PostCreateView.as_view(), name='tigpost_create'),
    path('<int:pk>/', views.TigPostDetail.as_view(), name='tigblog_detail'),
    path('edit/<int:pk>/', views.PostEditView.as_view(), name='edit_tigpost'),
    path('like/<int:pk>', views.PostLike.as_view(), name='tigpost_like'),
]
