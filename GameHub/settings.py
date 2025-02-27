"""
Django settings for GameHub project.

Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path
import os
# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

X_FRAME_OPTIONS = 'ALLOWALL'
# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-!lat55qv-1sobjvb56n%wj$(24#fy_y)-$g#b2ms&b*q@(*#dn'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
# X_FRAME_OPTIONS = 'SAMEORIGIN'
ALLOWED_HOSTS = ['*']  # Hoặc thêm chính xác domain của ngrok nếu cần



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'accounts',
    'games',
    'assets',
    'payments',
    'rewards',
    'security',
    'rest_framework',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook', 
    'allauth.socialaccount.providers.google',  
]

SITE_ID = 2

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',  
    'allauth.account.auth_backends.AuthenticationBackend',
]




MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'GameHub.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
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

WSGI_APPLICATION = 'GameHub.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # Sử dụng MySQL
        'NAME': 'gamehubplatfrom',          # Tên cơ sở dữ liệu
        'USER': 'root',               # Tên người dùng MySQL
        'PASSWORD': 'root',           # Mật khẩu MySQL
        'HOST': 'localhost',                   # Máy chủ (thường là localhost)
        'PORT': '3306',                        # Cổng MySQL mặc định
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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

AUTH_USER_MODEL = 'accounts.CustomUser'
# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/
os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'assets',"static"),
]
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')  # Thư mục lưu tệp media
# MEDIA_ROOT = BASE_DIR / 'media'
MEDIA_URL = '/media/'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'accounts.CustomUser'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'antran08112005@gmail.com'  # Thay bằng email của bạn
EMAIL_HOST_PASSWORD = 'evrb bxti ehpv rhrc'  # Thay bằng mật khẩu ứng dụng



PAYPAL_CLIENT_ID = "AT1JqbumrDzs0KuL18j2eWp3f1BPOCXm_71aTraIUM1F2mBRFB1n50poZMkVp7gy--pioTARfuSY7UQu"
PAYPAL_CLIENT_SECRET = "EKKhCcUWu4sFITAhBrlicgw9M8OkOFibKsi7dk2fx6JGqeJdJ0S1uwDmVElGGqYHZmcrpi4svMJ5cvJh"
PAYPAL_MODE = "sandbox"  

# Sử dụng Redis làm backend session
SESSION_ENGINE = "django.contrib.sessions.backends.cache"
SESSION_CACHE_ALIAS = "default"

# Cấu hình Redis cache
# settings.py

CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': 'redis://127.0.0.1:6379/1',  # Đảm bảo Redis đang chạy ở cổng này
        'OPTIONS': {
            'CLIENT_CLASS': 'django_redis.client.DefaultClient',
        },
    }
}

# Cấu hình cookie session
SESSION_COOKIE_AGE = 86400  # 24 giờ
SESSION_SAVE_EVERY_REQUEST = True
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = False  # Phải bật nếu dùng HTTPS
SESSION_COOKIE_SAMESITE = None  # Cho phép gửi cookie khi redirect từ PayPal

LOGIN_REDIRECT_URL = '/'

LOGIN_URL = '/errorlogin/' 