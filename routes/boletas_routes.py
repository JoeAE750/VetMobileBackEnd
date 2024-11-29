from flask import Blueprint, request, jsonify
from utils.extensions import db
from models.Boletas import Boletas
from schemas.Boleta_schema import boleta_schema, boletas_schema

boletas_bp = Blueprint("Boletas", __name__)

# Create
@boletas_bp.route('/boletas', methods=['POST'])
def create_boleta():
    data = request.get_json()
    new_boleta = Boletas(
        id_usuario=data['id_usuario'],
        fecha=data['fecha'],
        tipo=data['tipo'],
        total=data['total']
    )
    db.session.add(new_boleta)
    db.session.commit()
    return boleta_schema.dump(new_boleta), 201

# Read
@boletas_bp.route('/boletas', methods=['GET'])
def get_boletas():
    boletas = Boletas.query.all()
    return boletas_schema.dump(boletas), 200

# Read by ID
@boletas_bp.route('/boletas/<int:id_boleta>', methods=['GET'])
def get_boleta(id_boleta):
    boleta = Boletas.query.get_or_404(id_boleta)
    return boleta_schema.dump(boleta), 200

# Update
@boletas_bp.route('/boletas/<int:id_boleta>', methods=['PUT'])
def update_boleta(id_boleta):
    boleta = Boletas.query.get_or_404(id_boleta)
    data = request.get_json()

    boleta.id_usuario = data.get('id_usuario', boleta.id_usuario)
    boleta.fecha = data.get('fecha', boleta.fecha)
    boleta.tipo = data.get('tipo', boleta.tipo)
    boleta.total = data.get('total', boleta.total)

    db.session.commit()
    return boleta_schema.dump(boleta), 200

# Delete
@boletas_bp.route('/boletas/<int:id_boleta>', methods=['DELETE'])
def delete_boleta(id_boleta):
    boleta = Boletas.query.get_or_404(id_boleta)
    db.session.delete(boleta)
    db.session.commit()
    return jsonify({"message": f"Boleta con id {id_boleta} ha sido eliminada."}), 200
