from utils.extensions import db

class Tipo_Servicios(db.Model):
    __tablename__ = "Tipo_Servicios"
    id_servicio = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50), nullable=False)

    def __init__(self, nombre):
        self.nombre = nombre