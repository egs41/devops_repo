output "cluster_endpoint" {
  description = "Endpoint for EKS control plane"
  value       = aws_eks_cluster.main.endpoint
}

output "kubectl_config" {
  description = "kubectl config command"
  value       = "aws eks --region ${var.region} update-kubeconfig --name ${var.cluster_name}"
}

output "ecr_repository_url" {
  description = "ECR repository URL"
  value       = aws_ecr_repository.app_repo.repository_url
}

output "aws_account_id" {
  description = "AWS Account ID"
  value       = data.aws_caller_identity.current.account_id
}

output "argocd_server_info" {
  description = "Argo CD server information"
  value       = "kubectl get svc -n argocd argocd-server"
}