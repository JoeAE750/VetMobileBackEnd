from utils.extensions import ma
from models.DetalleBoleta import DetalleBoleta

class Detalle_boleta_schema(ma.SQLAlchemySchema):
    class Meta:
        model = DetalleBoleta
        fields = ('id_detalle', 'id_boleta', 'id_producto', 'cantidad', 'subtotal')

detalle_boleta_schema = Detalle_boleta_schema()
detalles_boleta_schema = Detalle_boleta_schema(many=True)
