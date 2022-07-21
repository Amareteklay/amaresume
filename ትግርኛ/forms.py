from django import forms
from django_summernote.widgets import SummernoteWidget
from .models import ርእይቶ, ልጣፍ


class ቅጥዒልጣፍ(forms.ModelForm):
    """ Form to create blog posts """
    class Meta:
        model = ልጣፍ
        fields = ('ደራሲ',
                  'ኣርእስቲ',
                  'ትሕዝቶ',
                  'ምስሊ',
                  'መጠቓለሊ',
                  'ምድብ')
        widgets = {
            'ትሕዝቶ': SummernoteWidget(),
            'መጠቓለሊ': SummernoteWidget()
        }

    def __init__(self, *args, **kwargs):
        super(ቅጥዒልጣፍ, self).__init__(*args, **kwargs)
        self.fields['ኣርእስቲ'].widget.attrs = {'placeholder': 'ኣርእስቲ...',
                                             'class': 'form-control',
                                             'rows': '5'}
        self.fields['ትሕዝቶ'].widget.attrs = {'placeholder': 'ትሕዝቶ...',
                                               'class': 'form-control',
                                               'rows': '5'}
        self.fields['መጠቓለሊ'].widget.attrs = {'placeholder': 'መጠቓለሊ...',
                                               'class': 'form-control',
                                               'rows': '5'}


class ቅጥዒርእይቶ(forms.ModelForm):
    """ Form to add comments to blog posts """
    class Meta:
        model = ርእይቶ
        fields = ('ትሕዝቶ',)

    def __init__(self, *args, **kwargs):
        super(ቅጥዒርእይቶ, self).__init__(*args, **kwargs)
        self.fields['ትሕዝቶ'].widget.attrs = {'placeholder': 'ርእይቶ...',
                                            'class': 'form-control',
                                            'rows': '5'}
