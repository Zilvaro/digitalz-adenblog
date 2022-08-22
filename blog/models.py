from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse


STATUS = ((0, "Draft"), (1, "Published"))
IMAGECOUNT = ((1, "Whole Page"), (2, "2xPage"))
IMAGEHEIGHT = ((320, "320px"), (270, "270px"), (160, "160px"), (88, "88px"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.title

    def number_of_likes(self):
        return self.likes.count()

    def get_absolute_url(self):
        return reverse('home',)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE,
                             related_name="comments")
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment {self.body} by {self.name}"


class HeroContent(models.Model):
    hero_title = models.CharField(max_length=200, unique=True)
    hero_slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="hero_content_posts"
    )
    hero_featured_image = CloudinaryField('image', default='placeholder')
    image_alt_text = models.CharField(max_length=200, blank=True, default='aden wellness theme image')
    hero_header = models.CharField(max_length=200, blank=True)
    hero_excerpt = models.TextField(blank=True)
    images_on_page = models.IntegerField(choices=IMAGECOUNT, default=1)
    image_height = models.IntegerField(choices=IMAGEHEIGHT, default=270)
    updated_on = models.DateTimeField(auto_now=True)
    hero_content = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.hero_title
