# GitHub Actions Workflow Coordination - Simplified

This repository uses a simplified, linear GitHub Actions workflow pipeline that ensures proper deployment order for both infrastructure and application changes.

## Simplified Workflow Overview

### Linear Pipeline Flow:
```
Push (any changes) → Sync to S3 → CloudFormation Deployment → ECS Deployment
```

### 1. Sync to S3 (`syncs3.yml`)
- **Trigger**: Push to `main` or `stage` branches (all changes)
- **Purpose**: Uploads all files (including CloudFormation templates) to S3
- **Process**:
  1. Syncs entire repository to S3 bucket
  2. Ensures CloudFormation templates are available for deployment
- **Next**: Triggers CloudFormation Deployment workflow

### 2. CloudFormation Deployment (`cf_changeset_deployment.yml`)
- **Trigger**: Completion of Sync to S3 workflow
- **Purpose**: Creates and executes CloudFormation changesets automatically
- **Process**:
  1. Creates CloudFormation changeset using templates from S3
  2. Waits for changeset to be ready
  3. Executes changeset automatically  
  4. Waits for stack update completion
- **Next**: Triggers ECS Deployment workflow

### 3. ECS Deployment (`Build-and-deploy.yml`)
- **Trigger**: Completion of CloudFormation Deployment workflow
- **Purpose**: Builds Docker image and deploys to ECS
- **Process**:
  1. Builds Docker image from latest code
  2. Pushes image to ECR
  3. Updates ECS service with new deployment

## Deployment Scenarios

### All Changes (Infrastructure + Application):
```
Push → CloudFormation Deployment → Sync to S3 → ECS Deployment
```
- All changes go through the complete pipeline
- Infrastructure changes are applied first
- Application changes follow automatically

### Benefits of Simplified Approach

- **Predictable**: Every push follows the same linear path
- **Safe**: Infrastructure is always updated before applications
- **Simple**: No complex conditional logic to debug
- **Reliable**: Each step waits for the previous to complete successfully
- **Consistent**: Same flow for all types of changes

## Manual Deployment

All workflows support manual dispatch (`workflow_dispatch`) for:
- Emergency deployments
- Testing workflow changes
- Deploying specific branches

## Environment Configuration

Both workflows support environment-specific deployments:
- **main branch** → Production environment
- **stage branch** → Staging environment

Each environment uses its own AWS credentials and configuration variables.

## Failure Handling

- If CloudFormation deployment fails, the pipeline stops
- If S3 sync fails, ECS deployment is skipped
- Each step only runs if the previous step completed successfully
