terraform {
  backend "gcs" {
    bucket = "tfstate-serverless-devsecops-460587643228"
    prefix = "terraform/state"
  }
}