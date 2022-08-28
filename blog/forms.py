from .models import Comment, Post, ContactMessage
from django import forms
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
        
    

class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ('first_name', 'last_name', 'email', 'contact_message',)