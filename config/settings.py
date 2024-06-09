import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Configuración de la base de datos
DATABASE = {
    'ENGINE': 'sqlite3',
    'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
}

# Configuración del servidor
SERVER = {
    'HOST': '127.0.0.1',
    'PORT': 8000,
    'DEBUG': True,
}

# Configuración de logs
LOGGING_CONFIG = os.path.join(BASE_DIR, 'config/logging.conf')

# Otros parámetros de configuración
ITEMS_PER_PAGE = 10
