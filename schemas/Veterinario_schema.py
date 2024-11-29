from utils.extensions import ma
from models.Veterinarios import Veterinarios

class Veterinario_schema(ma.SQLAlchemySchema):
    class Meta:
        model = Veterinarios
        fields = ('id_veterinario', 'nombre', 'especializacion')

veterinario_schema = Veterinario_schema()
veterinarios_schema = Veterinario_schema(many=True)
