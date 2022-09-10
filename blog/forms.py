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
        fields = ('title', 'author', 'featured_image', 'content', 'status',)        
        widgets = {
            'content': SummernoteWidget(),
        }


class AddContentForm(forms.ModelForm): 
    class Meta:
        model = HeroContent
        fields = ('hero_title', 'author', 'hero_featured_image',
                  'image_alt_text', 'hero_header', 'hero_excerpt', 
                  'images_on_desktop', 'image_height', 'image_place',
                  'image_order', 'hero_content', 'status',)
        widgets = {
            'hero_header': SummernoteWidget(),
            'hero_excerpt': SummernoteWidget(),        
            'hero_content': SummernoteWidget(),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ('first_name', 'last_name', 'email', 'contact_message',)