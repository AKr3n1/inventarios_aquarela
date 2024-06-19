"""
modelo para la gestion de elementos del inventario.
"""

from inventory_management.models.base_model import BaseModel

class InventoryItem(BaseModel):
    """
    Clase que representa un artículo en el inventario.
    """
    def __init__(self, name, quantity, price, db_path=None):
        """
        Inicializa una nueva instancia de InventoryItem.
        """
        super().__init__(db_path)
        self.name = name
        self.quantity = quantity
        self.price = price

    def save(self):
        """
        Guarda el artículo en la base de datos.
        """
        query = "INSERT INTO inventory (name, quantity, price) VALUES (?, ?, ?)"
        self.execute_query(query, (self.name, self.quantity, self.price))

    def update(self, item_id):
        """
        Actualiza un artículo existente en la base de datos.
        """
        query = "UPDATE inventory SET name = ?, quantity = ?, price = ? WHERE id = ?"
        self.execute_query(query, (self.name, self.quantity, self.price, item_id))

    def delete(self, item_id):
        """
        Elimina un articulo en la base de datos
        """
        query = "DELETE FROM inventory WHERE id = ?"
        self.execute_query(query, (item_id,))

    @classmethod
    def get_all(cls):
        """
        Recupera todos los articulos del inventario
        """
        base_model = BaseModel()
        query = "SELECT * FROM inventory"
        return base_model.fetch_all(query)

    @classmethod
    def find_by_id(cls, item_id):
        """
        Recupera un articulo del inventario por su ID
        """
        base_model = BaseModel()
        query = "SELECT * FROM inventory WHERE id = ?"
        return base_model.fetch_all(query, (item_id,))
