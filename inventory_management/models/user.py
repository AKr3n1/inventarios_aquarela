"""
Modelo para la gestion de los usuarios
"""

from inventory_management.models.base_model import BaseModel

class User(BaseModel):
    """
    clase que representa un usuario del sistema.
    """
    def __init__(self, username, password, role, db_path=None):
        """
        Inicializa un nuevo usuario
        """
        super().__init__(db_path)
        self.username = username
        self.password = password
        self.role = role

    def save(self):
        """
        Guarda el usuario en la base de datos
        """
        query = "INSERT INTO users (username, password, role) VALUES (?, ?, ?)"
        self.execute_query(query, (self.username, self.password, self.role))

    def update(self, user_id):
        """
        Actualiza la información del usuario en la base de datos.
        """
        query = "UPDATE users SET username = ?, password = ?, role = ? WHERE id = ?"
        self.execute_query(query, (self.username, self.password, self.role, user_id))

    def delete(self, user_id):
        """
        Elimina el usuario de la base de datos.
        """
        query = "DELETE FROM users WHERE id = ?"
        self.execute_query(query, (user_id,))

    @classmethod
    def get_all(cls):
        """
        Obtiene todos los usuarios de la base de datos.
        """
        base_model = BaseModel()
        query = "SELECT * FROM users"
        return base_model.fetch_all(query)

    @classmethod
    def find_by_id(cls, user_id):
        """
        Encuentra un usuario por su ID.
        """
        base_model = BaseModel()
        query = "SELECT * FROM users WHERE id = ?"
        return base_model.fetch_all(query, (user_id,))
