from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm, PostForm


class PostCreateView(CreateView, LoginRequiredMixin):
    """
    View to create blog posts
    """
    template_name = 'blog/create_post.html'
    form_class = PostForm

    def get_success_url(self):
        return reverse_lazy('blog:blog')


class PostEditView(LoginRequiredMixin, UpdateView):
    """
    View to update blog posts
    """
    model = Post
    fields = ['title', 'content', 'featured_image', 'excerpt', 'status']
    template_name = 'blog/edit_post.html'

    def get_success_url(self):
        slug = self.kwargs['slug']
        return reverse_lazy('blog:post_detail', kwargs={'slug': slug})

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author


class PostList(ListView):
    """
    A list view to display the list of blog posts
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog/blog.html'
    paginate_by = 10


class PostDetail(LoginRequiredMixin, View):
    """
    View for blog details page
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        form = CommentForm()
        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "has_commentd": False,
                "comments": comments,
                "liked": liked,
                "form": form
            },
        )

    def post(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by('created_on')
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True
        form = CommentForm(data=request.POST)
        if form.is_valid():
            form.instance.email = request.user.email
            form.instance.name = request.user
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            form = CommentForm()
        return render(
            request,
            "blog/post_detail.html",
            {
                "post": post,
                "has_commented": True,
                "comments": comments,
                "liked": liked,
                "form": form
            },
        )


class PostLike(View, LoginRequiredMixin):
    """
    Like blog post
    """
    def post(self, request, slug):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)
        return HttpResponseRedirect(reverse('blog:post_detail', args=[slug]))
