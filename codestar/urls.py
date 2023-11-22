from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # URL pattern for Django admin site
    path('admin/', admin.site.urls),
    
    # URL pattern for django-summernote integration
    path('summernote/', include('django_summernote.urls')),
    
    # URL patterns for the blog app (assuming 'blog.urls' includes the blog-related URLs)
    path('', include('blog.urls'), name='blog_urls'),

    # URL patterns for django-allauth authentication-related URLs
    path('accounts/', include('allauth.urls')),
]
