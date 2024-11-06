from utils.extensions import db

class Usuarios(db.Model):
    __tablename__ = "Usuarios"
    id_usuario = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50))
    password_hash = db.Column(db.String(255))
    nombre = db.Column(db.String(50))
    apellido = db.Column(db.String(50))
    email = db.Column(db.String(100))
    celular = db.Column(db.String(15))
    mascotas = db.relationship('Mascotas', back_populates='usuario', cascade='all, delete-orphan')

    def __init__(self, username, password_hash, nombre, apellido, email, celular):
        self.username = username
        self.password_hash = password_hash
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.celular = celular