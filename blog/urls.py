from . import views
from django.urls import path

urlpatterns = [
    path("", views.PostList.as_view(), name="home"),
    
    path('post/<slug:slug>/', views.PostDetail.as_view(), name='post_detail'), 
    path('hero/<slug:slug>', views.HeroContentDetail.as_view(), name='hero_detail'),
       
    
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
    path('contact', views.contact, name="contact_form"),
    path('message/', views.ContactView.as_view(), name='contact_form'),
    path('add_post/', views.AddPostView.as_view(), name="add_post"),
    path('edit/<slug:slug>', views.UpdatePostView.as_view(), name='update_post'),
    path('delete/<slug:slug>', views.DeletePostView.as_view(), name='delete_post'),

    path('add_content/', views.AddContentView.as_view(), name="add_content"),
    path('update/<slug:slug>', views.UpdateContentView.as_view(), name='update_content'),
    path('delete_content/<slug:slug>', views.DeleteContentView.as_view(), name='delete_content'),
  ]