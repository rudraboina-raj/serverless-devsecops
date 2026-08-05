from flask import Flask

from applications.payment_service.app.api.health import health_bp
from applications.payment_service.app.api.payment import payment_bp
from applications.payment_service.app.exceptions.handlers import register_error_handlers


def create_app():

    app = Flask(__name__)

    app.register_blueprint(health_bp)

    app.register_blueprint(payment_bp)

    register_error_handlers(app)

    return app


app = create_app()


if __name__ == "__main__":

    app.run(host="0.0.0.0", port=8080, debug=False)
