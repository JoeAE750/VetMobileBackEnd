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
    fecha_registro = db.Column(db.Date)

    def __init__(self, username, password_hash, nombre, apellido, email, celular, fecha_registro):
        self.username = username
        self.password_hash = password_hash
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.celular = celular
        self.fecha_registro = fecha_registro