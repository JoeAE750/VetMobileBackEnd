from utils.extensions import ma
from models.CategoriaProductos import CategoriaProductos

class CategoriaProductoSchema(ma.SQLAlchemySchema):
    class Meta:
        model = CategoriaProductos
        fields = ('id_categoria', 'nombre')

categoria_producto_schema = CategoriaProductoSchema()
categorias_producto_schema = CategoriaProductoSchema(many=True)