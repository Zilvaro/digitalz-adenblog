from . import views
from django.urls import path

urlpatterns = [
   path('mycontent', views.content, name="content"),
   path("content_list", views.ContentList.as_view(), name="content"),
]
