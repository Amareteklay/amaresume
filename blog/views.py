from django.shortcuts import render
from .models import Post

# Create your views here.

def blog(request):
    context = {}
    context["dataset"] = Post.objects.all()
    
    return render(request, 'blog/blog.html', context)