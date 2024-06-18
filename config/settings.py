"""
Configuraciones generales para el proyecto
"""
import os
from dotenv import load_dotenv

# Cargar variables de entorno desde el archivo .env
load_dotenv()

# Directorio base del proyecto
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Configuración de la base de datos
DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'data', 'inventory.db')}"

# Configuración de la aplicación
APP = {
    'name': 'Sistema de control de inventarios Aquarela',
    'version': '1.0.0',
    'debug': True,
    'secret_key': os.getenv('secret_key')
}
