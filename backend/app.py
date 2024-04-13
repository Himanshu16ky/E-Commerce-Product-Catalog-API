from flask import Flask, jsonify, request
from pymongo import MongoClient
import uuid
import json
from functools import wraps
from apis import create_product, get_product, get_all_products, update_product, delete_product
import os
from pymongo import MongoClient

app = Flask(__name__)
app.config['API_KEY'] = 'your-api-key'

# Connect to MongoDB
mongodb_uri = os.getenv('MONGODB_URI')
client = MongoClient(mongodb_uri)
db = client['e-commerce']
products_collection = db['products']

# Authentication decorator
def require_api_key(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        api_key = request.headers.get('X-API-Key')
        if api_key != app.config['API_KEY']:
            return jsonify({'error': 'Invalid API key'}), 401
        return func(*args, **kwargs)
    return wrapper


# API endpoints
@app.route('/products', methods=['POST'])
@require_api_key
def create_product_endpoint():
    product_data = request.json
    new_product, error = create_product(product_data)
    if error:
        return jsonify({'error': error}), 400
    product_data['_id'] = str(product_data['_id'])
    return product_data

@app.route('/products/<product_id>', methods=['GET'])
@require_api_key
def get_product_endpoint(product_id):
    product = get_product(product_id)
    if product:
        product['_id']=str(product['_id'])
        return jsonify(product)
    else:
        return jsonify({'error': 'Product not found'}), 404

@app.route('/products', methods=['GET'])
@require_api_key
def get_all_products_endpoint():
    products = get_all_products()
    print(products)
    return jsonify(products)

@app.route('/products/<product_id>', methods=['PUT'])
@require_api_key
def update_product_endpoint(product_id):
    update_data = request.json
    modified_count = update_product(product_id, update_data)
    if modified_count == 1:
        return jsonify({'message': 'Product updated successfully'})
    else:
        return jsonify({'error': 'Product not found'}), 404

@app.route('/products/<product_id>', methods=['DELETE'])
@require_api_key
def delete_product_endpoint(product_id):
    deleted_count = delete_product(product_id)
    if deleted_count == 1:
        return jsonify({'message': 'Product deleted successfully'})
    else:
        return jsonify({'error': 'Product not found'}), 404

if __name__ == '__main__':
    app.run(debug=True)