"""
ASGI config for logger_pro project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
from pathlib import Path
BASE_DIR = Path(__file__).resolve().parent.parent

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'logger_pro.settings')

application = get_asgi_application()


LOGGING = {
    "version": 1,
    'loggers':{
        'api':{
            'handlers':['file'],
            'level':'INFO'
        }
    },
    'handlers': {
            "file": {
                "level": "INFO",
                "class": "logging.FileHandler",
                "filename": BASE_DIR/'mylog.log',
                'formatter':'simple',
        },
    },
    'formatters': {
        "simple": {
            "format": "{levelname} {asctime} {message}",
            "style": "{",
        },
    }
}