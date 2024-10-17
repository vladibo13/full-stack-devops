from flask import Blueprint, jsonify, request, abort
from .models import User
from .extensions import db

bp = Blueprint('api', __name__, url_prefix='/api')

@bp.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    return jsonify([user.to_dict() for user in users])

@bp.route('/users/<int:id>', methods=['GET'])
def get_user(user_id):
    user = User.query.get_or_404(id)
    return jsonify(user.to_dict())

@bp.route('/users', methods=['POST'])
def create_user():
    data = request.json
    if not data.get('name') or not data.get('email'):
        abort(400, 'Name and Email are required')

    new_user = User(name=data['name'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify(new_user.to_dict()), 201

@bp.route('/users/<int:id>', methods=['PUT'])
def update_user(user_id):
    user = User.query.get_or_404(id)
    data = request.json

    user.name = data.get('name', user.name)
    user.email = data.get('email', user.email)
    db.session.commit()
    return jsonify(user.to_dict())

@bp.route('/users/<int:id>', methods=['DELETE'])
def delete_user(user_id):
    user = User.query.get_or_404(id)
    db.session.delete(user)
    db.session.commit()
    return jsonify({"message": "User deleted"}), 204