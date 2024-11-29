from flask import Blueprint, request, jsonify
from utils.extensions import db
from models.DetalleBoleta import DetalleBoleta
from schemas.DetalleBoleta_schema import detalle_boleta_schema, detalles_boleta_schema

detalle_boleta_bp = Blueprint("DetalleBoleta", __name__)

# Create
@detalle_boleta_bp.route('/detalle_boleta', methods=['POST'])
def create_detalle_boleta():
    data = request.get_json()
    new_detalle = DetalleBoleta(
        id_boleta=data['id_boleta'],
        id_producto=data['id_producto'],
        cantidad=data['cantidad'],
        subtotal=data['subtotal']
    )
    db.session.add(new_detalle)
    db.session.commit()
    return detalle_boleta_schema.dump(new_detalle), 201

# Read
@detalle_boleta_bp.route('/detalle_boleta', methods=['GET'])
def get_detalles_boleta():
    detalles = DetalleBoleta.query.all()
    return detalles_boleta_schema.dump(detalles), 200

# Read by ID
@detalle_boleta_bp.route('/detalle_boleta/<int:id_detalle>', methods=['GET'])
def get_detalle_boleta(id_detalle):
    detalle = DetalleBoleta.query.get_or_404(id_detalle)
    return detalle_boleta_schema.dump(detalle), 200

# Update
@detalle_boleta_bp.route('/detalle_boleta/<int:id_detalle>', methods=['PUT'])
def update_detalle_boleta(id_detalle):
    detalle = DetalleBoleta.query.get_or_404(id_detalle)
    data = request.get_json()

    detalle.id_boleta = data.get('id_boleta', detalle.id_boleta)
    detalle.id_producto = data.get('id_producto', detalle.id_producto)
    detalle.cantidad = data.get('cantidad', detalle.cantidad)
    detalle.subtotal = data.get('subtotal', detalle.subtotal)

    db.session.commit()
    return detalle_boleta_schema.dump(detalle), 200

# Delete
@detalle_boleta_bp.route('/detalle_boleta/<int:id_detalle>', methods=['DELETE'])
def delete_detalle_boleta(id_detalle):
    detalle = DetalleBoleta.query.get_or_404(id_detalle)
    db.session.delete(detalle)
    db.session.commit()
    return jsonify({"message": f"Detalle con id {id_detalle} ha sido eliminado."}), 200
