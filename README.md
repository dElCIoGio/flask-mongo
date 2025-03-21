# Flask + MongoDB Backend Template

This repository provides a base implementation for a **Flask + MongoDB** backend. It includes structured response handling, middleware, error handling, and a modular approach for adding routes.

## Features

- **Flask-based API** with structured JSON responses
- **Middleware** for request preprocessing and response formatting
- **Global exception handling**
- **MongoDB integration** with minimal setup
- **Modular routes with Blueprints**
- **Asynchronous support for I/O operations**

## Installation

### 1. Clone the repository

```sh
git clone https://github.com/dElCIoGio/flask-mongodb-template.git
cd flask-mongodb-template
```

### 2. Create a virtual environment (Recommended)

```sh
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```

### 3. Install dependencies

```sh
pip install -r requirements.txt
```
This will install all necessary dependencies, including MongoDB-related libraries.

## Running the Application

### 1. Start the Flask server with Uvicorn

```sh
uvicorn app:app --host 0.0.0.0 --port 5000 --reload
```

The server will start at `http://127.0.0.1:5000/`

### 2. Example Request

```sh
curl -X GET http://127.0.0.1:5000/
```

#### Response:

```json
{
    "status": 200,
    "success": true,
    "message": "User created",
    "data": {
        "id": 1,
        "name": "John Doe"
    }
}
```

## Folder Structure

```
/
│-- app.py              # Main Flask application
│-- middleware.py       # Middleware for request/response handling
│-- routes/
│   ├── user_routes.py  # User-related routes
│   ├── product_routes.py # Product-related routes
│-- requirements.txt    # Required dependencies
│-- README.md           # Documentation
```

## Environment Variables

The only required configuration for MongoDB is setting the following environment variables in a `.env` file:

```
MONGO_URI=mongodb://localhost:27017/
MONGO_DATABASE_NAME=mydatabase
```

## MongoDB Integration

No additional setup is required beyond setting the environment variables. The system will automatically connect to MongoDB using the provided values.


## Deployment

Use **Uvicorn** for production deployment:

```sh
uvicorn app:app --host 0.0.0.0 --port 5000
```