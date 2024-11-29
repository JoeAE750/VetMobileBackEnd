from utils.extensions import ma
from models.Productos import Productos

class Producto_schema(ma.SQLAlchemySchema):
    class Meta:
        model = Productos
        fields = ('id_producto', 'nombre', 'descripcion', 'precio', 'stock', 'id_categoria')

producto_schema = Producto_schema()
productos_schema = Producto_schema(many=True)