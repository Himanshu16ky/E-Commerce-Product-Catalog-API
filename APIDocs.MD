# API Documentation

This API provides endpoints for managing a simple e-commerce product catalog. It supports CRUD operations (Create, Read, Update, Delete) for products and requires authentication using an API key.

## Base URL

The base URL for all API endpoints is:
```
http://localhost:5000
```
## Authentication

This API requires authentication using an API key. The API key must be provided in the `X-API-Key` header for all requests.

**Example Request**
`GET /products ,
X-API-Key: your-api-key`

## Endpoints

### 1. Create a new product

- **Endpoint**: `POST /products`
- **Request Body**:

```json
  {
    "name": "Product Name",
    "description": "Product Description",
    "price": 19.99,
    "category": "Electronics"
  }
```

- **Response**:
```json
{
  "_id": "product_id",
  "name": "Product Name",
  "description": "Product Description",
  "price": 19.99,
  "category": "Electronics"
}
```
- **Error Response**:
```json
{
  "error": "Missing required fields"
}
```
### 2. Get a product by ID:

- **Endpoint**:
`GET /products/<product_id>`
- **Response**:
```json
{
  "_id": "product_id",
  "name": "Product Name",
  "description": "Product Description",
  "price": 19.99,
  "category": "Electronics"
}
```
- **Error Response**:
```json
{
  "error": "Product not found"
}
```
### 3. Get all products

- **Endpoint**: `GET /products`
- **Response Body**:
```json
[
  {
    "_id": "product_id_1",
    "name": "Product Name 1",
    "description": "Product Description 1",
    "price": 19.99,
    "category": "Electronics"
  },
  {
    "_id": "product_id_2",
    "name": "Product Name 2",
    "description": "Product Description 2",
    "price": 29.99,
    "category": "Apparel"
  }
]
```

### 4. Update a product

- **Endpoint**: `PUT /products/<product_id>`
- **Request Body**:
```json
{
  "name": "Updated Product Name",
  "price": 24.99
}
```

- **Response Body**:
```json
{
  "message": "Product updated successfully"
}
```

- **Error Responses**:
```json
{
  "error": "Product not found"
}
```


### 5. Delete a product

- **Endpoint**: `DELETE /products/<product_id>`

- **Response Body**:
```json
{
  "message": "Product deleted successfully"
}
```

- **Error Responses**:
```json
{
  "error": "Product not found"
}
```
