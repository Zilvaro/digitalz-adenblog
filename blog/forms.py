from django import forms
from .models import Comment, Post, ContactMessage, HeroContent
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class CommentForm(forms.ModelForm):
    """Form for post-comment submission."""
    class Meta:
        model = Comment
        fields = ('body',)


class AddPostForm(forms.ModelForm):
    """Returns the form for adding new Post using POST model. Author and Status
       fields are hidden fields and prefilled directly into the form."""
    class Meta:
        model = Post
        fields = ('title', 'author', 'posted_by', 'order', 'featured_image',
                  'excerpt', 'content', 'status',)
        widgets = {
            'content': SummernoteWidget(),
            'posted_by': SummernoteWidget(),
            'author': forms.TextInput(attrs={'class': 'form-control',
                                             'value': '',
                                             'id': 'poster',
                                             'type': 'hidden'}),
            'status': forms.TextInput(attrs={'class': 'form-control',
                                             'value': '',
                                             'id': 'status_id',
                                             'type': 'hidden'}),
        }


class AddContentForm(forms.ModelForm):
    """Returns the form for adding new Content Card using HeroContent model. Author 
       field is hidden to protect unauthorized input."""
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
    """Form for contact-message submission."""
    class Meta:
        model = ContactMessage
        fields = ('first_name', 'last_name', 'email', 'contact_message',)
