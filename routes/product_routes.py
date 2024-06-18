from flask import Blueprint, jsonify, request

product_bp = Blueprint('product', __name__, url_prefix='/products')

@product_bp.route('/', methods=['GET'])
def get_products():
    # Logic to get products
    return jsonify({"message": "List of products"})

@product_bp.route('/<int:product_id>', methods=['GET'])
def get_product(product_id):
    # Logic to get a specific product by ID
    return jsonify({"message": f"Product {product_id}"})

@product_bp.route('/', methods=['POST'])
def create_product():
    # Logic to create a new product
    data = request.get_json()
    return jsonify({"message": "Product created", "data": data})
