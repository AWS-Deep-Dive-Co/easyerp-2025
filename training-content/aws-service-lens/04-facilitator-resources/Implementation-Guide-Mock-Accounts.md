# Implementation Guide: Setting Up Mock Accounts & Easter Eggs
## Step-by-Step Setup for Training Environment

### Phase 1: Create Base User Accounts

#### AWS IAM User Creation
```bash
# Create IAM users for each team member
aws iam create-user --user-name sarah.chen
aws iam create-user --user-name marcus.rodriguez  
aws iam create-user --user-name jennifer.walsh
aws iam create-user --user-name david.kim
aws iam create-user --user-name rachel.thompson
aws iam create-user --user-name alex.rivera

# Create access keys for each user (save these for login credentials)
aws iam create-access-key --user-name sarah.chen
aws iam create-access-key --user-name marcus.rodriguez
# ... repeat for each user
```

#### GitHub User Setup
1. Invite users as collaborators to the EasyCo repository
2. Set initial permission levels as specified in the access matrix
3. Configure branch protection rules (with intentional gaps)

### Phase 2: Implement Appropriate Access Policies

#### AWS IAM Policies (Proper Access Levels)

##### Developer Base Policy
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ecs:DescribeServices",
        "ecs:DescribeTasks",
        "ecs:ListTasks",
        "ecr:GetDownloadUrlForLayer",
        "ecr:BatchGetImage",
        "ecr:BatchCheckLayerAvailability"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:RequestedRegion": "us-east-1"
        },
        "StringLike": {
          "aws:userid": "*:*dev*"
        }
      }
    }
  ]
}
```

##### QA Analyst Policy
```json
{
  "Version": "2012-10-17", 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ecs:DescribeServices",
        "ecs:RestartTask",
        "logs:GetLogEvents",
        "logs:DescribeLogGroups",
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": [
        "arn:aws:ecs:*:*:service/dev-*",
        "arn:aws:ecs:*:*:service/staging-*",
        "arn:aws:logs:*:*:log-group:dev-*",
        "arn:aws:logs:*:*:log-group:staging-*",
        "arn:aws:s3:::easyco-test-*/*"
      ]
    }
  ]
}
```

##### DevOps Engineer Policy
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow", 
      "Action": [
        "cloudformation:*",
        "ecs:*",
        "ecr:*"
      ],
      "Resource": "*",
      "Condition": {
        "StringNotLike": {
          "aws:userid": "*prod*"
        }
      }
    }
  ]
}
```

### Phase 3: Plant Easter Egg Violations

#### High Severity Violations

##### 1. Sarah Chen - Junior Developer Excessive Access
```bash
# Add production ECR push permissions (VIOLATION)
aws iam attach-user-policy \
  --user-name sarah.chen \
  --policy-arn arn:aws:iam::ACCOUNT:policy/ProductionECRPushPolicy

# GitHub: Make repository admin (VIOLATION)
# Navigate to GitHub Settings > Manage Access > sarah.chen > Change to Admin
```

**ProductionECRPushPolicy**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ecr:PutImage",
        "ecr:InitiateLayerUpload", 
        "ecr:UploadLayerPart",
        "ecr:CompleteLayerUpload"
      ],
      "Resource": "arn:aws:ecr:us-east-1:ACCOUNT:repository/easyerp-production"
    }
  ]
}
```

##### 2. Marcus Rodriguez - Database Access Violation
```bash
# Create database access policy (VIOLATION)
aws iam attach-user-policy \
  --user-name marcus.rodriguez \
  --policy-arn arn:aws:iam::ACCOUNT:policy/DirectDatabaseAccess
```

**DirectDatabaseAccess Policy**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "rds:DescribeDBInstances",
        "rds:Connect"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "secretsmanager:GetSecretValue"
      ],
      "Resource": "arn:aws:secretsmanager:*:*:secret:prod-db-credentials-*"
    }
  ]
}
```

##### 3. Jennifer Walsh - Infrastructure Modification Access
```bash
# Add CloudFormation permissions (VIOLATION)
aws iam attach-user-policy \
  --user-name jennifer.walsh \
  --policy-arn arn:aws:iam::aws:policy/CloudFormationFullAccess

# GitHub: Add main branch push access (VIOLATION)
# Settings > Branches > main > Edit > Uncheck "Restrict pushes that create files"
```

#### Medium Severity Violations

##### 4. Shared AWS Credentials Setup
```bash
# Create shared service account (VIOLATION)
aws iam create-user --user-name shared-deploy-user
aws iam create-access-key --user-name shared-deploy-user

# Attach broad permissions
aws iam attach-user-policy \
  --user-name shared-deploy-user \
  --policy-arn arn:aws:iam::aws:policy/PowerUserAccess
```

**GitHub Secrets Setup (VIOLATION)**:
```yaml
# Add same credentials to multiple environment secrets
AWS_ACCESS_KEY_ID: AKIA... (same for dev, staging, prod)
AWS_SECRET_ACCESS_KEY: xyz... (same for dev, staging, prod) 
```

