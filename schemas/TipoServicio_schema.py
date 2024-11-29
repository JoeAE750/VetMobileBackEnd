from utils.extensions import ma
from models.Tipo_Servicios import Tipo_Servicios

class TipoServicioSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Tipo_Servicios
        fields = ('id_servicio', 'nombre')

tipo_servicio_schema = TipoServicioSchema()
tipos_servicio_schema = TipoServicioSchema(many=True)
