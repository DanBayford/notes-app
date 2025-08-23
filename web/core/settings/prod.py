import os

from .base import *

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

DEBUG = bool(int(os.environ.get("DEBUG", default=0)))

# 'DJANGO_ALLOWED_HOSTS' should be a single string of hosts with a space between each.
# For example: 'DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]'
ALLOWED_HOSTS = os.environ.get("DJANGO_ALLOWED_HOSTS", "").split(" ")

if ALLOWED_HOSTS == " ":
    raise RuntimeError("Environment variable ALLOWED_HOSTS is not set")

# Where to move static files via collectstatic for production web serving
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")

# Whitenoise static asset server config
MIDDLEWARE.insert(1, "whitenoise.middleware.WhiteNoiseMiddleware")

STORAGES = {
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}
