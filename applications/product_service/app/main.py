from flask import Flask

from shared.core.settings import Settings
from shared.database.initialize import initialize_database

from .logging.logger import configure_logging
from .api.health import health_bp
from .api.product import product_bp
from .exceptions.handlers import register_error_handlers

logger = configure_logging()

app = Flask(__name__)

# Create database tables if they do not exist
initialize_database()

register_error_handlers(app)

app.register_blueprint(health_bp)
app.register_blueprint(product_bp)

if __name__ == "__main__":

    logger.info("Starting Product Service...")

    app.run(
        host="0.0.0.0",
        port=Settings.PORT,
        debug=Settings.DEBUG,
    )
