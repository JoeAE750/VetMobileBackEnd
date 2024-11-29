from utils.extensions import ma
from models.Boletas import Boletas

class Boleta_schema(ma.SQLAlchemySchema):
    class Meta:
        model = Boletas
        fields = ('id_boleta', 'id_usuario', 'fecha', 'tipo', 'total')

boleta_schema = Boleta_schema()
boletas_schema = Boleta_schema(many=True)