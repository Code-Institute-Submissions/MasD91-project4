from pathlib import Path
import os
import dj_database_url
from django.contrib.messages import constants as messages

# Checking if 'env.py' file exists and importing environment variables if available
if os.path.isfile('env.py'):
    import env

# Setting the base directory for the project
BASE_DIR = Path(__file__).resolve().parent.parent
TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')

# Secret key for Django application (used for cryptographic signing)
SECRET_KEY = os.environ.get('SECRET_KEY')

# Debug mode for development (should be turned off in production)
DEBUG = False

X_FRAME_OPTIONS = 'SAMEORIGIN'

# Whitelisted hosts that this Django application can serve
ALLOWED_HOSTS = [
    'md-project-4-db497f716926.herokuapp.com',
    'localhost',
    '8000-masd91-project4-u9ydcka4vmw.ws-eu106.gitpod.io',
]

# List of origins that are allowed to set cookies via CSRF
CSRF_TRUSTED_ORIGINS = [
    'https://md-project-4-db497f716926.herokuapp.com',
    'https://localhost',
    'https://8000-masd91-project4-u9ydcka4vmw.ws-eu106.gitpod.io'
]

# List of installed applications for this Django project
INSTALLED_APPS = [
    # Django's built-in apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',

    # Third-party apps
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'cloudinary_storage',
    'django.contrib.staticfiles',
    'cloudinary',
    'django_summernote',
    'crispy_forms',
    'crispy_bootstrap4',

    # Custom app (assuming 'blog' is your custom app)
    'blog',
]

# Site ID for Django's sites framework
SITE_ID = 1

# Redirect URLs after login and logout
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'

# Template pack for crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'

# Mapping Django message levels to Bootstrap alert classes
MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

# Account email verification setting (none here, change for production)
ACCOUNT_EMAIL_VERIFICATION = 'none'

# Middleware classes used by the Django application
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'allauth.account.middleware.AccountMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

# Root URL configuration for the Django project
ROOT_URLCONF = 'codestar.urls'

# Template configuration for the Django project
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [TEMPLATES_DIR],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# WSGI application entry point for the Django project
WSGI_APPLICATION = 'codestar.wsgi.application'

# Database configuration (using dj_database_url to parse DATABASE_URL from environment variables)
DATABASES = {
     'default': dj_database_url.parse(os.environ.get("DATABASE_URL"))
 }

# Password validation settings for user passwords
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization settings for the Django project
LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

# Static files configuration for the Django project
STATIC_URL = '/static/'
STATIC_STORAGE = 'cloudinary_storage.storage.StaticHashedCloudinaryStorage'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Media files configuration for the Django project
MEDIA_URL = 'media/'
DEFAULT_FILE_STORAGE = 'cloudinary_storage.storage.MediaCloudinaryStorage'

# Default primary key field type for models
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
