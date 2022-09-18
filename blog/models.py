from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.template.defaultfilters import slugify
from django.urls import reverse


STATUS = ((0, "Draft"), (1, "Published"))
IMAGECOUNTMOBILE = ((12, "Whole Page"), (6, "2xPage"))
IMAGECOUNTDESKTOP = ((12, "Whole Page"), (8, "2/3 of Page"),
                     (6, "Half of Page"), (4, "1/3 of Page"),
                     (3, "1/4 of Page"))
IMAGEHEIGHT = ((40, "400px"), (32, "320px"), (27, "270px"), (20, "220px"),
               (16, "160px"), (8, "88px"), (5, "50px"))
IMAGEPLACE = ((1, "Image-as-background"), (2, "Image-on-side"))
TEXTBACKGROUND = ((1, "No background"), (2, "Put background"))


class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    posted_by = models.TextField(null=True, blank=True)
    order = models.IntegerField(default=1)
    featured_image = CloudinaryField('image', default='placeholder')
    excerpt = models.TextField(blank=True)
    updated_on = models.DateField(auto_now=True)
    content = models.TextField(null=True, blank=True)
    created_on = models.DateField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)
    likes = models.ManyToManyField(
        User, related_name='blogpost_like', blank=True)

    class Meta:
        ordering = ["order"]

    def save(self, *args, **kwargs):
        if not self.slug:
            # the slug is set based on the submitted title
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

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
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="hero_content_posts"
    )
    hero_featured_image = CloudinaryField('image', default='placeholder')
    image_alt_text = models.CharField(max_length=200, blank=True,
                                      default='aden wellness theme image')
    hero_header = models.CharField(max_length=200, blank=True)
    text_background = models.IntegerField(choices=TEXTBACKGROUND,
                                          default=1)
    hero_excerpt = models.TextField(blank=True)
    images_on_mobile_page = models.IntegerField(choices=IMAGECOUNTMOBILE,
                                                default=12)
    images_on_desktop = models.IntegerField(choices=IMAGECOUNTDESKTOP,
                                            default=6)
    image_height = models.IntegerField(choices=IMAGEHEIGHT, default=27)
    image_place = models.IntegerField(choices=IMAGEPLACE, default=1)
    image_order = models.IntegerField(default=1)
    updated_on = models.DateTimeField(auto_now=True)
    hero_content = models.TextField(blank=True)
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["image_order"]

    def save(self, *args, **kwargs):
        if not self.slug:
            # the slug is set based on the submitted title
            self.slug = slugify(self.hero_title)
        return super().save(*args, **kwargs)

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
