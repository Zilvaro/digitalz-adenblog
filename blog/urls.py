from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('add_post/>', views.AddPostView.as_view(), name="add_post"),
    path('contact', views.contact, name="contact_form"),
    path('message/>', views.ContactView.as_view(), name='contact_form'),
  ]