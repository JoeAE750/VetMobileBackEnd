from flask import Blueprint, request, jsonify, make_response
from utils.extensions import db
from models.Mascotas import Mascotas
from schemas.Mascota_schema import mascota_schema, mascotas_schema

mascotas_bp = Blueprint("Mascotas", __name__)

#Create
@mascotas_bp.route('/mascotas', methods=['POST'])
def create_mascota():
    data = request.get_json()
    new_mascota = Mascotas(
        id_usuario = data['id_usuario'],
        nombre = data['nombre'],
        especie = data['especie'],
        raza = data['raza'],
        edad = data['edad'],
        peso = data['peso'],
        genero = data['genero']
    )
        
        
    db.session.add(new_mascota)
    db.session.commit()
    return mascota_schema.dump(new_mascota),201

# Read
@mascotas_bp.route('/mascotas', methods=['GET'])
def get_mascotas():
    mascotas = Mascotas.query.all()
    return mascotas_schema.dump(mascotas), 200

# Read mascotas por id del dueño
@mascotas_bp.route('/mascotas/usuario', methods=['GET'])
def get_mascotas_usuario():
    id_usuario = request.args.get('id_usuario')
    mascotas = Mascotas.query.filter_by(id_usuario=id_usuario).all()
    return mascotas_schema.dump(mascotas), 200

# Read mascotas por id del dueño y nombre de mascota
@mascotas_bp.route('/mascota', methods=['GET'])
def get_mascota_usuario():
    id_usuario = request.args.get('id_usuario')
    nombre = request.args.get('nombre')
    mascota = Mascotas.query.filter_by(id_usuario=id_usuario, nombre=nombre).first_or_404()
    return mascota_schema.dump(mascota), 200

# Update Mascota by id_mascota
@mascotas_bp.route('/mascotas/<int:id_mascota>', methods=['PUT'])
def update_mascota(id_mascota):
    mascota = Mascotas.query.get_or_404(id_mascota)

    data = request.get_json()
    
    # Update fields, ensuring the required fields are present
    mascota.nombre = data.get('nombre', mascota.nombre)
    mascota.especie = data.get('especie', mascota.especie)
    mascota.raza = data.get('raza', mascota.raza)
    mascota.edad = data.get('edad', mascota.edad)
    mascota.peso = data.get('peso', mascota.peso)
    mascota.genero = data.get('genero', mascota.genero)
    
    db.session.commit()

    return mascota_schema.dump(mascota), 200

# Delete Mascota by id_mascota
@mascotas_bp.route('/mascotas/<int:id_mascota>', methods=['DELETE'])
def delete_mascota(id_mascota):
    mascota = Mascotas.query.get_or_404(id_mascota)
    
    db.session.delete(mascota)
    db.session.commit()
    
    return jsonify({"message": f"Mascota con id {id_mascota} ha sido eliminada."}), 200