##### 5. Database Credential Sharing
```bash
# Create same database secret for multiple environments (VIOLATION)
aws secretsmanager create-secret \
  --name staging-db-credentials \
  --secret-string '{"username":"admin","password":"SamePassword123"}'

aws secretsmanager create-secret \
  --name prod-db-credentials \
  --secret-string '{"username":"admin","password":"SamePassword123"}'
```

#### Subtle Violations

##### 6. Emergency Deployment Workflow
Create file: `.github/workflows/emergency-deploy.yml`
```yaml
name: Emergency Production Deploy
on:
  workflow_dispatch:
    inputs:
      reason:
        description: 'Emergency deployment reason'
        required: false  # VIOLATION: Not even required
        type: string
      skip_tests:
        description: 'Skip all testing'
        type: boolean
        default: true  # VIOLATION: Defaults to skip tests

jobs:
  emergency-deploy:
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: actions/checkout@v3
      - name: Deploy without gates
        run: |
          echo "EMERGENCY DEPLOYMENT - BYPASSING ALL CONTROLS"
          # Add actual deployment commands here
```

##### 7. Bastion Host Security Group Over-Permission
```bash
# Create overly permissive security group (VIOLATION)
aws ec2 create-security-group \
  --group-name bastion-overpermissive \
  --description "Bastion host with excessive access"

# Allow SSH from anywhere (VIOLATION)  
aws ec2 authorize-security-group-ingress \
  --group-name bastion-overpermissive \
  --protocol tcp \
  --port 22 \
  --cidr 0.0.0.0/0

# Allow database access from bastion to anywhere (VIOLATION)
aws ec2 authorize-security-group-egress \
  --group-name bastion-overpermissive \
  --protocol tcp \
  --port 5432 \
  --cidr 0.0.0.0/0
```

### Phase 4: Generate Audit Trail Evidence

#### Create CloudTrail Events for Discovery
```bash
# Generate ECR push events from junior developer (VIOLATION)
aws ecr put-image \
  --repository-name easyerp-production \
  --image-manifest file://manifest.json \
  --profile sarah-chen-profile

# Generate direct database connection attempts
aws rds describe-db-instances --profile marcus-rodriguez-profile

# Generate CloudFormation events from QA user
aws cloudformation describe-stacks --profile jennifer-walsh-profile
```

#### Setup Monitoring for Violations
```bash
# Create CloudWatch alarm for unusual ECR activity
aws cloudwatch put-metric-alarm \
  --alarm-name "UnauthorizedECRPush" \
  --alarm-description "Detect ECR pushes from non-DevOps users" \
  --metric-name PutImage \
  --namespace AWS/ECR \
  --statistic Sum \
  --period 300 \
  --threshold 1 \
  --comparison-operator GreaterThanThreshold
```

### Phase 5: Auditor Account Setup

#### Create Read-Only Audit Account
```bash
# Create auditor user
aws iam create-user --user-name auditor-readonly

# Attach comprehensive read-only policies
aws iam attach-user-policy \
  --user-name auditor-readonly \
  --policy-arn arn:aws:iam::aws:policy/ReadOnlyAccess

aws iam attach-user-policy \
  --user-name auditor-readonly \
  --policy-arn arn:aws:iam::aws:policy/CloudWatchReadOnlyAccess

aws iam attach-user-policy \
  --user-name auditor-readonly \
  --policy-arn arn:aws:iam::aws:policy/CloudTrailReadOnlyAccess
```

**Custom Auditor Policy**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iam:Get*",
        "iam:List*",
        "ecr:Describe*",
        "ecr:List*",
        "ecs:Describe*",
        "ecs:List*",
        "cloudformation:Describe*",
        "cloudformation:List*",
        "secretsmanager:ListSecrets",
        "secretsmanager:DescribeSecret"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Deny",
      "Action": [
        "secretsmanager:GetSecretValue"  
      ],
      "Resource": "*"
    }
  ]
}
```

### Phase 6: Verification & Testing

#### Pre-Training Verification Checklist
- [ ] All user accounts created and accessible
- [ ] Violations planted and verifiable
- [ ] CloudTrail events generated and searchable
- [ ] GitHub permissions set with intentional gaps
- [ ] Auditor accounts have appropriate read-only access
- [ ] Emergency workflows accessible to unauthorized users
- [ ] Database credentials shared between environments
- [ ] Cross-environment access violations detectable

#### Test Scenarios
```bash
# Test 1: Verify junior developer can push to production ECR
aws ecr get-login-token --profile sarah-chen
docker push ACCOUNT.dkr.ecr.us-east-1.amazonaws.com/easyerp-production:test

# Test 2: Verify QA can modify CloudFormation
aws cloudformation update-stack --stack-name prod-stack --profile jennifer-walsh

# Test 3: Verify shared credentials work across environments  
aws sts get-caller-identity --profile shared-deploy
```

This implementation guide provides everything needed to create a realistic audit training environment with discoverable control weaknesses that mirror real-world scenarios.
