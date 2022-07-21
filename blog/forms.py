from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import Comment, Post


class PostForm(forms.ModelForm):
    """ Form to create blog posts """
    class Meta:
        model = Post
        fields = ('author',
                  'title',
                  'content',
                  'featured_image',
                  'excerpt',
                  'status')
        widgets = {
            'content': SummernoteWidget(),
            'excerpt': SummernoteWidget()
        }

    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['title'].widget.attrs = {'placeholder': 'Title...',
                                             'class': 'form-control',
                                             'rows': '5'}
        self.fields['content'].widget.attrs = {'placeholder': 'Content...',
                                               'class': 'form-control',
                                               'rows': '5'}
        self.fields['excerpt'].widget.attrs = {'placeholder': 'Excerpt...',
                                               'class': 'form-control',
                                               'rows': '5'}


class CommentForm(forms.ModelForm):
    """ Form to add comments to blog posts """
    class Meta:
        model = Comment
        fields = ('body',)

    def __init__(self, *args, **kwargs):
        super(CommentForm, self).__init__(*args, **kwargs)
        self.fields['body'].widget.attrs = {'placeholder': 'Comment here...',
                                            'class': 'form-control',
                                            'rows': '5'}
