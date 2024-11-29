from utils.extensions import db


class Veterinarios(db.Model):
    __tablename__ = "Veterinarios"
    id_veterinario = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    especializacion = db.Column(db.String(100), nullable=False)
    horainicio = db.Column(db.String(10))
    horafinal = db.Column(db.String(10))

    def __init__(self, nombre, especializacion):
        self.nombre = nombre
        self.especializacion = especializacion