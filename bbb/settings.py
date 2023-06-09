"""
Django settings for bbb project.

Generated by 'django-admin startproject' using Django 4.1.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-+2bomrmhme0rm$$8^1j+34c!=$8c5ged($n*cvf6%=w^+z3d(#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'bbb', 'oauth2_provider', 'sloth.api',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bbb.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'bbb.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
import os
ALLOWED_HOSTS.append('*')
MEDIA_ROOT = '{}/{}'.format(BASE_DIR, 'media')
STATIC_ROOT = '{}/{}'.format(BASE_DIR, 'static')
MEDIA_URL = '/media/'

CLOUD_PROVIDER_API_URL = os.environ.get('CLOUD_PROVIDER_API_URL', 'https://deploy.cloud.aplicativo.click')
CLOUD_PROVIDER_API_TOKEN = os.environ.get('CLOUD_PROVIDER_API_TOKEN', '0123456789')

CSRF_TRUSTED_ORIGINS = [
    'http://*.local.aplicativo.click',
    'https://*.cloud.aplicativo.click',
]
ADMINS = [('admin', 'admin@mydomain.com')]

USER_ROLE_NAME = 'Usuário'
LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Recife'
USE_I18N = True
USE_L10N = True
USE_TZ = False
DECIMAL_SEPARATOR = ','
USE_THOUSAND_SEPARATOR = True
OAUTH2_PROVIDER_APPLICATION_MODEL = 'api.application'
OAUTH2_PROVIDER = {
    'SCOPES_BACKEND_CLASS': 'sloth.api.backends.Scopes'
}

DEFAULT_FROM_EMAIL = 'noreply@mydomain.com'
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'mydomain.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = 'noreply@mydomain.com>'
EMAIL_HOST_PASSWORD = '*****'
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

DEFAULT_PASSWORD = lambda user: '123'
FORCE_PASSWORD_DEFINITION = False
OAUTH2_AUTHENTICATORS = {
    'APP': {
        'TEXT': 'Acessar com App',
        'LOGO': None,
        'REDIRECT_URI': 'http://localhost:8000/app/login/',
        'CLIENTE_ID': None,
        'CLIENT_SECRET': None,
        'AUTHORIZE_URL': None,
        'ACCESS_TOKEN_URL': None,
        'USER_DATA_URL': None,
        'USER_AUTO_CREATE': False,
        'USER_DATA': {
            'USERNAME': 'username',
            'EMAIL': 'email',
            'FIRST_NAME': None,
            'LAST_NAME': None
        }
    }
}

if bool(os.environ.get('USE_REDIS')):
    REDIS_HOST = os.environ.get('REDIS_HOST', 'redis')
    REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
    REDIS_PASSWORD = os.environ.get('REDIS_PASSWORD', None)
    SESSION_ENGINE = 'django.contrib.sessions.backends.cache'
    SESSION_CACHE_ALIAS = 'default'
    CACHES = {
        "default": {
            "BACKEND": "django_redis.cache.RedisCache",
            "LOCATION": "redis://{}:{}/1".format(REDIS_HOST, REDIS_PORT),
            "OPTIONS": {
                "CLIENT_CLASS": "django_redis.client.DefaultClient",
                "PASSWORD": REDIS_PASSWORD
            }
        }
    }

if bool(os.environ.get('USE_POSTGRES')):
    DATABASES['default']['ENGINE'] = 'django.db.backends.postgresql_psycopg2'
    DATABASES['default']['NAME'] = os.environ.get('DATABASE_NAME', 'database')
    DATABASES['default']['USER'] = os.environ.get('DATABASE_USER', 'postgres')
    DATABASES['default']['PASSWORD'] = os.environ.get('DATABASE_PASSWORD', 'password')
    DATABASES['default']['HOST'] = os.environ.get('DATABASE_HOST', 'postgres')
    DATABASES['default']['PORT'] = os.environ.get('DATABASE_PORT', '5432')
