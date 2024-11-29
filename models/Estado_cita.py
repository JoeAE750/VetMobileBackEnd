from utils.extensions import db

class Estado_cita(db.Model):
    __tablename__ = "Estado_cita"
    id_estado = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(20), nullable=False)

    def __init__(self, nombre):
        self.nombre = nombre