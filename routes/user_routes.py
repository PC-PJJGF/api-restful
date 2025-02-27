from flask import Blueprint, jsonify, request
from models.user_model import User, db

user_bp = Blueprint("users", __name__)

@user_bp.route("/users", methods=["GET"])
def obtener_usuarios():
    users = User.query.all()
    return jsonify([t.serialize() for t in users])

# Crea funciones para POST, PUT, DELETE siguiendo un patrón similar

@user_bp.route("/users", methods=["POST"])
def crear_usuario():
    data = request.json
    user = User(
        titulo=data["titulo"],
        descripcion=data["descripcion"],
        completado=data["completado"],
    )
    db.session.add(user)
    db.session.commit()
    return jsonify(user.serialize()), 201

@user_bp.route("/users/<int:id>", methods=["PUT"])
def actualizar_usuario(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    data = request.json
    user.titulo = data["titulo"]
    user.descripcion = data["descripcion"]
    user.completado = data["completado"]
    db.session.commit()
    return jsonify(user.serialize())

@user_bp.route("/users/<int:id>", methods=["DELETE"])
def eliminar_usuario(id):
    user = User.query.get(id)
    if not user:
        return jsonify({"message": "User not found"}), 404
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"}), 200