# ECS Deployment Workflow

This workflow builds Docker images and deploys them to AWS ECS based on the branch being pushed to.

## Overview

The workflow consists of two jobs:
1. **Build** - Builds Docker image and pushes to Amazon ECR
2. **Deploy** - Updates ECS service to trigger new deployment

## Environment Setup

### GitHub Environments Required

Create two environments in your repository:
- **Production** (for `main` branch)
- **Staging** (for non-main branches like `stage`)

### Environment Variables

Each environment needs these variables:

| Variable | Description | Example | Default |
|----------|-------------|---------|---------|
| `AWS_REGION` | Target AWS region | `us-east-2` | `us-east-2` |
| `IMAGE_NAME` | Docker image name | `easyerp` | `easyerp` |
| `ECS_CLUSTER_NAME` | ECS cluster name | `EasyERP-Production` | (required) |
| `ECS_SERVICE_NAME` | ECS service name | `EasyERP-Production` | (required) |

### Environment Secrets

Each environment needs these secrets:

| Secret | Description |
|--------|-------------|
| `AWS_ACCESS_KEY_ID` | AWS access key for ECR and ECS operations |
| `AWS_SECRET_ACCESS_KEY` | AWS secret access key |

## Example Environment Configuration

### Production Environment
```
Variables:
- AWS_REGION: us-east-2
- IMAGE_NAME: easyerp
- ECS_CLUSTER_NAME: EasyERP-Production
- ECS_SERVICE_NAME: EasyERP-Production

Secrets:
- AWS_ACCESS_KEY_ID: AKIA...
- AWS_SECRET_ACCESS_KEY: secret...
```

### Staging Environment
```
Variables:
- AWS_REGION: us-east-2
- IMAGE_NAME: easyerp
- ECS_CLUSTER_NAME: EasyERP-Stage
- ECS_SERVICE_NAME: EasyERP-Stage

Secrets:
- AWS_ACCESS_KEY_ID: AKIA...
- AWS_SECRET_ACCESS_KEY: secret...
```

## How It Works

1. **Push to Repository**: When you push code changes
2. **Environment Selection**: 
   - `main` branch → Production environment
   - Other branches → Staging environment
3. **Docker Build**: Builds image with environment-specific tag
4. **ECR Push**: Pushes image to Amazon ECR with tags:
   - `{env}-{commit-sha}` (e.g., `prod-abc123`)
   - `{env}-latest` (e.g., `prod-latest`)
5. **ECS Deploy**: Forces new deployment to pull latest image

## Image Tagging Strategy

- **Production**: `easyerp:prod-{commit-sha}` and `easyerp:prod-latest`
- **Staging**: `easyerp:stage-{commit-sha}` and `easyerp:stage-latest`

## Workflow Triggers

- **Production**: Pushes to `main` branch
- **Staging**: Pushes to `stage` branch (or other non-main branches)
- **Manual**: Can be triggered manually via workflow_dispatch

## Path Ignore

The workflow ignores changes to:
- `Cloudformation/**` - CloudFormation templates
- `.github/**` - GitHub Actions workflows

## Prerequisites

- AWS ECR repository for your Docker images
- ECS cluster and service already deployed
- Proper IAM permissions for ECR and ECS operations
- GitHub repository with proper environment configuration

## Troubleshooting

- Ensure ECR repository exists for your image
- Verify ECS cluster and service names match environment variables
- Check AWS credentials have ECR push and ECS update permissions
- Confirm Docker image builds successfully locally
- Verify ECS task definition is configured to pull from ECR

## Security Notes

- AWS credentials are stored as GitHub secrets
- Environment variables are used for non-sensitive configuration
- Each environment has separate credentials for isolation
