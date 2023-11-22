from . import views
from django.urls import path

# List of URL patterns and their corresponding views

# URL pattern for the home page, associated with the PostList view
urlpatterns = [
    path('', views.PostList.as_view(), name='home'),

    # URL pattern for displaying details of a single post, uses a slug to identify the post
    path('<slug:slug>/', views.PostDetail.as_view(), name='post_detail'),

    # URL pattern for handling the 'like' functionality on a post, using the post's slug
    path('like/<slug:slug>', views.PostLike.as_view(), name='post_like'),
]
