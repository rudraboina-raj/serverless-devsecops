# -------------------------------------------------------
# GCP Project
# -------------------------------------------------------

variable "project_id" {
  description = "Google Cloud Project ID"
  type        = string
}

variable "region" {
  description = "Deployment region"
  type        = string
}

variable "zone" {
  description = "Deployment zone"
  type        = string
}

# -------------------------------------------------------
# Artifact Registry
# -------------------------------------------------------

variable "repository_id" {
  description = "Artifact Registry repository name"
  type        = string
}

# -------------------------------------------------------
# Network
# -------------------------------------------------------

variable "network_name" {
  description = "VPC name"
  type        = string
}

variable "subnet_name" {
  description = "Subnet name"
  type        = string
}

variable "subnet_cidr" {
  description = "Subnet CIDR"
  type        = string
}

# -------------------------------------------------------
# Cloud SQL
# -------------------------------------------------------

variable "instance_name" {
  description = "Cloud SQL instance name"
  type        = string
}

variable "database_name" {
  description = "Application database name"
  type        = string
}

variable "db_username" {
  description = "Database username"
  type        = string
}

variable "db_password" {
  description = "Database password"
  type        = string
  sensitive   = true
}

# -------------------------------------------------------
# Employee Service
# -------------------------------------------------------

variable "employee_service_name" {
  description = "Employee Cloud Run Service Name"
  type        = string
  default     = "employee-service"
}

variable "employee_service_image" {
  description = "Employee Service Docker Image"
  type        = string
}

variable "employee_service_account_id" {
  description = "Employee Service Account ID"
  type        = string
  default     = "employee-service-sa"
}

variable "employee_service_account_name" {
  description = "Employee Service Account Display Name"
  type        = string
  default     = "Employee Service Account"
}

# -------------------------------------------------------
# Product Service
# -------------------------------------------------------

variable "product_service_name" {
  description = "Product Cloud Run Service Name"
  type        = string
  default     = "product-service"
}

variable "product_service_image" {
  description = "Product Service Docker Image"
  type        = string
}

# -------------------------------------------------------
# Order Service
# -------------------------------------------------------

variable "order_service_name" {
  description = "Order Cloud Run Service Name"
  type        = string
  default     = "order-service"
}

variable "order_service_image" {
  description = "Order Service Docker Image"
  type        = string
}

# -------------------------------------------------------
# Payment Service
# -------------------------------------------------------

variable "payment_service_name" {
  description = "Payment Cloud Run Service Name"
  type        = string
  default     = "payment-service"
}

variable "payment_service_image" {
  description = "Payment Service Docker Image"
  type        = string
}

# -------------------------------------------------------
# Notification Service
# -------------------------------------------------------

variable "notification_service_name" {
  description = "Notification Cloud Run Service Name"
  type        = string
  default     = "notification-service"
}

variable "notification_service_image" {
  description = "Notification Service Docker Image"
  type        = string
}

# -------------------------------------------------------
# SMTP Configuration
# -------------------------------------------------------

variable "smtp_email" {
  description = "SMTP Email"
  type        = string
}

variable "smtp_password" {
  description = "SMTP Password"
  type        = string
  sensitive   = true
}

variable "smtp_server" {
  description = "SMTP Server"
  type        = string
  default     = "smtp.gmail.com"
}

variable "smtp_port" {
  description = "SMTP Port"
  type        = string
  default     = "587"
}

# -------------------------------------------------------
# Employee Pub/Sub
# -------------------------------------------------------

variable "employee_events_topic_name" {
  description = "Employee Events Topic"
  type        = string
}

variable "employee_events_subscription_name" {
  description = "Employee Events Subscription"
  type        = string
}

# -------------------------------------------------------
# Payment Pub/Sub
# -------------------------------------------------------

variable "payment_events_topic_name" {
  description = "Payment Events Topic"
  type        = string
  default     = "payment-events"
}

variable "payment_events_subscription_name" {
  description = "Payment Events Subscription"
  type        = string
  default     = "payment-events-sub"
}