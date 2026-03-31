from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required, get_jwt_identity
from marshmallow import ValidationError
from app.services.auth_service import AuthService
from app.schemas.user_schema import RegisterSchema, LoginSchema

auth_bp = Blueprint("auth", __name__)
auth_service = AuthService()

register_schema = RegisterSchema()
login_schema = LoginSchema()


@auth_bp.route("/register", methods=["POST"])
def register():
    body = request.get_json(silent=True)
    if not body:
        return jsonify({"error": "Corpo da requisição inválido ou ausente."}), 400

    try:
        data = register_schema.load(body)
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400

    try:
        user = auth_service.register(data["username"], data["password"])
        return jsonify({"message": "Usuário criado com sucesso.", "user": user}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@auth_bp.route("/login", methods=["POST"])
def login():
    body = request.get_json(silent=True)
    if not body:
        return jsonify({"error": "Corpo da requisição inválido ou ausente."}), 400

    try:
        data = login_schema.load(body)
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400

    try:
        result = auth_service.login(data["username"], data["password"])
        return jsonify(result), 200
    except PermissionError as e:
        return jsonify({"error": str(e)}), 401


@auth_bp.route("/me", methods=["GET"])
@jwt_required()
def me():
    user_id = int(get_jwt_identity())
    user = auth_service.get_by_id(user_id)
    if not user:
        return jsonify({"error": "Usuário não encontrado."}), 404
    return jsonify({"id": user.id, "username": user.username}), 200
