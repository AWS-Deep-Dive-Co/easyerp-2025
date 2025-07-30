# CloudFormation Change Set Creation Workflow

This workflow creates CloudFormation Change Sets for existing stacks whenever templates in the CloudFormation folder are updated.

## Overview

The workflow consists of two parts:
1. **S3 Sync** (`syncs3.yml`) - Syncs CloudFormation templates to S3
2. **Change Set Creation** (`stackset-deployment.yml`) - Creates change sets for existing stacks

## Environment Setup

### GitHub Environments Required

Create two environments in your repository:
- **Production** (for `main` branch)
- **Staging** (for non-main branches)

### Environment Variables

Each environment needs these variables:

| Variable | Description | Example |
|----------|-------------|---------|
| `AWS_REGION` | Target AWS region | `us-east-1` |
| `STACK_NAME` | Name of the existing CloudFormation stack | `my-production-stack` |
| `S3_BUCKET` | S3 bucket for storing templates | `my-cloudformation-templates` |
| `MASTER_TEMPLATE` | Main template filename | `master.yaml` |

### Environment Secrets

Each environment needs these secrets:

| Secret | Description |
|--------|-------------|
| `AWS_ACCESS_KEY_ID` | AWS access key for CloudFormation operations |
| `AWS_SECRET_ACCESS_KEY` | AWS secret access key |

## How It Works

1. **Push to Repository**: When you push changes to CloudFormation templates
2. **S3 Sync**: Templates are automatically synced to the appropriate S3 bucket
3. **Change Set Creation**: A change set is created for the existing CloudFormation stack
4. **Manual Review**: You review and execute the change set in the AWS console

## Workflow Triggers

- **Production**: Pushes to `main` branch
- **Staging**: Pushes to any other branch

## Change Set Naming

Change sets are automatically named with timestamp: `changeset-YYYYMMDD-HHMMSS`

## Next Steps After Workflow

1. Go to AWS CloudFormation console
2. Navigate to your stack
3. Click on "Change Sets" tab
4. Find the newly created change set
5. Review the changes
6. Execute the change set if approved

## Prerequisites

- Existing CloudFormation stack deployed in your AWS account
- Proper IAM permissions for CloudFormation operations
- S3 bucket for storing templates
- GitHub repository with proper environment configuration

## Troubleshooting

- Ensure your existing stack name matches the `STACK_NAME` variable
- Verify AWS credentials have CloudFormation permissions
- Check that S3 bucket exists and is accessible
- Confirm template syntax is valid before pushing
