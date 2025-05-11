"""
Configuração ASGI para o projeto HevyAI.

Expõe o aplicativo ASGI como uma variável de módulo chamada ``application``.
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'hevyai.settings')

application = get_asgi_application()