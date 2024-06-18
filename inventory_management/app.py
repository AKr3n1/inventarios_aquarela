"""
configura el registro de logs según las especificaciones definidas en 'config/logging.conf'.
"""

import logging
import logging.config
from config.settings import BASE_DIR

logging.config.fileConfig(BASE_DIR + '/config/logging.conf')
logger = logging.getLogger(__name__)

logger.debug('Este es un mensaje de debug')
logger.info('Este es un mensaje informativo')
logger.warning('Este es un mensaje de advertencia')
logger.error('Este es un mensaje de error')
logger.critical('Este es un mensaje crítico')

def main():
    """
    Tu lógica principal de la aplicación puede ir aquí
    """
    logger.info('La aplicación ha iniciado')

if __name__ == '__main__':
    main()
