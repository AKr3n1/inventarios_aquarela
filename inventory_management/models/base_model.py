"""
Define una clase base para todos los modelos,
proporcionando funcionalidad común como la conexión a la base de datos.
"""

import sqlite3
from config.settings import DATABASE_URL

class BaseModel:
    """
    proporciona métodos comunes para la conexión a la base de datos 
    y la ejecución de consultas SQL.
    """
    def __init__(self, db_path=DATABASE_URL):
        self.db_path = db_path

    def connect(self):
        """
        Establece una conexión con la base de datos.
        """
        return sqlite3.connect(self.db_path)

    def execute_query(self, query, params=()):
        """
        Ejecuta una consulta SQL que modifica la base de datos
        """
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            conn.commit()
            return cursor

    def fetch_all(self, query, params=()):
        """
        Ejecuta una consulta SQL que recupera datos de la base de datos
        """
        with self.connect() as conn:
            cursor = conn.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
