from flask import Blueprint

from shared.core.settings import Settings

health_bp = Blueprint("health", __name__)


@health_bp.route("/health", methods=["GET"])
def health():

    return {
        "project": Settings.PROJECT_NAME,
        "service": "product-service",
        "status": "UP",
        "version": Settings.APP_VERSION,
    }, 200