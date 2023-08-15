"""
WSGI config for WeTrainSmart project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""
import sys
import os
sys.path.append('/var/www/WeTrainSmart')
sys.path.append('/var/www/WeTrainSmart/env/Lib//site-packages')
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WeTrainSmart.settings')

application = get_wsgi_application()
