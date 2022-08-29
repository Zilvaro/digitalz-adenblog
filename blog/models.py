from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.urls import reverse


STATUS = ((0, "Draft"), (1, "Published"))
IMAGECOUNTMOBILE = ((12, "Whole Page"), (6, "2xPage"))
IMAGECOUNTDESKTOP = ((12, "Whole Page"), (6, "2xPage"), (4, "3xPage"), (3, "4xPage"))
IMAGEHEIGHT = ((32, "320px"), (27, "270px"), (16, "160px"), (8, "88px"))
IMAGEPLACE = ((1, "Image-on-top"), (2, "Image-on-side"), (3, "Image-as-background"))

class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    content = models.TextField(null=True, blank=True)
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
    images_on_mobile_page = models.IntegerField(choices=IMAGECOUNTMOBILE, default=12)
    images_on_desktop = models.IntegerField(choices=IMAGECOUNTDESKTOP, default=6)
    image_height = models.IntegerField(choices=IMAGEHEIGHT, default=27)
    image_place = models.IntegerField(choices=IMAGEPLACE, default=3)
    updated_on = models.DateTimeField(auto_now=True)
    hero_content = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.hero_title

    def get_absolute_url(self):
        return reverse('home',)


class ContactMessage(models.Model):
    first_name = models.CharField(max_length=80)
    last_name = models.CharField(max_length=80)
    email = models.EmailField()
    contact_message = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return self.email

    def get_absolute_url(self):
        return reverse('home',)