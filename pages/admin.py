from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(SummernoteModelAdmin):
    """
    Register contact to admin
    """
    list_display = ('name', 'email', 'subject', 'message')
    summernote_fields = ('message',)