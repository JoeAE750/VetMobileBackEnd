from utils.extensions import db
from sqlalchemy import DateTime

class Boletas(db.Model):
    __tablename__ = "Boletas"
    id_boleta = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('Usuarios.id_usuario'), nullable=False)
    fecha = db.Column(DateTime(timezone=True), nullable=False)
    tipo = db.Column(db.String(20), nullable=False)
    total = db.Column(db.Numeric(10, 2), nullable=False)

    def __init__(self, id_usuario, fecha, tipo, total):
        self.id_usuario = id_usuario
        self.fecha = fecha
        self.tipo = tipo
        self.total = total