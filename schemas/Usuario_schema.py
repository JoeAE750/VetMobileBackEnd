from utils.extensions import ma
from models.Usuarios import Usuarios

class UsuarioSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Usuarios
        fields = ('id_usuario', 'username', 'password_hash', 'nombre', 'apellido', 'email', 'celular', 'fecha_registro')

usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)