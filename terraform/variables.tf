variable "cluster_name" {
  description = "EKS cluster name"
  type        = string
  default     = "user-management-cluster"
}

variable "region" {
  description = "AWS region"
  type        = string
  default     = "ap-northeast-2"
}

variable "ecr_repository_name" {
  description = "ECR repository name"
  type        = string
  default     = "user-management-app"
}