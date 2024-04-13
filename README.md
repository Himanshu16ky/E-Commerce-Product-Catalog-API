# **E-Commerce Product Catalog API**

This is a RESTful API built with Python 3, Flask, and MongoDB for managing a simple e-commerce product catalog. The API supports CRUD operations for products and requires authentication using API keys.

## Prerequisites

Before running the application, ensure that you have the following prerequisites installed:

- Python 3.x
- MongoDB

## Installation

1. Clone the repository
2. Navigate to the project directory:
``` 
cd backend 
```
3. Install the required Python packages
4. Set the MongoDB connection URI as an environment variable

Replace the URI with your MongoDB connection string if needed.

## Usage

1. Start the Flask application:
```
python app.py
```
The application will run on `http://localhost:5000` by default.

2. Use a tool like Postman or cURL to interact with the API endpoints. Make sure to include the `X-API-Key` header with the correct API key value in your requests.


## Testing

To run the integration tests, execute the following command:
```
pytest test_api.py
```

Make sure your Flask application is running before running the tests.

## Acknowledgments

- [Flask](https://flask.palletsprojects.com/)
- [PyMongo](https://pymongo.readthedocs.io/)
- [Pytest](https://docs.pytest.org/)