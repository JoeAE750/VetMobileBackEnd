from utils.extensions import db


class Mascotas(db.Model):
    __tablename__ = "Mascotas"
    id_mascota = db.Column(db.Integer, primary_key=True)
    id_usuario = db.Column(db.Integer, db.ForeignKey('Usuarios.id_usuario'),nullable=False)
    usuario = db.relationship('Usuarios', back_populates='mascotas')
    nombre = db.Column(db.String(100))
    especie = db.Column(db.Integer,db.ForeignKey('Especies.id_especie'),nullable=False)
    raza = db.Column(db.String(50))
    edad = db.Column(db.Integer)
    peso = db.Column(db.Numeric(4,2))
    genero = db.Column(db.String(1))

    def __init__(self, id_usuario, nombre, especie, raza, edad, peso, genero):
        self.id_usuario = id_usuario
        self.nombre = nombre
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.peso = peso
        self.genero = genero