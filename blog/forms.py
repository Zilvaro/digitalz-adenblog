from django import forms
from .models import Comment, Post, ContactMessage, HeroContent
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'author', 'posted_by', 'order', 'featured_image',
                  'excerpt', 'content', 'status',)
        widgets = {
            'content': SummernoteWidget(),
            'posted_by': SummernoteWidget(),
            'author': forms.TextInput(attrs={'class': 'form-control',
                                             'value': '', 'id': 'poster',
                                             'type': 'hidden'}),
            'status': forms.TextInput(attrs={'class': 'form-control',
                                             'value': '', 'id': 'status_id',
                                             'type': 'hidden'}),
        }


class AddContentForm(forms.ModelForm):
    class Meta:
        model = HeroContent
        fields = ('hero_title', 'author', 'hero_featured_image',
                  'image_alt_text', 'hero_header', 'text_background',
                  'hero_excerpt',
                  'images_on_desktop', 'image_height', 'image_place',
                  'image_order', 'hero_content', 'status',)
        widgets = {
            'hero_header': SummernoteWidget(),
            'hero_excerpt': SummernoteWidget(),
            'hero_content': SummernoteWidget(),
            'author': forms.TextInput(attrs={'class': 'form-control',
                                             'value': '', 'id': 'writer',
                                             'type': 'hidden'}),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ('first_name', 'last_name', 'email', 'contact_message',)
