from utils.extensions import ma
from models.Estado_cita import Estado_cita

class EstadoCita_schema(ma.SQLAlchemySchema):
    class Meta:
        model = Estado_cita
        fields = ('id_estado', 'nombre')

estado_cita_schema = EstadoCita_schema()
estados_cita_schema = EstadoCita_schema(many=True)
