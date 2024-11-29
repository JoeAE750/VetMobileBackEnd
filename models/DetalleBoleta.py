from utils.extensions import db

class DetalleBoleta(db.Model):
    __tablename__ = "Detalle_Boleta"
    id_detalle = db.Column(db.Integer, primary_key=True)
    id_boleta = db.Column(db.Integer, db.ForeignKey('Boletas.id_boleta'), nullable=False)
    id_producto = db.Column(db.Integer, db.ForeignKey('Productos.id_producto'), nullable=False)
    cantidad = db.Column(db.Integer, nullable=False)
    subtotal = db.Column(db.Numeric(10, 2), nullable=False)

    def __init__(self, id_boleta, id_producto, cantidad, subtotal):
        self.id_boleta = id_boleta
        self.id_producto = id_producto
        self.cantidad = cantidad
        self.subtotal = subtotal