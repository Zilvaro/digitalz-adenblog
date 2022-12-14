from django.contrib import admin
from .models import Post, Comment, HeroContent, ContactMessage
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content', 'posted_by',)


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ('name', 'email', 'body')
    actions = ['approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(approved=True)


@admin.register(HeroContent)
class HeroContentAdmin(SummernoteModelAdmin):

    list_display = ('hero_title', 'slug', 'status', 'created_on')
    search_fields = ['hero_title', 'hero_content']
    list_filter = ('status', 'created_on')
    prepopulated_fields = {'slug': ('hero_title',)}
    summernote_fields = ('hero_content', 'hero_header', 'hero_excerpt',)


@admin.register(ContactMessage)
class ContactsAdmin(SummernoteModelAdmin):

    list_display = ('first_name', 'last_name', 'email', 'contact_message')
    search_fields = ['first_name', 'last_name', 'email']
