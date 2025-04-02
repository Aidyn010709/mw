import os
from datetime import timedelta
from pathlib import Path
import environ

BASE_DIR = Path(__file__).resolve().parent.parent

env = environ.Env(
    DEBUG=(bool, True),
    SECRET_KEY=(str, "django-insecure--ex6p^^+5*+ii!-(0a31^e5p1)_8ywkbp$0b+x8-v+" "r630t+@$"),
    CSRF_COOKIE_SECURE=(bool, False),
    SESSION_COOKIE_SECURE=(bool, False),
    SECURE_HSTS_SECONDS=(int, 0),
    SECURE_HSTS_INCLUDE_SUBDOMAINS=(bool, False),
    SECURE_SSL_REDIRECT=(bool, False),
    ALLOWED_HOSTS=(list, ["*", "localhost"]),
    DATABASE_URL=(str, "postgresql://postgres:1@localhost:5432/mw"),
    DATABASE_CONN_MAX_AGE=(int, 600),
    DATABASE_POOL=(bool, True),
    ACCESS_TOKEN_LIFETIME=(int, 12),
    REFRESH_TOKEN_LIFETIME=(int, 60),
    EMAIL_HOST_USER=(str, "sassassas107@gmail.com"),
    EMAIL_HOST_PASSWORD=(str, "lozbgrqaojcaeamx"),
)

CORS_ALLOW_ALL_ORIGINS = True

SECRET_KEY = env("SECRET_KEY")

CSRF_COOKIE_SECURE = env("CSRF_COOKIE_SECURE")
SESSION_COOKIE_SECURE = env("SESSION_COOKIE_SECURE")
SECURE_HSTS_SECONDS = env("SECURE_HSTS_SECONDS")
SECURE_HSTS_INCLUDE_SUBDOMAINS = env("SECURE_HSTS_INCLUDE_SUBDOMAINS")
SECURE_SSL_REDIRECT = env("SECURE_SSL_REDIRECT")

DEBUG = env("DEBUG")

ALLOWED_HOSTS = env("ALLOWED_HOSTS")

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # libraries
    "rest_framework",
    "drf_yasg",
    "django_filters",
    "rest_framework.authtoken",
    "rest_framework_simplejwt",
    "corsheaders",

    "apps.accounts",
    "apps.faculty",
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    "corsheaders.middleware.CorsMiddleware",
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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

AUTH_USER_MODEL = "accounts.CustomUser"
WSGI_APPLICATION = "core.wsgi.application"


db_url_config = env.db_url()
db_url_config["OPTIONS"] = db_url_config.get("OPTIONS", {})
db_url_config["pool"] = env("DATABASE_POOL")
db_url_config["CONN_MAX_AGE"] = env("DATABASE_CONN_MAX_AGE")
DATABASES = {
    "default": db_url_config,
}
LOGIN_REDIRECT_URL = "/"


AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.accounts.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.accounts.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.accounts.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.accounts.password_validation.NumericPasswordValidator',
    },
]

LANGUAGE_CODE = "ru"

TIME_ZONE = "Asia/Bishkek"

USE_I18N = True

USE_TZ = True

DATE_FORMAT = "d.m.Y"
TIME_FORMAT = "H:i:s"
DATETIME_FORMAT = "d.m.Y H:i:s"


STATIC_URL = os.getenv("STATIC_URL", default="static/")

STATICFILES_DIRS = [
    BASE_DIR / os.getenv("STATICFILES_DIRS", default="static")
]

STATIC_ROOT = BASE_DIR / os.getenv("STATIC_ROOT", default="staticfiles")

MEDIA_URL = os.getenv("MEDIA_URL", default="/media/")
MEDIA_ROOT = BASE_DIR / os.getenv("MEDIA_ROOT", default="media")

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.BasicAuthentication",
        "rest_framework.authentication.TokenAuthentication",
    ],
    "DEFAULT_FILTER_BACKENDS": [
        "django_filters.rest_framework.DjangoFilterBackend",
        "rest_framework.filters.SearchFilter"
    ]
}

ACCESS_TOKEN_LIFETIME = env("ACCESS_TOKEN_LIFETIME")
REFRESH_TOKEN_LIFETIME = env("REFRESH_TOKEN_LIFETIME")

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(hours=int(ACCESS_TOKEN_LIFETIME)),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=int(REFRESH_TOKEN_LIFETIME)),
    "ROTATE_REFRESH_TOKENS": True,
    "BLACKLIST_AFTER_ROTATION": True,
    "ALGORITHM": "HS256",
    "SIGNING_KEY": SECRET_KEY,
    "VERIFYING_KEY": None,
    "AUDIENCE": None,
    "ISSUER": None,
    "AUTH_HEADER_TYPES": ("JWT", "Bearer", "Token"),
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "JTI_CLAIM": "jti",
    "SLIDING_TOKEN_REFRESH_EXP_CLAIM": "refresh_exp",
}

SWAGGER_SETTINGS = {
    "SECURITY_DEFINITIONS": {
        "Bearer": {"type": "apiKey", "name": "Authorization", "in": "header"},
        "x-api-key": {"type": "apiKey", "name": "x-api-key", "in": "header"},
    },
    "USE_SESSION_AUTH": False,
}

CELERY_BROKER_URL = 'pyamqp://guest@localhost//'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_PASSWORD = env('EMAIL_HOST_PASSWORD')
EMAIL_HOST_USER = env('EMAIL_HOST_USER')
