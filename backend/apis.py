from pymongo import MongoClient
from bson import ObjectId 
import os
from pymongo import MongoClient

# Connect to MongoDB
mongodb_uri = os.getenv('MONGODB_URI')
client = MongoClient(mongodb_uri)
db = client['e-commerce']
products_collection = db['products']
# Create a new product
def create_product(product_data):
    print(product_data)
    if not all(key in product_data for key in ['name', 'description', 'price', 'category']):
        return None, 'Missing required fields'
    # product_data['_id'] = str(product_data['_id'])  # Generate a unique ID
    result = products_collection.insert_one(product_data)
    return product_data, None

# Read (get) a product by ID
def get_product(product_id):
    product = products_collection.find_one({'_id': ObjectId(product_id)})
    return product

# Read (get) all products
def get_all_products():
    products = products_collection.find()
    products_list = []
    for item in products:
        item['_id'] = str(item['_id'])
        products_list.append(item)
    return list(products_list)

# Update a product
def update_product(product_id, update_data):
    if not products_collection.find_one({'_id': ObjectId(product_id)}):
        return 0, 'Product not found'
    result = products_collection.update_one({'_id': ObjectId(product_id)}, {'$set': update_data})
    return result.modified_count

# Delete a product
def delete_product(product_id):
    result = products_collection.delete_one({'_id': ObjectId(product_id)})
    if result.deleted_count == 0:
        return 0, 'Product not found'
    return result.deleted_count
