from django import forms
from .models import Comment, Post, ContactMessage, HeroContent
from django_summernote.fields import SummernoteTextFormField, SummernoteTextField


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)


class AddPostForm(forms.ModelForm):
    
    content = SummernoteTextField()
    
    class Meta:
        model = Post
        fields = ('title', 'slug', 'author', 'featured_image', 'content', 'status',)


class AddContentForm(forms.ModelForm): 
    class Meta:
        model = HeroContent
        fields = ('hero_title', 'hero_slug', 'author', 'hero_featured_image',
                  'image_alt_text', 'hero_header', 'hero_card',
                  'images_on_desktop', 'hero_content', 'status',)
      

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ('first_name', 'last_name', 'email', 'contact_message',)