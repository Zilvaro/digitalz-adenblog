from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from .models import Content


def content(request):
   return render(request, 'content.html')

class ContentList(generic.ListView):
   model = Content
   template_name = 'content.html'


class ContentDetail(View):
   
   def get(self, request, slug, *args, **kwargs):
        queryset = Content.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "content_detail.html",
            {
                "post": post
            },
        )