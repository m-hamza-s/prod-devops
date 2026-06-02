terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region                      = "us-east-1"
  access_key                  = "test"
  secret_key                  = "test"
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true

  endpoints {
    s3  = "http://localhost:4566"
    sqs = "http://localhost:4566"
    iam = "http://localhost:4566"
  }
}

# S3 Bucket
resource "aws_s3_bucket" "devops_bucket" {
  bucket = "prod-devops-demo-bucket"
}

# S3 Bucket Object
resource "aws_s3_object" "devops_file" {
  bucket  = aws_s3_bucket.devops_bucket.id
  key     = "hello.txt"
  content = "Hello from Terraform + LocalStack!"
}

# SQS Queue
resource "aws_sqs_queue" "devops_queue" {
  name = "prod-devops-queue"
}
