from flask import Flask

from shared.core.settings import Settings
from .logging.logger import configure_logging

from .api.health import health_bp
from .api.order import order_bp

app = Flask(__name__)

logger = configure_logging()

app.register_blueprint(health_bp)
app.register_blueprint(order_bp)


if __name__ == "__main__":

    logger.info("Order Service started successfully.")

    app.run(
        host="0.0.0.0",
        port=Settings.PORT,
        debug=Settings.DEBUG,
    )
