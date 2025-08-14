import os
from pathlib import Path

from decouple import config
import pymysql

pymysql.install_as_MySQLdb()

BASE_DIR = Path(__file__).resolve().parent.parent
ENVIRONMENT = config("ENVIRONMENT", cast=str, default="development")
DATABASE = config("DATABASE", cast=str, default=None)
SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", default=False, cast=bool)
ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS", cast=lambda v: [s.strip() for s in v.split(",")]
)

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "website.apps.WebsiteConfig",
    "compressor",
    "rest_framework",
    "storages",
    "widget_tweaks",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail",
    "modelcluster",
    "taggit",
    "wagtailmetadata",
    "wagtail_modeladmin",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "wagtail.contrib.redirects.middleware.RedirectMiddleware",
]

ROOT_URLCONF = "www_fortkentoc_org.urls"

if DATABASE == "MYSQL" or ENVIRONMENT == "production":
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.mysql",
            "NAME": config("MYSQL_DB"),
            "USER": config("MYSQL_USER"),
            "PASSWORD": config("MYSQL_PASSWORD"),
            "HOST": config("MYSQL_HOST"),
            "PORT": config("MYSQL_PORT"),
        }
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }


TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]


WSGI_APPLICATION = "www_fortkentoc_org.wsgi.application"

AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

LANGUAGE_CODE = "en-us"

TIME_ZONE = "America/New_York"

USE_I18N = True

USE_TZ = True

if ENVIRONMENT == "production":
    AWS_STORAGE_BUCKET_NAME = "cdn.fortkentoc.org"
    AWS_CLOUDFRONT_DOMAIN = "cdn.fortkentoc.org"
    AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")

    AWS_PUBLIC_MEDIA_LOCATION = "media"
    AWS_PRIVATE_MEDIA_LOCATION = "private-media"
    MEDIA_ROOT = "/%s/" % AWS_PUBLIC_MEDIA_LOCATION
    MEDIA_URL = "//%s/%s/" % (AWS_CLOUDFRONT_DOMAIN, AWS_PUBLIC_MEDIA_LOCATION)
    STORAGES = {
        "default": {
            "BACKEND": "www_fortkentoc_org.storage_backends.PublicMediaStorage",
        },
        "staticfiles": {
            "BACKEND": "www_fortkentoc_org.storage_backends.StaticStorage",
        },
    }

    STATICFILES_LOCATION = "static"
    STATIC_ROOT = "/%s/" % STATICFILES_LOCATION
    STATIC_URL = "//%s/%s/" % (AWS_CLOUDFRONT_DOMAIN, STATICFILES_LOCATION)
else:
    STATIC_URL = "static/"
    MEDIA_URL = "media/"
    MEDIA_ROOT = BASE_DIR / "media"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATICFILES_FINDERS = [
    "compressor.finders.CompressorFinder",
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]


DATA_UPLOAD_MAX_NUMBER_FIELDS = 10_000

COMPRESS_ROOT = BASE_DIR / "static"
COMPRESS_ENABLED = False

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/login/"

WAGTAIL_SITE_NAME = "Fort Kent Outdoor Center"
WAGTAILADMIN_BASE_URL = config("BASE_URL")
BASE_URL = config("BASE_URL")
WAGTAILDOCS_EXTENSIONS = ["pdf"]
