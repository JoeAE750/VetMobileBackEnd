from flask import Blueprint, request, jsonify
from utils.extensions import db
from models.Citas import Citas
from schemas.Cita_schema import cita_schema, citas_schema

citas_bp = Blueprint("Citas", __name__)

# Create
@citas_bp.route('/citas', methods=['POST'])
def create_cita():
    data = request.get_json()
    new_cita = Citas(
        id_mascota=data['id_mascota'],
        id_veterinario=data['id_veterinario'],
        fecha_cita=data['fecha_cita'],
        razon=data['razon'],
        id_estado=data['id_estado'],
        id_servicio=data['id_servicio'],
        id_usuario=data['id_usuario']
    )
    db.session.add(new_cita)
    db.session.commit()
    return cita_schema.dump(new_cita), 201

# Read
@citas_bp.route('/citas', methods=['GET'])
def get_citas():
    citas = Citas.query.all()
    return citas_schema.dump(citas), 200

# Read by ID
@citas_bp.route('/citas/<int:id_cita>', methods=['GET'])
def get_cita(id_cita):
    cita = Citas.query.get_or_404(id_cita)
    return cita_schema.dump(cita), 200

#Read by ID de Usuario
@citas_bp.route('/citas/usuario/<int:id_usuario>', methods=['GET'])
def get_cita_usuario(id_usuario):
    citas = Citas.query.filter_by(id_usuario=id_usuario).all()
    return citas_schema.dump(citas)

# Update
@citas_bp.route('/citas/<int:id_cita>', methods=['PUT'])
def update_cita(id_cita):
    cita = Citas.query.get_or_404(id_cita)
    data = request.get_json()

    cita.id_mascota = data.get('id_mascota', cita.id_mascota)
    cita.id_veterinario = data.get('id_veterinario', cita.id_veterinario)
    cita.fecha_cita = data.get('fecha_cita', cita.fecha_cita)
    cita.razon = data.get('razon', cita.razon)
    cita.id_estado = data.get('id_estado', cita.id_estado)
    cita.id_servicio = data.get('id_servicio', cita.id_servicio)

    db.session.commit()
    return cita_schema.dump(cita), 200

# Delete
@citas_bp.route('/citas/<int:id_cita>', methods=['DELETE'])
def delete_cita(id_cita):
    cita = Citas.query.get_or_404(id_cita)
    db.session.delete(cita)
    db.session.commit()
    return jsonify({"message": f"Cita con id {id_cita} ha sido eliminada."}), 200
