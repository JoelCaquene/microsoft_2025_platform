"""
WSGI config for microsoft_2025_platform project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.2/howto/deployment/wsgi/
"""

import os
from django.core.wsgi import get_wsgi_application
from whitenoise.django import DjangoWhiteNoise  # Importe o WhiteNoise

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'microsoft_2025_platform.settings')

application = get_wsgi_application()
application = DjangoWhiteNoise(application) # Aplica o WhiteNoise à sua aplicação
