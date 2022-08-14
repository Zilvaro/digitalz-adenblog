from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Content


def content(request):
   return render(request, 'content.html')

class ContentList(generic.ListView):
    model = Content
    template_name = 'content.html'
    
