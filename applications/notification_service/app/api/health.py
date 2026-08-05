from flask import Blueprint

from shared.core.settings import Settings

health_bp = Blueprint("health", __name__)


@health_bp.get("/health")
def health():

    return {
        "project": Settings.PROJECT_NAME,
        "service": "notification-service",
        "status": "UP",
        "version": Settings.APP_VERSION,
    }, 200
