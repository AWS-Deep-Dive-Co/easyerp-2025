# GitHub Actions Workflow Coordination

This repository uses coordinated GitHub Actions workflows to handle both CloudFormation infrastructure changes and application code deployments. The workflows are designed to ensure proper deployment order and prevent conflicts.

## Workflow Overview

### 1. Sync to S3 (`syncs3.yml`)
- **Trigger**: Push to `main` or `stage` branches with CloudFormation changes
- **Purpose**: Uploads CloudFormation templates to S3
- **Next**: Triggers CloudFormation Deployment workflow

### 2. CloudFormation Deployment (`cf_changeset_deployment.yml`)
- **Trigger**: Completion of "Sync to S3" workflow
- **Purpose**: Creates and executes CloudFormation changesets automatically
- **Process**:
  1. Creates CloudFormation changeset
  2. Waits for changeset to be ready
  3. Executes changeset automatically
  4. Waits for stack update completion
- **Next**: Triggers ECS Deployment workflow

### 3. ECS Deployment (`Build-and-deploy.yml`)
- **Triggers**: 
  - Push to `main` or `stage` branches (any changes)
  - Completion of CloudFormation Deployment workflow
  - Manual dispatch
- **Smart Logic**:
  - **Code-only changes**: Deploys immediately
  - **CloudFormation changes**: Waits for CloudFormation deployment to complete first
  - **Manual trigger**: Deploys immediately

## Deployment Scenarios

### Scenario 1: Code-Only Changes
```
Push (app code) → ECS Deployment → Docker Build → ECS Deploy
```
- Fast path for application updates
- No infrastructure changes needed

### Scenario 2: CloudFormation Changes
```
Push (CF templates) → Sync to S3 → CloudFormation Deployment → ECS Deployment → Docker Build → ECS Deploy
```
- Infrastructure changes are applied first
- Application deployment follows automatically

### Scenario 3: Mixed Changes
```
Push (CF + app code) → Sync to S3 → CloudFormation Deployment → ECS Deployment → Docker Build → ECS Deploy
```
- CloudFormation changes are detected and processed first
- Application changes wait for infrastructure completion

## Workflow Logic

The ECS Deployment workflow uses intelligent trigger detection:

1. **workflow_run trigger**: Runs after CloudFormation deployment completes
2. **push trigger**: Checks if changes include CloudFormation files
   - If yes: Skips deployment (waits for CloudFormation workflow)
   - If no: Proceeds with immediate deployment

## Benefits

- **Automatic coordination**: No manual intervention required
- **Safe deployment order**: Infrastructure changes always applied before app changes
- **Efficient**: Code-only changes deploy immediately without waiting
- **Flexible**: Supports manual deployments when needed
- **Resilient**: Failed CloudFormation deployments prevent app deployments

## Environment Configuration

Both workflows support environment-specific deployments:
- **main branch** → Production environment
- **stage branch** → Staging environment

Each environment uses its own AWS credentials and configuration variables.
