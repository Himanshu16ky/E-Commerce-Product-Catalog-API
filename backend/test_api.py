import pytest
import requests
import json

BASE_URL = 'http://localhost:5000'
API_KEY = 'your-api-key'

@pytest.fixture
def client():
    return requests.Session()

@pytest.fixture
def headers():
    return {'X-API-Key': API_KEY}

def test_create_product(client, headers):
    product_data = {
        'name': 'Test Product0000',
        'description': 'This is a test product',
        'price': 19.99,
        'category': 'Electronics'
    }
    response = client.post(f'{BASE_URL}/products', headers=headers, json=product_data)
    assert response.status_code == 200
    assert response.json()['name'] == product_data['name']

def test_get_product(client, headers):
    print(client, headers)
    response = client.get(f'{BASE_URL}/products/test-product-id', headers=headers)
    assert response.status_code == 500

def test_get_all_products(client, headers):
    response = client.get(f'{BASE_URL}/products', headers=headers)
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_update_product(client, headers):
    product_data = {
        'name': 'Updated Test Product',
        'price': 24.99
    }
    response = client.put(f'{BASE_URL}/products/test-product-id', headers=headers, json=product_data)
    assert response.status_code == 500

def test_delete_product(client, headers):
    response = client.delete(f'{BASE_URL}/products/test-product-id', headers=headers)
    assert response.status_code == 500