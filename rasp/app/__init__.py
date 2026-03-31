from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_jwt_extended import JWTManager
from flask_bcrypt import Bcrypt
from flask_migrate import Migrate
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

db = SQLAlchemy()
jwt = JWTManager()
bcrypt = Bcrypt()
migrate = Migrate()


def create_app():
    app = Flask(__name__, static_folder="static")

    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "dev-secret-key")
    app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET_KEY", "dev-jwt-key")
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("DATABASE_URL", "sqlite:///data.db")
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    CORS(app)

    db.init_app(app)
    jwt.init_app(app)
    bcrypt.init_app(app)
    migrate.init_app(app, db)

    from app.routes.auth_routes import auth_bp
    from app.routes.data_routes import data_bp

    app.register_blueprint(auth_bp, url_prefix="/auth")
    app.register_blueprint(data_bp, url_prefix="/data")

    @app.route("/")
    def index():
        return app.send_static_file("index.html")

    @app.errorhandler(404)
    def not_found(e):
        return jsonify({"error": "Recurso não encontrado."}), 404

    @app.errorhandler(405)
    def method_not_allowed(e):
        return jsonify({"error": "Método não permitido."}), 405

    @app.errorhandler(500)
    def internal_error(e):
        return jsonify({"error": "Erro interno do servidor."}), 500

    with app.app_context():
        db.create_all()

    return app
