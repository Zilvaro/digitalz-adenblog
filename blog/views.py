from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View 
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Post, HeroContent, ContactMessage 
from .forms import CommentForm, AddPostForm, ContactForm


class PostList(generic.TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, *args, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(*args, **kwargs)
        # Add in a QuerySet of all the books
        context['blog_content'] = Post.objects.all()
        context['hero_content'] = HeroContent.objects.all()
        return context
        

class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_detail.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )

class PostLike(View):
    
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class AddPostView(generic.CreateView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'add_post.html'
    fields = ('title', 'slug', 'author', 'featured_image', 'content', 'status')


class UpdatePostView(generic.UpdateView):
    model = Post
    template_name = 'update_post.html'
    fields = ('title', 'slug', 'featured_image', 'content', 'status')


class DeletePostView(generic.DeleteView):
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


def contact(request):
    if request.method == 'POST':
        first_name = request.POST['']
        last_name = models.CharField(max_length=80)
        email = models.EmailField()
        contact_message = models.TextField()
        created_on = models.DateTimeField(auto_now_add=True)

    return render(request, 'contact_form.html', {})


class ContactView(generic.CreateView):
    model = ContactMessage
    template_name = 'contact_form.html'
    fields = ('first_name', 'last_name', 'email', 'contact_message')


def heroview(request):
   return render(request, 'hero_detail.html')


class HeroContentDetail(View):
   
   def get(self, request, slug, *args, **kwargs):
        queryset = HeroContent.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "hero_detail.html",
            {
                "post": post
            },
        )