"""
Este módulo configura la conexión a la base de datos
y proporciona una función para obtener sesiones de la base de datos.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///D:/Programacion/inventarios_aquarela/data/test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    """
    Generador de sesiones de la base de datos. Cierra la sesión automáticamente al finalizar.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
