variable "project_id" {
  type = string
}

variable "region" {
  type = string
}

variable "service_name" {
  type = string
}

variable "image" {
  type = string
}

variable "container_port" {
  type    = number
  default = 8080
}

variable "vpc_connector" {
  type = string
}

variable "service_account" {
  description = "Service Account Email used by Cloud Run"
  type        = string
}

variable "cpu" {
  type    = string
  default = "1"
}

variable "memory" {
  type    = string
  default = "512Mi"
}

variable "min_instances" {
  type    = number
  default = 0
}

variable "max_instances" {
  type    = number
  default = 5
}

# -------------------------------------------------------
# Normal Environment Variables
# -------------------------------------------------------

variable "environment_variables" {

  description = "Plain environment variables"

  type = map(string)

  default = {}

}

# -------------------------------------------------------
# Secret Manager Environment Variables
# -------------------------------------------------------

variable "secret_environment_variables" {

  description = "Environment variables backed by Secret Manager"

  type = map(object({

    secret = string

    version = string

  }))

  default = {}

}