from flask import Blueprint, request, jsonify, make_response
from utils.extensions import db
from models.Usuarios import Usuarios
from schemas.Usuario_schema import usuario_schema, usuarios_schema
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token

usuarios_bp = Blueprint("Usuarios", __name__)

# Create
@usuarios_bp.route('/usuarios', methods=['POST'])
def create_usuario():
    data = request.get_json()
    hashed_password = Bcrypt().generate_password_hash(data['password_hash']).decode('utf-8')
    new_usuario = Usuarios(
        username=data['username'],
        password_hash=hashed_password,
        nombre=data['nombre'],
        apellido=data['apellido'],
        email=data['email'],
        celular=data['celular']
    )

    db.session.add(new_usuario)
    db.session.commit()
    return usuario_schema.dump(new_usuario), 201

# Read
@usuarios_bp.route('/usuarios', methods=['GET'])
def get_usuarios():
    usuarios = Usuarios.query.all()
    return usuarios_schema.dump(usuarios), 200

# Read por username
@usuarios_bp.route('/usuarios/<string:username>', methods=['GET'])
def get_usuario(username):
    usuario = Usuarios.query.filter_by(username=username).first_or_404()
    return usuario_schema.dump(usuario), 200

# Update 
@usuarios_bp.route('/usuarios/<string:username>', methods=['PUT'])
def update_usuario(username):
    usuario = Usuarios.query.filter_by(username=username).first_or_404()
    data = request.get_json()

    usuario.username = data.get('username', usuario.username)
    usuario.password_hash = data.get('password_hash', usuario.password_hash)
    usuario.nombre = data.get('nombre', usuario.nombre)
    usuario.apellido = data.get('apellido', usuario.apellido)
    usuario.email = data.get('email', usuario.email)
    usuario.celular = data.get('celular', usuario.celular)

    db.session.commit()
    return usuario_schema.dump(usuario), 200

# Delete
@usuarios_bp.route('/usuarios/<string:username>', methods=['DELETE'])
def delete_usuario(username):
    usuario = Usuarios.query.filter_by(username=username).first_or_404()
    db.session.delete(usuario)
    db.session.commit()
    return '', 204

#Login
@usuarios_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    username = data.get("username")
    password_hash = data.get("password_hash")

    if not all([username, password_hash]):
        return jsonify({"mensaje": "Todos los campos son requeridos", "status": "error"}), 400

    usuario = Usuarios.query.filter_by(username=username).first()
    if usuario and Bcrypt().check_password_hash(usuario.password_hash, password_hash):
        access_token = create_access_token(identity={'id_usuario': usuario.id_usuario, 'username': usuario.username})
        return jsonify({"mensaje": "Login exitoso", "status": 1, "access_token": access_token}), 200
    else:
        return jsonify({"mensaje": "Credenciales incorrectas", "status": 0}), 401