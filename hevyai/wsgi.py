"""
Configuração WSGI para o projeto HevyAI.

Expõe o aplicativo WSGI como uma variável de módulo chamada ``application``.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hevyai.settings')

application = get_wsgi_application()