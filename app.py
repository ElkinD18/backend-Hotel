from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from models import db
from routes.clients import clients_bp
from routes.reservations import reservations_bp
from routes.rooms import rooms_bp
from routes.users import users_bp
from routes.accounts import accounts_bp
from routes.general_parameters import general_parameters_bp
from routes.invoices import invoices_bp
from routes.financial_records import financial_records_bp
from routes.reports import reports_bp
from flask_jwt_extended import JWTManager
from flasgger import Swagger
def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    CORS(app)  # Habilitar CORS

    db.init_app(app)

    app.config['JWT_SECRET_KEY'] = 'your_jwt_secret_key'  # Cambia esto por una clave secreta segura
    jwt = JWTManager(app)

    app.register_blueprint(users_bp, url_prefix='/api')
    app.register_blueprint(rooms_bp, url_prefix='/api')
    app.register_blueprint(accounts_bp, url_prefix='/api')
    app.register_blueprint(reservations_bp, url_prefix='/api')
    app.register_blueprint(reports_bp, url_prefix='/api')
    app.register_blueprint(invoices_bp, url_prefix='/api')
    app.register_blueprint(financial_records_bp, url_prefix='/api')
    app.register_blueprint(clients_bp, url_prefix='/api')

    swagger = Swagger(app, template_file='docs/swagger.yml')

    @app.route('/')
    def index():
        return jsonify({"message": "Welcome to the Hotel Reservation System API"}), 200

    return app

app = create_app()