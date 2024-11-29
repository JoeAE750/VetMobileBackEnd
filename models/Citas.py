from utils.extensions import db
from sqlalchemy import DateTime

class Citas(db.Model):
    __tablename__ = "Citas"
    id_cita = db.Column(db.Integer, primary_key=True)
    id_mascota = db.Column(db.Integer, db.ForeignKey('Mascotas.id_mascota'),nullable=False)
    id_veterinario = db.Column(db.Integer, db.ForeignKey('Veterinarios.id_veterinario'),nullable=False)
    fecha_cita = db.Column(DateTime(timezone=False))
    razon = db.Column(db.String(255))
    id_estado = db.Column(db.Integer, db.ForeignKey('Estado_cita.id_estado'),nullable=False)
    id_servicio = db.Column(db.Integer, db.ForeignKey('Tipo_Servicios.id_servicio'),nullable=False)
    id_usuario = db.Column(db.Integer, db.ForeignKey('Usuarios.id_usuario'), nullable=False)

    def __init__(self,id_mascota,id_veterinario,fecha_cita,razon,id_estado,id_servicio,id_usuario):
        self.id_mascota=id_mascota
        self.id_veterinario=id_veterinario
        self.razon=razon
        self.id_estado=id_estado
        self.id_servicio=id_servicio
        self.id_usuario=id_usuario
        self.fecha_cita=fecha_cita