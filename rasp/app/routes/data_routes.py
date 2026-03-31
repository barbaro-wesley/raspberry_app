from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from marshmallow import ValidationError
from app.services.data_service import DataService
from app.schemas.data_schema import DataInputSchema

data_bp = Blueprint("data", __name__)
data_service = DataService()

data_input_schema = DataInputSchema()


@data_bp.route("/", methods=["GET"])
@jwt_required()
def get_all():
    entries = data_service.get_all_entries()
    return jsonify(entries), 200


@data_bp.route("/", methods=["POST"])
@jwt_required()
def create():
    body = request.get_json(silent=True)
    if not body:
        return jsonify({"error": "Corpo da requisição inválido ou ausente."}), 400

    try:
        data = data_input_schema.load(body)
    except ValidationError as e:
        return jsonify({"error": e.messages}), 400

    try:
        entry = data_service.add_entry(data["data"])
        return jsonify({"message": "Registro criado com sucesso.", "entry": entry}), 201
    except ValueError as e:
        return jsonify({"error": str(e)}), 400


@data_bp.route("/<int:data_id>", methods=["DELETE"])
@jwt_required()
def delete(data_id):
    try:
        data_service.delete_entry(data_id)
        return jsonify({"message": f"Registro {data_id} removido com sucesso."}), 200
    except LookupError as e:
        return jsonify({"error": str(e)}), 404
