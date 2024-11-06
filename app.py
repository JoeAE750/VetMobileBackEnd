from flask import Flask
from routes.Usuarios_routes import usuarios_bp
from routes.Mascotas_routes import mascotas_bp
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

if __name__ == '__main__':
  app.run(port=5000)