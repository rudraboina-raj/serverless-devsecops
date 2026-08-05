from flask import jsonify


def register_error_handlers(app):

    @app.errorhandler(Exception)
    def handle_exception(error):

        return jsonify({
            "message": str(error)
        }), 500