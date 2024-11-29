from flask import Blueprint, request, jsonify
from utils.extensions import db
from models.Productos import Productos
from schemas.Producto_schema import producto_schema, productos_schema

productos_bp = Blueprint("Productos", __name__)

# Create
@productos_bp.route('/productos', methods=['POST'])
def create_producto():
    data = request.get_json()
    new_producto = Productos(
        nombre=data['nombre'],
        descripcion=data.get('descripcion'),
        precio=data['precio'],
        stock=data['stock'],
        id_categoria=data['id_categoria']
    )
    db.session.add(new_producto)
    db.session.commit()
    return producto_schema.dump(new_producto), 201

# Read
@productos_bp.route('/productos', methods=['GET'])
def get_productos():
    productos = Productos.query.all()
    return productos_schema.dump(productos), 200

# Read by ID
@productos_bp.route('/productos/<int:id_producto>', methods=['GET'])
def get_producto(id_producto):
    producto = Productos.query.get_or_404(id_producto)
    return producto_schema.dump(producto), 200

# Update
@productos_bp.route('/productos/<int:id_producto>', methods=['PUT'])
def update_producto(id_producto):
    producto = Productos.query.get_or_404(id_producto)
    data = request.get_json()

    producto.nombre = data.get('nombre', producto.nombre)
    producto.descripcion = data.get('descripcion', producto.descripcion)
    producto.precio = data.get('precio', producto.precio)
    producto.stock = data.get('stock', producto.stock)
    producto.id_categoria = data.get('id_categoria', producto.id_categoria)

    db.session.commit()
    return producto_schema.dump(producto), 200

# Delete
@productos_bp.route('/productos/<int:id_producto>', methods=['DELETE'])
def delete_producto(id_producto):
    producto = Productos.query.get_or_404(id_producto)
    db.session.delete(producto)
    db.session.commit()
    return jsonify({"message": f"Producto con id {id_producto} ha sido eliminado."}), 200
