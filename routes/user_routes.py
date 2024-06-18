from flask import Blueprint, jsonify, request

user_bp = Blueprint('user', __name__, url_prefix='/users')

@user_bp.route('/', methods=['GET'])
def get_users():
    # Logic to get users
    return jsonify({"message": "List of users"})

@user_bp.route('/<int:user_id>', methods=['GET'])
def get_user(user_id):
    return jsonify({"message": f"User {user_id}"})

@user_bp.route('/', methods=['POST'])
def create_user():
    data = request.get_json()
    return jsonify({"message": "User created", "data": data})
