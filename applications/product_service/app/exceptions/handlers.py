from flask import jsonify
from marshmallow import ValidationError


def register_error_handlers(app):

    @app.errorhandler(ValidationError)
    def handle_validation_error(error):

        return jsonify({"errors": error.messages}), 400

    @app.errorhandler(ValueError)
    def handle_value_error(error):

        return jsonify({"error": str(error)}), 400

    @app.errorhandler(Exception)
    def handle_exception(error):

        return jsonify({"error": "Internal Server Error", "details": str(error)}), 500
