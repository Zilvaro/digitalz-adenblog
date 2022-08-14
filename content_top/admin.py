from django.contrib import admin
from .models import Content
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Content)
class ContentAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content',)
