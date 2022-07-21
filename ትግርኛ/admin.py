from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import ልጣፍ, ርእይቶ


@admin.register(ልጣፍ)
class PostAdmin(SummernoteModelAdmin):
    """ Register ልጣፍ model to admin """
    list_display = ('ኣርእስቲ', 'ስለግ', 'ምድብ', 'ዕለት')
    search_fields = ['ኣርእስቲ', 'ትሕዝቶ']
    list_filter = ('ምድብ', 'ዕለት')
    prepopulated_fields = {'ስለግ': ('ኣርእስቲ',)}
    summernote_fields = ('ትሕዝቶ',)


@admin.register(ርእይቶ)
class CommentAdmin(admin.ModelAdmin):
    """ Register Comment model to admin """
    list_display = ('ሽም', 'ትሕዝቶ', 'ልጣፍ', 'ዕለት', 'ፀዲቑ')
    list_filter = ('ፀዲቑ', 'ዕለት')
    search_fields = ['ሽም', 'ኢመይል', 'ትሕዝቶ']
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)
