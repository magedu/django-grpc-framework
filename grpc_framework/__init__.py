import django
from .management.commands._utils import get_server

__title__ = 'Django gRPC framework'
__version__ = '1.0.0'
__author__ = 'Comynli'
__license__ = 'Apache-2.0'
__copyright__ = 'Copyright 2020 Magedu Ltd'

# Version synonym
VERSION = __version__

if django.VERSION < (3, 2):
    default_app_config = 'grpc_framework.apps.GrpcFrameworkConfig'

__all__ = ['get_server']
