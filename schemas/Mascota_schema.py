from utils.extensions import ma
from models.Mascotas import Mascotas

class MascotaSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Mascotas
        fields = ('id_mascota','id_usuario','nombre','especie','raza','edad','peso','genero')

mascota_schema = MascotaSchema()
mascotas_schema = MascotaSchema(many=True)