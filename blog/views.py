from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from .models import Post, HeroContent, ContactMessage
from .forms import CommentForm, AddPostForm, ContactForm, AddContentForm


class PostList(generic.TemplateView):
    """View to render the list of POSTs on the home page."""
    template_name = 'index.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['blog_content'] = Post.objects.all()
        context['hero_content'] = HeroContent.objects.all()
        return context


class PostDetail(View):
    """View to render the detailed content of the POST, 'likes' and comments
       numbers. Plus, to display the form for th euser to leave a comment."""

    def get(self, request, slug, *args, **kwargs):
        """ Get Post information."""
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
        """ Return data for Post details rendering."""
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
    """View that renders the 'likes' for the specific user to add or remove"""
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


class AddPostView(generic.CreateView):
    """The view that renders the form to add the new Post from the
       front-end."""
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'add_post.html'
    form_class = AddPostForm


class UpdatePostView(generic.UpdateView):
    """The view that renders the pre-filled form to edit the Post from
       the front-end."""
    model = Post
    template_name = 'update_post.html'
    form_class = AddPostForm


class DeletePostView(generic.DeleteView):
    """The view that renders the form to delete a given Post."""
    model = Post
    template_name = 'delete_post.html'
    success_url = reverse_lazy('home')


def contact(request):
    """Renders the contact template."""
    if request.method == 'POST':
        first_name = request.POST['']
        last_name = models.CharField(max_length=80)
        email = models.EmailField()
        contact_message = models.TextField()
        created_on = models.DateTimeField(auto_now_add=True)

    return render(request, 'contact_form.html', {})


class ContactView(generic.CreateView):
    """The view to render the contact form for the registered user to leave
       a message to the admin."""
    model = ContactMessage
    template_name = 'contact_form.html'
    fields = ('first_name', 'last_name', 'email', 'contact_message')


class HeroContentDetail(generic.DetailView):
    """View to render the details of selected Content."""
    def get(self, request, slug, *args, **kwargs):
        queryset = HeroContent.objects.filter(status=1)

        content = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "hero_detail.html",
            {
               "content": content,
            },
        )


class AddContentView(generic.CreateView):
    """The view that renders the form to add the new Content
       from the front-end."""
    model = HeroContent
    template_name = 'add_content.html'
    form_class = AddContentForm


class UpdateContentView(generic.UpdateView):
    """The view that renders the pre-filled form to edit the Content card
       from the front-end."""
    model = HeroContent
    template_name = 'update_content.html'
    form_class = AddContentForm


class DeleteContentView(generic.DeleteView):
    """The view that renders the form to delete a given Content."""
    model = HeroContent
    template_name = 'delete_content.html'
    form_class = AddContentForm
    success_url = reverse_lazy('home')


class DraftList(generic.TemplateView):
    """The view that renders the pre-filled form to edit the Content with
       Status 'draft'."""
    template_name = 'draft_content.html'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['hero_content'] = HeroContent.objects.all()
        return context
