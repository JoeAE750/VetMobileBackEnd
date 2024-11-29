from flask import Blueprint, request, jsonify
from utils.extensions import db
from models.Veterinarios import Veterinarios
from schemas.Veterinario_schema import veterinario_schema, veterinarios_schema

veterinarios_bp = Blueprint("Veterinarios", __name__)

# Create
@veterinarios_bp.route('/veterinarios', methods=['POST'])
def create_veterinario():
    data = request.get_json()
    new_veterinario = Veterinarios(
        nombre=data['nombre'],
        especializacion=data['especializacion']
    )
    db.session.add(new_veterinario)
    db.session.commit()
    return veterinario_schema.dump(new_veterinario), 201

# Read
@veterinarios_bp.route('/veterinarios', methods=['GET'])
def get_veterinarios():
    veterinarios = Veterinarios.query.all()
    return veterinarios_schema.dump(veterinarios), 200

# Read by ID
@veterinarios_bp.route('/veterinarios/<int:id_veterinario>', methods=['GET'])
def get_veterinario(id_veterinario):
    veterinario = Veterinarios.query.get_or_404(id_veterinario)
    return veterinario_schema.dump(veterinario), 200

# Update
@veterinarios_bp.route('/veterinarios/<int:id_veterinario>', methods=['PUT'])
def update_veterinario(id_veterinario):
    veterinario = Veterinarios.query.get_or_404(id_veterinario)
    data = request.get_json()

    veterinario.nombre = data.get('nombre', veterinario.nombre)
    veterinario.especializacion = data.get('especializacion', veterinario.especializacion)

    db.session.commit()
    return veterinario_schema.dump(veterinario), 200

# Delete
@veterinarios_bp.route('/veterinarios/<int:id_veterinario>', methods=['DELETE'])
def delete_veterinario(id_veterinario):
    veterinario = Veterinarios.query.get_or_404(id_veterinario)
    db.session.delete(veterinario)
    db.session.commit()
    return jsonify({"message": f"Veterinario con id {id_veterinario} ha sido eliminado."}), 200
