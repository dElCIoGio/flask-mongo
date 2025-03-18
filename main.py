from flask import Flask, jsonify, Response

from app.api.v1.route import router as v1_router
from app.middleware.ResponseMiddleware import after_request

app = Flask(__name__)

app.before_request(after_request)

app.register_blueprint(v1_router)


@app.errorhandler(Exception)
def handle_exception(error: Exception) -> Response:
    response_data = {
        "status": 500,
        "success": False,
        "error": {
            "code": 500,
            "message": str(error)
        }
    }
    return jsonify(response_data), 500

@app.route('/health')
def home():
    return jsonify({
        "data": "healthy"
    })