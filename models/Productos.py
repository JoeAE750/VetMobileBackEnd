from utils.extensions import db
from sqlalchemy import Text

class Productos(db.Model):
    __tablename__ = "Productos"
    id_producto = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    descripcion = db.Column(Text, nullable=True)
    precio = db.Column(db.Numeric(10, 2), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    id_categoria = db.Column(db.Integer, db.ForeignKey('Categoria_Productos.id_categoria'), nullable=False)

    def __init__(self, nombre, descripcion, precio, stock, id_categoria):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio
        self.stock = stock
        self.id_categoria = id_categoria