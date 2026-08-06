# -------------------------------------------------------
# GCP Project Configuration
# -------------------------------------------------------

project_id = "serverless-devsecops"

region = "asia-south1"

zone = "asia-south1-a"

# -------------------------------------------------------
# Artifact Registry
# -------------------------------------------------------

repository_id = "serverless-repo"

# -------------------------------------------------------
# Networking
# -------------------------------------------------------

network_name = "serverless-vpc"

subnet_name = "serverless-subnet"

subnet_cidr = "10.10.0.0/24"

# -------------------------------------------------------
# Cloud SQL
# -------------------------------------------------------

instance_name = "postgres-db"

database_name = "appdb"

db_username = "appuser"

# db_password will be passed from GitHub Actions
# TF_VAR_db_password

# -------------------------------------------------------
# Cloud Run - Employee Service
# -------------------------------------------------------

employee_service_name = "employee-service"

employee_service_image = "asia-south1-docker.pkg.dev/serverless-devsecops/serverless-repo/employee-service:v3"

employee_service_account_id = "employee-service-sa"

employee_service_account_name = "Employee Service Account"

# -------------------------------------------------------
# Cloud Run - Product Service
# -------------------------------------------------------

product_service_name = "product-service"

product_service_image = "asia-south1-docker.pkg.dev/serverless-devsecops/serverless-repo/product-service:v2"

# -------------------------------------------------------
# Cloud Run - Order Service
# -------------------------------------------------------

order_service_name = "order-service"

order_service_image = "asia-south1-docker.pkg.dev/serverless-devsecops/serverless-repo/order-service:v1"

# -------------------------------------------------------
# Cloud Run - Payment Service
# -------------------------------------------------------

payment_service_name = "payment-service"

payment_service_image = "asia-south1-docker.pkg.dev/serverless-devsecops/serverless-repo/payment-service:v2"

# -------------------------------------------------------
# Cloud Run - Notification Service
# -------------------------------------------------------

notification_service_name = "notification-service"

notification_service_image = "asia-south1-docker.pkg.dev/serverless-devsecops/serverless-repo/notification-service:v11"

smtp_email = "rudraboina0435@gmail.com"

# smtp_password will be passed from GitHub Actions
# TF_VAR_smtp_password

smtp_server = "smtp.gmail.com"

smtp_port = "587"

# -------------------------------------------------------
# Pub/Sub
# -------------------------------------------------------

employee_events_topic_name = "employee-events"

employee_events_subscription_name = "employee-events-sub"

payment_events_topic_name = "payment-events"

payment_events_subscription_name = "payment-events-sub"