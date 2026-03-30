from flask import Blueprint, request, jsonify
from app.services.auth_service import AuthService

auth_bp = Blueprint("auth", __name__)
auth_service = AuthService()


@auth_bp.route("/register", methods=["POST"])
def register():
    body = request.get_json(silent=True)
    if not body:
        return jsonify({"error": "Corpo da requisição inválido ou ausente."}), 400

    username = body.get("username")
    password = body.get("password")

    try:
        user = auth_service.register(username, password)
        return jsonify({"message": "Usuário criado com sucesso.", "user": user}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@auth_bp.route("/login", methods=["POST"])
def login():
    body = request.get_json(silent=True)
    if not body:
        return jsonify({"error": "Corpo da requisição inválido ou ausente."}), 400

    username = body.get("username")
    password = body.get("password")

    try:
        result = auth_service.login(username, password)
        return jsonify(result), 200
    except PermissionError as e:
        return jsonify({"error": str(e)}), 401