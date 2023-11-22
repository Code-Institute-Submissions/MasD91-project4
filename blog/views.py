from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Post
from .forms import CommentForm

# Represents a ListView for displaying a list of posts
class PostList(generic.ListView):
    model = Post
    queryset = Post.objects.filter(status=1).order_by("-created_on")
    template_name = "index.html"
    paginate_by = 6

# Represents a View for displaying the details of a single post
class PostDetail(View):

    def get(self, request, slug, *args, **kwargs):
        # Fetching the post object matching the provided slug
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        
        # Fetching comments related to the post and preparing data for rendering
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
        # Similar to the 'get' method but handling POST request for commenting on a post
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
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

# Represents a View for handling 'like' functionality on a post
class PostLike(View):

    def post(self, request, slug):
        # Fetch the post object corresponding to the provided slug
        post_object = get_object_or_404(Post, slug=slug)

        # Toggles user's 'like' status for the post
        if post_object.likes.filter(id=request.user.id).exists():
            post_object.likes.remove(request.user)
        else:
            post_object.likes.add(request.user)
        
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))
