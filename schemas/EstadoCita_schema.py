from utils.extensions import ma
from models.EstadoCita import EstadoCita

class EstadoCita_schema(ma.SQLAlchemySchema):
    class Meta:
        model = EstadoCita
        fields = ('id_estado', 'nombre')

estado_cita_schema = EstadoCita_schema()
estados_cita_schema = EstadoCita_schema(many=True)
