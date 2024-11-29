from utils.extensions import db

class CategoriaProductos(db.Model):
    __tablename__ = "Categoria_Productos"
    id_categoria = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def __init__(self, nombre):
        self.nombre = nombre