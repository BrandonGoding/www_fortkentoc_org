import os
from pathlib import Path

import pymysql
from decouple import config

ENVIRONMENT = config("ENVIRONMENT", default="development")

pymysql.install_as_MySQLdb()
BASE_DIR = Path(__file__).resolve().parent.parent
SECRET_KEY = config("SECRET_KEY")
DEBUG = config("DEBUG", default=False, cast=bool)
ALLOWED_HOSTS = config(
    "ALLOWED_HOSTS", cast=lambda v: [s.strip() for s in v.split(",")]
)
ALLOWED_CIDR_NETS = config(
    "ALLOWED_CIDR_NETS", cast=lambda v: [s.strip() for s in v.split(",")]
)

INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "membership.apps.MembershipConfig",
    "website.apps.WebsiteConfig",
    "compressor",
    "rest_framework",
    "storages",
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
    "wagtail_modeladmin",
    "widget_tweaks",
]

MIDDLEWARE = [
    "website.middleware.HealthCheckMiddleware",
    "allow_cidr.middleware.AllowCIDRMiddleware",
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

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

STATIC_URL = "static/"

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"

STATICFILES_FINDERS = [
    "compressor.finders.CompressorFinder",
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]


COMPRESS_ROOT = BASE_DIR / "static"
COMPRESS_ENABLED = config("COMPRESS_ENABLED", default=False, cast=bool)
WAGTAIL_SITE_NAME = "The Fort Kent Outdoor Center"
WAGTAILADMIN_BASE_URL = "https://www.fortkentoc.org"
EMAIL_BACKEND = config(
    "EMAIL_BACKEND", default="django.core.mail.backends.console.EmailBackend"
)


if ENVIRONMENT == "production":
    AWS_S3_FILE_OVERWRITE = False
    AWS_STORAGE_BUCKET_NAME = config("AWS_STORAGE_BUCKET_NAME")
    AWS_ACCESS_KEY_ID = config("AWS_ACCESS_KEY_ID")
    AWS_SECRET_ACCESS_KEY = config("AWS_SECRET_ACCESS_KEY")
    AWS_S3_CUSTOM_DOMAIN = "%s" % AWS_STORAGE_BUCKET_NAME
    AWS_S3_OBJECT_PARAMETERS = {
        "CacheControl": "max-age=86400",
    }
    AWS_STATIC_LOCATION = "static"
    AWS_PUBLIC_MEDIA_LOCATION = "media/public"
    DEFAULT_FILE_STORAGE = (
        "www_fortkentoc_org.storage_backends.PublicMediaStorage"
    )
    AWS_PRIVATE_MEDIA_LOCATION = "media/private"
    PRIVATE_FILE_STORAGE = (
        "www_fortkentoc_org.storage_backends.PrivateMediaStorage"
    )
    STATICFILES_STORAGE = "www_fortkentoc_org.storage_backends.StaticStorage"
    EMAIL_HOST = config("EMAIL_HOST", default="")
    EMAIL_HOST_USER = config("EMAIL_HOST_USER", default="")
    EMAIL_HOST_PASSWORD = config("EMAIL_HOST_PASSWORD", default="")
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True
    EMAIL_USE_SSL = False
    SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True

if ENVIRONMENT == "development":
    MEDIA_ROOT = os.path.join(BASE_DIR, "media")
    MEDIA_URL = "/media/"

LOGIN_REDIRECT_URL = "/"
LOGOUT_REDIRECT_URL = "/login/"

CART_SESSION_ID = "fkoc_cart"

if ENVIRONMENT == "development":
    STRIPE_SECRET_KEY = config("STRIPE_SECRET_KEY", default="")
    STRIPE_ADULT_MEMBERSHIP_PRICE = config(
        "DEVELOPMENT_STRIPE_ADULT_MEMBERSHIP_PRICE", default=""
    )
    STRIPE_YOUTH_MEMBERSHIP_PRICE = config(
        "DEVELOPMENT_STRIPE_YOUTH_MEMBERSHIP_PRICE", default=""
    )
    STRIPE_FAMILY_MEMBERSHIP_PRICE = config(
        "DEVELOPMENT_STRIPE_FAMILY_MEMBERSHIP_PRICE", default=""
    )
    STRIPE_UMFK_MEMBERSHIP_PRICE = config(
        "DEVELOPMENT_STRIPE_UMFK_MEMBERSHIP_PRICE", default=""
    )
    BASE_URL = "http://localhost:8000"

if ENVIRONMENT == "production":
    STRIPE_SECRET_KEY = config("STRIPE_SECRET_KEY", default="")
    STRIPE_ADULT_MEMBERSHIP_PRICE = config(
        "PRODUCTION_STRIPE_ADULT_MEMBERSHIP_PRICE", default=""
    )
    STRIPE_YOUTH_MEMBERSHIP_PRICE = config(
        "PRODUCTION_STRIPE_YOUTH_MEMBERSHIP_PRICE", default=""
    )
    STRIPE_FAMILY_MEMBERSHIP_PRICE = config(
        "PRODUCTION_STRIPE_FAMILY_MEMBERSHIP_PRICE", default=""
    )
    STRIPE_UMFK_MEMBERSHIP_PRICE = config(
        "PRODUCTION_STRIPE_UMFK_MEMBERSHIP_PRICE", default=""
    )
    BASE_URL = "https://www.fortkentoc.org"
