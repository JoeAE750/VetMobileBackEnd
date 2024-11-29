from flask import Blueprint, request, jsonify
from utils.extensions import db
from models.Tipo_Servicios import Tipo_Servicios
from schemas.TipoServicio_schema import tipo_servicio_schema, tipos_servicio_schema

tipo_servicio_bp = Blueprint("TipoServicios", __name__)

# Create
@tipo_servicio_bp.route('/tipo_servicio', methods=['POST'])
def create_tipo_servicio():
    data = request.get_json()
    new_tipo_servicio = Tipo_Servicios(nombre=data['nombre'])
    db.session.add(new_tipo_servicio)
    db.session.commit()
    return tipo_servicio_schema.dump(new_tipo_servicio), 201

# Read all
@tipo_servicio_bp.route('/tipo_servicio', methods=['GET'])
def get_tipos_servicio():
    tipos_servicio = Tipo_Servicios.query.all()
    return tipos_servicio_schema.dump(tipos_servicio), 200

# Read by ID
@tipo_servicio_bp.route('/tipo_servicio/<int:id_servicio>', methods=['GET'])
def get_tipo_servicio(id_servicio):
    tipo_servicio = Tipo_Servicios.query.get_or_404(id_servicio)
    return tipo_servicio_schema.dump(tipo_servicio), 200

# Update
@tipo_servicio_bp.route('/tipo_servicio/<int:id_servicio>', methods=['PUT'])
def update_tipo_servicio(id_servicio):
    tipo_servicio = Tipo_Servicios.query.get_or_404(id_servicio)
    data = request.get_json()
    tipo_servicio.nombre = data.get('nombre', tipo_servicio.nombre)
    db.session.commit()
    return tipo_servicio_schema.dump(tipo_servicio), 200

# Delete
@tipo_servicio_bp.route('/tipo_servicio/<int:id_servicio>', methods=['DELETE'])
def delete_tipo_servicio(id_servicio):
    tipo_servicio = Tipo_Servicios.query.get_or_404(id_servicio)
    db.session.delete(tipo_servicio)
    db.session.commit()
    return jsonify({"message": f"Tipo de servicio con id {id_servicio} ha sido eliminado."}), 200
