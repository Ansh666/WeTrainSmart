"""
WSGI config for WeTrainSmart project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
from django.contrib.auth.handlers.modwsgi import check_password, groups_for_user
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WeTrainSmart.settings')
from django.core.handlers.wsgi import WSGIHandler
application = get_wsgi_application()
