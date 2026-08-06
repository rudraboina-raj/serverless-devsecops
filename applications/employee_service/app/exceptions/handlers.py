from flask import jsonify
from marshmallow import ValidationError
from werkzeug.exceptions import HTTPException


def register_error_handlers(app):

    @app.errorhandler(ValidationError)
    def handle_validation_error(error):
        return jsonify({"errors": error.messages}), 400

    @app.errorhandler(ValueError)
    def handle_value_error(error):
        return jsonify({"error": str(error)}), 400

    @app.errorhandler(HTTPException)
    def handle_http_exception(error):
        return (
            jsonify(
                {
                    "error": error.name,
                    "details": error.description,
                }
            ),
            error.code,
        )

    @app.errorhandler(Exception)
    def handle_exception(error):
        return jsonify({"error": "Internal Server Error"}), 500
