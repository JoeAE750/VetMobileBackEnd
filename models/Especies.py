from utils.extensions import db

class Especies(db.Model):
    __tablename__ = "Especies"
    id_especie = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))

    def __init__(self, nombre):
        self.nombre = nombre
