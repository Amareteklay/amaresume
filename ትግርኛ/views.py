from django.shortcuts import render, get_object_or_404, reverse
from django.urls import reverse_lazy
from django.views.generic import ListView, View
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from .models import ልጣፍ
from .forms import ቅጥዒርእይቶ, ቅጥዒልጣፍ


class PostCreateView(CreateView, LoginRequiredMixin):
    """
    View to create blog posts
    """
    template_name = 'ትግርኛ/create_tigpost.html'
    form_class = ቅጥዒልጣፍ

    def get_success_url(self):
        return reverse_lazy('ትግርኛ:tig_blog')


class PostEditView(LoginRequiredMixin, UpdateView):
    """
    View to update blog posts
    """
    model = ልጣፍ
    fields = ['ኣርእስቲ', 'ትሕዝቶ', 'ምስሊ', 'መጠቓለሊ', 'ምድብ']
    template_name = 'ትግርኛ/edit_tigpost.html'

    def get_success_url(self):
        slug = self.kwargs['ስለግ']
        return reverse_lazy('ትግርኛ:tigblog_detail', kwargs={'ስለግ': slug})

    def test_func(self):
        ልጣፍ = self.get_object()
        return self.request.user == ልጣፍ.ደራሲ


class TigPostList(ListView):
    """
    A list view to display the list of blog posts
    """
    model = ልጣፍ
    queryset = ልጣፍ.objects.filter(ምድብ=1).order_by('ዕለት')
    template_name = 'ትግርኛ/tigblog.html'
    paginate_by = 10


class TigPostDetail(LoginRequiredMixin, View):
    """
    View for blog details page
    """
    def get(self, request, pk, *args, **kwargs):
        queryset = ልጣፍ.objects.filter(ምድብ=1)
        tigpost = get_object_or_404(queryset, pk=pk)
        comments = tigpost.tigcomments.filter(ፀዲቑ=True).order_by('ዕለት')
        liked = False
        if tigpost.ፈተውቲ.filter(id=self.request.user.id).exists():
            liked = True
        form = ቅጥዒልጣፍ()
        return render(
            request,
            "ትግርኛ/tigblog_detail.html",
            {
                "post": tigpost,
                "has_commentd": False,
                "comments": comments,
                "liked": liked,
                "form": form
            },
        )

    def post(self, request, pk, *args, **kwargs):
        queryset = ልጣፍ.objects.filter(ምድብ=1)
        tigpost = get_object_or_404(queryset, pk=pk)
        comments = tigpost.tigcomments.filter(ፀዲቑ=True).order_by('ዕለት')
        liked = False
        if tigpost.ፈተውቲ.filter(id=self.request.user.id).exists():
            liked = True
        form = ቅጥዒርእይቶ(data=request.POST)
        if form.is_valid():
            form.instance.ኢመይል = request.user.email
            form.instance.ሽም = request.user
            tigcomment = form.save(commit=False)
            tigcomment.ልጣፍ = tigpost
            tigcomment.save()
        else:
            form = ቅጥዒርእይቶ()
        return render(
            request,
            "ትግርኛ/tigblog_detail.html",
            {
                "post": tigpost,
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
    def post(self, request, pk):
        tigpost = get_object_or_404(ልጣፍ, pk=pk)
        if tigpost.ፈተውቲ.filter(id=request.user.id).exists():
            tigpost.ፈተውቲ.remove(request.user)
        else:
            tigpost.ፈተውቲ.add(request.user)
        return HttpResponseRedirect(reverse('ትግርኛ:tigblog_detail', args=[pk]))
