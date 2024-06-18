from flask import Blueprint, jsonify, request

order_bp = Blueprint('order', __name__, url_prefix='/orders')

@order_bp.route('/', methods=['GET'])
def get_orders():
    # Logic to get orders
    return jsonify({"message": "List of orders"})

@order_bp.route('/<int:order_id>', methods=['GET'])
def get_order(order_id):
    # Logic to get a specific order by ID
    return jsonify({"message": f"Order {order_id}"})

@order_bp.route('/', methods=['POST'])
def create_order():
    # Logic to create a new order
    data = request.get_json()
    return jsonify({"message": "Order created", "data": data})
