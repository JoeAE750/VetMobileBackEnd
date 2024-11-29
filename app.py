from flask import Flask
from routes.Usuarios_routes import usuarios_bp
from routes.Mascotas_routes import mascotas_bp
from routes.boletas_routes import boletas_bp
from routes.citas_routes import citas_bp
from routes.detalle_boleta_routes import detalle_boleta_bp
from routes.productos import productos_bp
from routes.Tipo_servicio import tipo_servicio_bp
from routes.veterinarios_routes import veterinarios_bp
from config import DATABASE_CONNECTION_URI
from flask_cors import CORS
from utils.extensions import bcrypt
from utils.extensions import db
from utils.extensions import jwt


app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

app.secret_key = 'sismovilesg1'

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_POOL_SIZE"] = 20
app.config["SQLALCHEMY_POOL_TIMEOUT"] = 30
app.config["SQLALCHEMY_POOL_RECYCLE"] = 1800

# no cache
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0

db.init_app(app)
bcrypt.init_app(app)
jwt.init_app(app)

app.register_blueprint(usuarios_bp)
app.register_blueprint(mascotas_bp)
app.register_blueprint(boletas_bp)
app.register_blueprint(citas_bp)
app.register_blueprint(detalle_boleta_bp)
app.register_blueprint(productos_bp)
app.register_blueprint(tipo_servicio_bp)
app.register_blueprint(veterinarios_bp)

if __name__ == '__main__':
  app.run(port=5000)