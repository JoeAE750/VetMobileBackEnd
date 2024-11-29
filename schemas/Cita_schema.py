from utils.extensions import ma
from models.Citas import Citas

class Cita_schema(ma.SQLAlchemySchema):
    class Meta:
        model = Citas
        fields = ('id_cita', 'id_mascota', 'id_veterinario', 'fecha_cita', 'razon', 'id_estado', 'id_servicio')

cita_schema = Cita_schema()
citas_schema = Cita_schema(many=True)
