# GitHub Environments Setup for StackSet Deployment

This workflow uses GitHub Environments to manage secrets and environment variables for different deployment targets (development and production).

## Required GitHub Environments

You need to create two environments in your GitHub repository:

1. **`development`** - For develop branch deployments
2. **`production`** - For main branch deployments (with protection rules recommended)

## Environment Setup Instructions

### 1. Create Environments

Go to your repository settings → Environments → New environment

#### Development Environment
- **Name**: `development`
- **Protection Rules**: Optional (can deploy immediately)

#### Production Environment  
- **Name**: `production`
- **Protection Rules**: Recommended
  - ✅ Required reviewers (1-6 people)
  - ✅ Wait timer (optional)
  - ✅ Deployment protection rules

### 2. Configure Secrets (Required)

Add these secrets to **both** environments:

| Secret Name | Description | Example |
|------------|-------------|---------|
| `AWS_ACCESS_KEY_ID` | AWS Access Key with CloudFormation permissions | `AKIAIOSFODNN7EXAMPLE` |
| `AWS_SECRET_ACCESS_KEY` | AWS Secret Access Key | `wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY` |

### 3. Configure Environment Variables (Optional)

Add these variables to customize deployment behavior:

#### Common Variables (Both Environments)

| Variable Name | Description | Default Value | Example |
|--------------|-------------|---------------|---------|
| `AWS_REGION` | Target AWS region for deployment | `us-east-1` | `us-west-2` |
| `PROJECT_NAME` | Project name for resource tagging | `easyerp` | `my-project` |
| `MASTER_TEMPLATE` | Main CloudFormation template file | `master.yaml` | `main-template.yaml` |

#### Development Environment Variables

| Variable Name | Description | Default Value | Example |
|--------------|-------------|---------------|---------|
| `DEV_STACKSET_NAME` | Development StackSet name | `easyerp-dev-stackset` | `myproject-dev-stackset` |
| `VPC_CIDR` | VPC CIDR block for development | - | `10.0.0.0/16` |
| `INSTANCE_TYPE` | EC2 instance type for development | - | `t3.micro` |

#### Production Environment Variables

| Variable Name | Description | Default Value | Example |
|--------------|-------------|---------------|---------|
| `PROD_STACKSET_NAME` | Production StackSet name | `easyerp-prod-stackset` | `myproject-prod-stackset` |
| `VPC_CIDR` | VPC CIDR block for production | - | `10.1.0.0/16` |
| `INSTANCE_TYPE` | EC2 instance type for production | - | `t3.small` |

## Workflow Behavior

### Development Deployments (develop branch)
- Uses `development` environment
- Deploys to dev StackSet
- Uses development environment variables and secrets

### Production Deployments (main branch)
- Uses `production` environment
- Requires approval if protection rules are enabled
- Deploys to production StackSet
- Uses production environment variables and secrets

## CloudFormation Template Requirements

Your CloudFormation templates should accept these parameters:

```yaml
Parameters:
  Environment:
    Type: String
    Description: Environment name (dev/prod)
    
  ProjectName:
    Type: String
    Description: Project name for resource naming
    Default: easyerp
    
  VpcCidr:
    Type: String
    Description: VPC CIDR block
    Default: 10.0.0.0/16
    
  InstanceType:
    Type: String
    Description: EC2 instance type
    Default: t3.micro
```

## AWS Permissions Required

The AWS credentials need the following permissions:

### CloudFormation Permissions
```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "cloudformation:*"
            ],
            "Resource": "*"
        }
    ]
}
```

### Additional Service Permissions
Depending on your CloudFormation templates, you may need additional permissions for:
- EC2 (VPC, Security Groups, Instances)
- ECS (Clusters, Services, Tasks)
- RDS (Databases, Subnets)
- IAM (Roles, Policies)
- S3 (Buckets, Objects)
- CloudWatch (Logs, Metrics)

## Example Environment Setup

### Development Environment Variables
```
AWS_REGION=us-east-1
DEV_STACKSET_NAME=mycompany-dev-stackset
PROJECT_NAME=mycompany-erp
MASTER_TEMPLATE=infrastructure/main.yaml
VPC_CIDR=10.0.0.0/16
INSTANCE_TYPE=t3.micro
```

### Production Environment Variables
```
AWS_REGION=us-west-2
PROD_STACKSET_NAME=mycompany-prod-stackset
PROJECT_NAME=mycompany-erp
MASTER_TEMPLATE=infrastructure/main.yaml
VPC_CIDR=10.1.0.0/16
INSTANCE_TYPE=t3.large
```

## Troubleshooting

### Common Issues

1. **Missing Environment**: Ensure environments are created with exact names `development` and `production`

2. **Missing Secrets**: Verify AWS credentials are added to the correct environment

3. **Permission Denied**: Check AWS IAM permissions for CloudFormation and required services

4. **Template Not Found**: Verify `MASTER_TEMPLATE` variable points to correct file path

5. **Parameter Errors**: Ensure CloudFormation template accepts all passed parameters

### Debugging Steps

1. Check workflow run logs for specific error messages
2. Verify environment variable values in workflow summary
3. Test CloudFormation template locally with AWS CLI
4. Validate AWS credentials have required permissions

## Security Best Practices

1. **Use Protection Rules**: Enable required reviewers for production environment
2. **Rotate Credentials**: Regularly rotate AWS access keys
3. **Principle of Least Privilege**: Grant only required AWS permissions
4. **Monitor Deployments**: Review CloudTrail logs for StackSet operations
5. **Use Branch Protection**: Require pull request reviews before merging
