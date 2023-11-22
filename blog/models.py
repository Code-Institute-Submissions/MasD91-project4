from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Choices for the 'status' field in Post model
STATUS = ((0, "Draft"), (1, "Published"))

# Model representing a blog post
class Post(models.Model):
    title = models.CharField(max_length=200, unique=True)  # Title of the blog post
    slug = models.SlugField(max_length=200, unique=True)  # URL slug for the post
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts")  # Author of the post
    featured_image = CloudinaryField('image', default='placeholder')  # Featured image for the post using Cloudinary
    excerpt = models.TextField(blank=True)  # A short excerpt or summary of the post
    updated_on = models.DateTimeField(auto_now=True)  # Date and time of the last update
    content = models.TextField()  # Content of the blog post
    created_on = models.DateTimeField(auto_now_add=True)  # Date and time of creation
    status = models.IntegerField(choices=STATUS, default=0)  # Status of the post: Draft or Published
    likes = models.ManyToManyField(User, related_name='blogpost_like', blank=True)  # Users who liked the post

    class Meta:
        ordering = ["-created_on"]  # Ordering posts by creation date in descending order

    def __str__(self):
        return self.title  # String representation of the Post model - returns the title of the post

    def number_of_likes(self):
        return self.likes.count()  # Method to count the number of likes for the post

# Model representing comments on a blog post
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")  # Post the comment is associated with
    name = models.CharField(max_length=80)  # Name of the commenter
    email = models.EmailField()  # Email of the commenter
    body = models.TextField()  # Content of the comment
    created_on = models.DateTimeField(auto_now_add=True)  # Date and time of comment creation
    approved = models.BooleanField(default=False)  # Approval status of the comment

    class Meta:
        ordering = ["created_on"]  # Ordering comments by creation date in ascending order

    def __str__(self):
        return f"Comment {self.body} by {self.name}"  # String representation of the Comment model - returns comment details
