import os
import socket
from .base import *

SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

DEBUG = bool(int(os.environ.get("DEBUG", default=1)))

# 'DJANGO_ALLOWED_HOSTS' should be a single string of hosts with a space between each.
# For example: 'DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 [::1]'
ALLOWED_HOSTS = os.environ.get(
    "DJANGO_ALLOWED_HOSTS", "localhost 127.0.0.1 [::1]"
).split(" ")

INSTALLED_APPS.insert(6, "debug_toolbar")

MIDDLEWARE.insert(1, "debug_toolbar.middleware.DebugToolbarMiddleware")

"""
Required for debug toolbar
Docker container has dynamic IP so cannot be hard coded
https://ranjanmp.medium.com/django-debug-toolbar-not-showing-up-when-using-docker-django-docker-e79585813bc6
"""
hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = (
    [ip[:-1] + "1" for ip in ips]
    + [  # Docker network IP
        "127.0.0.1"
    ]
    + ips
)
