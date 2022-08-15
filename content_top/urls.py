from . import views
from django.urls import path

urlpatterns = [
   path('mycontent', views.content, name="content"),
   path('mylist', views.ContentList.as_view(), name="content"),
   path('article/<slug:slug>', views.ContentDetail.as_view(), name="content-view"),
]