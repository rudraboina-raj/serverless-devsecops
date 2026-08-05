import os


class Settings:

    PROJECT_NAME = "TechMart Enterprise Platform"

    APP_VERSION = "1.0.0"

    PORT = int(os.getenv("PORT", "8080"))

    DEBUG = os.getenv("DEBUG", "true").lower() == "true"

    # ==========================================================
    # Database
    # ==========================================================

    DB_HOST = os.getenv("DB_HOST", "127.0.0.1")

    DB_PORT = int(os.getenv("DB_PORT", "5432"))

    DB_NAME = os.getenv("DB_NAME", "appdb")

    DB_USERNAME = os.getenv("DB_USERNAME", "appuser")

    DB_PASSWORD = os.getenv("DB_PASSWORD", "Welcome@123")

    # ==========================================================
    # GCP
    # ==========================================================

    PROJECT_ID = os.getenv(
        "PROJECT_ID",
        "serverless-devsecops",
    )

    # ==========================================================
    # Pub/Sub Topics
    # ==========================================================

    EMPLOYEE_EVENTS_TOPIC = os.getenv(
        "EMPLOYEE_EVENTS_TOPIC",
        "employee-events",
    )

    PAYMENT_EVENTS_TOPIC = os.getenv(
        "PAYMENT_EVENTS_TOPIC",
        "payment-events",
    )

    # ==========================================================
    # SMTP
    # ==========================================================

    SMTP_SERVER = os.getenv(
        "SMTP_SERVER",
        "smtp.gmail.com",
    )

    SMTP_PORT = os.getenv(
        "SMTP_PORT",
        "587",
    )

    SMTP_EMAIL = os.getenv(
        "SMTP_EMAIL",
        "",
    )

    SMTP_PASSWORD = os.getenv(
        "SMTP_PASSWORD",
        "",
    )
