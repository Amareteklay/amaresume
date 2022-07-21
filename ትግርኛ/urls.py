from django.urls import path
from . import views

app_name = 'ትግርኛ'

urlpatterns = [
    path('', views.TigPostList.as_view(), name='tig_blog'),
    path('create/', views.PostCreateView.as_view(), name='tigpost_create'),
    path('<slug:ስለግ>/', views.TigPostDetail.as_view(), name='tigblog_detail'),
    path('edit/<slug:ስለግ>/', views.PostEditView.as_view(), name='edit_post'),
    path('like/<slug:ስለግ>', views.PostLike.as_view(), name='post_like'),
]
