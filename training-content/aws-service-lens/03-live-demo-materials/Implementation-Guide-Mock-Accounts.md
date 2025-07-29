# Implementation Guide: Setting Up Mock Accounts & Easter Eggs
## Step-by-Step Setup for EasyCo Manufacturing Training Environment

### Phase 1: Create Base User Accounts

#### AWS IAM User Creation
```bash
# Create IAM users for each EasyCo team member
aws iam create-user --user-name alannah.rye
aws iam create-user --user-name lorin.richards  
aws iam create-user --user-name kester.ellison
aws iam create-user --user-name alex.guenther
aws iam create-user --user-name maisy.watts
aws iam create-user --user-name joey.kuhnsman
aws iam create-user --user-name greta.dyson
aws iam create-user --user-name derek.steele
aws iam create-user --user-name susan.darnell

# Create access keys for each user (save these for login credentials)
aws iam create-access-key --user-name alannah.rye
aws iam create-access-key --user-name lorin.richards
# ... repeat for each user
```

#### GitHub User Setup
1. Invite users as collaborators to the EasyCo ERP repository
2. Set initial permission levels as specified in the access matrix
3. Configure branch protection rules (with intentional gaps for violations)

### Phase 2: Implement Appropriate Access Policies

#### AWS IAM Policies (Proper Access Levels)

##### Junior Developer Base Policy (Alannah Rye)
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
        "ecr:BatchCheckLayerAvailability",
        "logs:GetLogEvents",
        "logs:DescribeLogGroups"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:RequestedRegion": "us-east-1",
          "aws:ResourceTag/Environment": "dev"
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "s3:ExistingObjectTag/Environment": "dev"
        }
      }
    }
  ]
}
```

##### Senior Developer Policy (Lorin Richards)
```json
{
  "Version": "2012-10-17", 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ecs:DescribeServices",
        "ecs:RestartTask",
        "ecs:UpdateService",
        "ecr:GetDownloadUrlForLayer",
        "ecr:BatchGetImage",
        "ecr:PutImage",
        "logs:GetLogEvents",
        "logs:DescribeLogGroups"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/Environment": ["dev", "stage"]
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "s3:ExistingObjectTag/Environment": ["dev", "stage"]
        }
      }
    }
  ]
}
```

##### QA Analyst Policy (Kester Ellison & Alex Guenther)
```json
{
  "Version": "2012-10-17", 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ecs:DescribeServices",
        "ecs:DescribeTasks",
        "ecs:RestartTask",
        "logs:GetLogEvents",
        "logs:DescribeLogGroups",
        "logs:DescribeLogStreams"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/Environment": ["dev", "stage"]
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": [
        "rds:DescribeDBInstances"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/Environment": "stage"
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "s3:ExistingObjectTag/Environment": ["dev", "stage"]
        }
      }
    }
  ]
}
```

##### DevOps Engineer Policy (Maisy Watts)
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow", 
      "Action": [
        "cloudformation:*",
        "ecs:*",
        "ecr:*",
        "iam:Get*",
        "iam:List*",
        "iam:PassRole",
        "logs:*",
        "cloudwatch:*"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/Environment": ["dev", "stage"]
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": [
        "cloudformation:DescribeStacks",
        "cloudformation:ListStacks"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/Environment": "prod"
        }
      }
    }
  ]
}
```

##### Database Administrator Policy (Greta Dyson)
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "rds:*",
        "secretsmanager:GetSecretValue",
        "secretsmanager:UpdateSecret",
        "secretsmanager:RotateSecret",
        "cloudwatch:GetMetricStatistics",
        "cloudwatch:ListMetrics"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "s3:ExistingObjectTag/Purpose": "*backup*"
        }
      }
    }
  ]
}
```

##### Business Analyst Policy (Derek Steele)
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "cloudwatch:GetMetricStatistics",
        "cloudwatch:ListMetrics",
        "cloudwatch:DescribeAlarms",
        "logs:GetLogEvents",
        "logs:DescribeLogGroups"
      ],
      "Resource": "*",
      "Condition": {
        "StringLike": {
          "cloudwatch:MetricName": ["ApplicationMetrics", "BusinessMetrics", "UserActivity"]
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "s3:ExistingObjectTag/DataType": "business-reports"
        }
      }
    }
  ]
}
```

##### Treasury/Cost Management Policy (Susan Darnell)
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ce:*",
        "budgets:*",
        "aws-portal:ViewBilling",
        "aws-portal:ViewAccount",
        "cloudwatch:GetMetricStatistics",
        "support:*"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:GetObject",
        "s3:PutObject"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "s3:ExistingObjectTag/DataType": "cost-reports"
        }
      }
    }
  ]
}
```

### Phase 3: Plant Easter Egg Violations

#### High Severity Violations

##### 1. Alannah Rye - Junior Developer Excessive Production Access
```bash
# Add production ECR push permissions (VIOLATION)
aws iam attach-user-policy \
  --user-name alannah.rye \
  --policy-arn arn:aws:iam::ACCOUNT:policy/ProductionECRPushPolicy

# Add production RDS secrets access (VIOLATION)
aws iam attach-user-policy \
  --user-name alannah.rye \
  --policy-arn arn:aws:iam::ACCOUNT:policy/ProductionSecretsReadAccess

# GitHub: Make repository admin (VIOLATION)
# Navigate to GitHub Settings > Manage Access > alannah.rye > Change to Admin
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
        "ecr:CompleteLayerUpload",
        "ecr:BatchCheckLayerAvailability"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/Environment": "prod"
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:PutObject"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "s3:ExistingObjectTag/Environment": "prod"
        }
      }
    }
  ]
}
```

**ProductionSecretsReadAccess**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "secretsmanager:GetSecretValue"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/Environment": "prod"
        }
      }
    }
  ]
}
```

##### 2. Lorin Richards - Senior Developer Production Database Access
```bash
# Create direct production database access policy (VIOLATION)
aws iam attach-user-policy \
  --user-name lorin.richards \
  --policy-arn arn:aws:iam::ACCOUNT:policy/DirectProductionDatabaseAccess

# Add CloudFormation permissions for security groups (VIOLATION)
aws iam attach-user-policy \
  --user-name lorin.richards \
  --policy-arn arn:aws:iam::ACCOUNT:policy/SecurityGroupManagement
```

**DirectProductionDatabaseAccess Policy**:
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
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/Environment": "prod"
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": [
        "secretsmanager:GetSecretValue"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/Environment": "prod"
        }
      }
    }
  ]
}
```

**SecurityGroupManagement Policy**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:AuthorizeSecurityGroupIngress",
        "ec2:AuthorizeSecurityGroupEgress",
        "ec2:RevokeSecurityGroupIngress",
        "ec2:RevokeSecurityGroupEgress"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/Environment": "prod"
        }
      }
    }
  ]
}
```

##### 3. Kester Ellison - QA Infrastructure Modification Access
```bash
# Add production CloudFormation permissions (VIOLATION)
aws iam attach-user-policy \
  --user-name kester.ellison \
  --policy-arn arn:aws:iam::aws:policy/CloudFormationFullAccess

# Add production ECS permissions (VIOLATION)
aws iam attach-user-policy \
  --user-name kester.ellison \
  --policy-arn arn:aws:iam::ACCOUNT:policy/ProductionECSModify

# GitHub: Add main branch push access (VIOLATION)
# Settings > Branches > main > Edit > Add kester.ellison to bypass restrictions
```

**ProductionECSModify Policy**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ecs:UpdateService",
        "ecs:CreateService",
        "ecs:DeleteService",
        "ecs:RegisterTaskDefinition"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/Environment": "prod"
        }
      }
    }
  ]
}
```

##### 4. Derek Steele - Business Analyst Technical Infrastructure Access
```bash
# Add technical infrastructure access (VIOLATION)
aws iam attach-user-policy \
  --user-name derek.steele \
  --policy-arn arn:aws:iam::ACCOUNT:policy/TechnicalInfrastructureAccess

# Add IAM read access (VIOLATION)
aws iam attach-user-policy \
  --user-name derek.steele \
  --policy-arn arn:aws:iam::aws:policy/IAMReadOnlyAccess
```

**TechnicalInfrastructureAccess Policy**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ecs:RestartTask",
        "ecs:UpdateService",
        "cloudformation:DescribeStacks",
        "cloudformation:ListStacks"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/Environment": "prod"
        }
      }
    },
    {
      "Effect": "Allow",
      "Action": [
        "s3:PutObject"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "s3:ExistingObjectTag/DataType": "system-config"
        }
      }
    }
  ]
}
```

##### 5. Susan Darnell - Treasury Operational System Access
```bash
# Add production operational controls (VIOLATION)
aws iam attach-user-policy \
  --user-name susan.darnell \
  --policy-arn arn:aws:iam::ACCOUNT:policy/ProductionOperationalAccess
```

**ProductionOperationalAccess Policy**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ec2:StartInstances",
        "ec2:StopInstances",
        "ec2:TerminateInstances",
        "rds:ModifyDBInstance",
        "ecs:UpdateService",
        "lambda:UpdateFunctionConfiguration"
      ],
      "Resource": "*",
      "Condition": {
        "StringEquals": {
          "aws:ResourceTag/Environment": "prod"
        }
      }
    }
  ]
}
```

#### Medium Severity Violations

##### 6. Maisy Watts - Shared AWS Credentials Setup
```bash
# Create shared service account (VIOLATION)
aws iam create-user --user-name easyerp-shared-deploy
aws iam create-access-key --user-name easyerp-shared-deploy

# Attach broad permissions to shared account
aws iam attach-user-policy \
  --user-name easyerp-shared-deploy \
  --policy-arn arn:aws:iam::aws:policy/PowerUserAccess
```

**GitHub Secrets Setup (VIOLATION)**:
```yaml
# Add same credentials to multiple environment secrets
# In repository secrets:
AWS_ACCESS_KEY_ID_DEV: AKIA... (shared account)
AWS_SECRET_ACCESS_KEY_DEV: xyz... (shared account)
AWS_ACCESS_KEY_ID_STAGING: AKIA... (same shared account)
AWS_SECRET_ACCESS_KEY_STAGING: xyz... (same shared account) 
AWS_ACCESS_KEY_ID_PROD: AKIA... (same shared account)
AWS_SECRET_ACCESS_KEY_PROD: xyz... (same shared account)
```

##### 7. Greta Dyson - Database Admin Container Access
```bash
# Add ECR and ECS permissions to DBA (VIOLATION)
aws iam attach-user-policy \
  --user-name greta.dyson \
  --policy-arn arn:aws:iam::ACCOUNT:policy/ContainerImageAccess
```

**ContainerImageAccess Policy**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "ecr:PutImage",
        "ecr:BatchGetImage",
        "ecs:RegisterTaskDefinition",
        "ecs:UpdateService"
      ],
      "Resource": "*"
    }
  ]
}
```

#### Subtle Violations

##### 8. Cross-Environment Database Credentials
```bash
# Create same database secret for multiple environments (VIOLATION)
aws secretsmanager create-secret \
  --name easyerp-stage-db-credentials \
  --secret-string '{"username":"easyerpuser","password":"SharedPassword123!"}' \
  --tags '[{"Key":"Environment","Value":"stage"}]'

aws secretsmanager create-secret \
  --name easyerp-prod-db-credentials \
  --secret-string '{"username":"easyerpuser","password":"SharedPassword123!"}' \
  --tags '[{"Key":"Environment","Value":"prod"}]'
```

##### 9. Tag-Based Access Control Bypass (Subtle Violation)
```bash
# Create policy that bypasses tag restrictions through wildcard conditions (VIOLATION)
aws iam create-policy \
  --policy-name TagBypassPolicy \
  --policy-document '{
    "Version": "2012-10-17",
    "Statement": [
      {
        "Effect": "Allow",
        "Action": [
          "ecs:UpdateService",
          "rds:ModifyDBInstance"
        ],
        "Resource": "*",
        "Condition": {
          "StringLike": {
            "aws:ResourceTag/Environment": "*"
          }
        }
      }
    ]
  }'

# Attach to multiple users who should only have dev/stage access
aws iam attach-user-policy --user-name kester.ellison --policy-arn arn:aws:iam::ACCOUNT:policy/TagBypassPolicy
```

##### 10. Emergency Deployment Workflow
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
      deployer:
        description: 'Who is deploying'
        required: false  # VIOLATION: No accountability
      target_environment:
        description: 'Target environment (stage/prod)'
        required: false  # VIOLATION: Could deploy to wrong environment
        default: 'prod'

jobs:
  emergency-deploy:
    runs-on: ubuntu-latest
    # VIOLATION: No environment protection rules
    steps:
      - uses: actions/checkout@v3
      - name: Deploy without gates
        run: |
          echo "EMERGENCY DEPLOYMENT - BYPASSING ALL CONTROLS"
          echo "Reason: ${{ github.event.inputs.reason }}"
          echo "Deployer: ${{ github.event.inputs.deployer }}"
          echo "Target: ${{ github.event.inputs.target_environment }}"
          # Deploy to any environment without proper validation
          aws ecs update-service \
            --cluster easyerp-${{ github.event.inputs.target_environment }} \
            --service webapp \
            --force-new-deployment
        env:
          AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID_SHARED }}
          AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY_SHARED }}
```

##### 11. Bastion Host Security Group Over-Permission
```bash
# Create overly permissive bastion security group (VIOLATION)
aws ec2 create-security-group \
  --group-name easyerp-bastion-overpermissive \
  --description "Bastion host with excessive access" \
  --vpc-id vpc-12345678 \
  --tag-specifications 'ResourceType=security-group,Tags=[{Key=Environment,Value=prod},{Key=Purpose,Value=bastion}]'

# Allow SSH from anywhere (VIOLATION)  
aws ec2 authorize-security-group-ingress \
  --group-id sg-12345678 \
  --protocol tcp \
  --port 22 \
  --cidr 0.0.0.0/0

# Allow database access from bastion to anywhere (VIOLATION)
aws ec2 authorize-security-group-egress \
  --group-id sg-12345678 \
  --protocol tcp \
  --port 5432 \
  --cidr 0.0.0.0/0

# Associate with bastion instance
aws ec2 modify-instance-attribute \
  --instance-id i-1234567890abcdef0 \
  --groups sg-12345678

# Tag the bastion instance improperly (VIOLATION: Wrong environment tag)
aws ec2 create-tags \
  --resources i-1234567890abcdef0 \
  --tags Key=Environment,Value=dev Key=ActualEnvironment,Value=prod
```

### Phase 4: Generate Audit Trail Evidence

#### Create CloudTrail Events for Discovery
```bash
# Generate ECR push events from junior developer to production (VIOLATION)
aws ecr put-image \
  --repository-name easyerp-prod \
  --image-manifest file://manifest.json \
  --profile alannah-rye-profile

# Generate production S3 access from junior developer
aws s3 cp test-file.txt s3://easyerp-prod-assets/ --profile alannah-rye-profile

# Generate direct database connection attempts from senior developer to production
aws rds describe-db-instances --profile lorin-richards-profile | grep -E "(prod|Environment.*prod)"

# Generate database secret access from senior developer for production
aws secretsmanager get-secret-value --secret-id easyerp-prod-db-credentials --profile lorin-richards-profile

# Generate CloudFormation events from QA user on production resources
aws cloudformation describe-stacks --profile kester-ellison-profile | grep -E "prod"

# Generate ECS service modifications from QA user on production
aws ecs update-service --cluster easyerp-prod --service webapp --desired-count 3 --profile kester-ellison-profile

# Generate infrastructure access from business analyst on production resources
aws ecs list-services --cluster easyerp-prod --profile derek-steele-profile
aws ecs update-service --cluster easyerp-prod --service webapp --force-new-deployment --profile derek-steele-profile

# Generate operational changes from treasury user on production resources
aws ec2 describe-instances --filters "Name=tag:Environment,Values=prod" --profile susan-darnell-profile
aws ec2 stop-instances --instance-ids i-1234567890abcdef0 --profile susan-darnell-profile
aws rds modify-db-instance --db-instance-identifier easyerp-prod --db-instance-class db.t3.small --profile susan-darnell-profile

# Generate container access from DBA on production
aws ecr put-image --repository-name easyerp-prod --image-manifest file://db-migration.json --profile greta-dyson-profile

# Generate tag-based access violations
aws ecs describe-services --cluster easyerp-stage --profile kester-ellison-profile
aws ecs describe-services --cluster easyerp-prod --profile kester-ellison-profile
```

#### Setup Monitoring for Violations
```bash
# Create CloudWatch alarm for unusual ECR activity on prod resources
aws cloudwatch put-metric-alarm \
  --alarm-name "UnauthorizedECRPush-JuniorDeveloper-Prod" \
  --alarm-description "Detect ECR pushes from junior developers to production resources" \
  --metric-name PutImage \
  --namespace AWS/ECR \
  --statistic Sum \
  --period 300 \
  --threshold 1 \
  --comparison-operator GreaterThanThreshold \
  --dimensions Name=RepositoryName,Value=easyerp-prod

# Create alarm for database access violations on production
aws cloudwatch put-metric-alarm \
  --alarm-name "DirectDatabaseAccess-Production" \
  --alarm-description "Detect direct database connections to production databases" \
  --metric-name ConnectionCount \
  --namespace AWS/RDS \
  --statistic Sum \
  --period 300 \
  --threshold 5 \
  --comparison-operator GreaterThanThreshold \
  --dimensions Name=DBInstanceIdentifier,Value=easyerp-prod

# Create alarm for business user technical access to production
aws cloudwatch put-metric-alarm \
  --alarm-name "BusinessUserProductionAccess" \
  --alarm-description "Detect technical infrastructure access from business users to production" \
  --metric-name APICallsCount \
  --namespace CloudTrail \
  --statistic Sum \
  --period 300 \
  --threshold 10 \
  --comparison-operator GreaterThanThreshold

# Create alarm for cross-environment tag violations
aws cloudwatch put-metric-alarm \
  --alarm-name "TagBasedAccessViolations" \
  --alarm-description "Detect access to resources outside of proper environment tags" \
  --metric-name AccessViolations \
  --namespace CloudTrail \
  --statistic Sum \
  --period 300 \
  --threshold 1 \
  --comparison-operator GreaterThanThreshold

# Create alarm for off-hours production changes
aws cloudwatch put-metric-alarm \
  --alarm-name "OffHoursProductionChanges" \
  --alarm-description "Detect production changes outside business hours" \
  --metric-name ModificationEvents \
  --namespace CloudTrail \
  --statistic Sum \
  --period 3600 \
  --threshold 1 \
  --comparison-operator GreaterThanThreshold
```

### Phase 5: Auditor Account Setup

#### Create Read-Only Audit Account
```bash
# Create auditor user
aws iam create-user --user-name easyerp-auditor-readonly

# Attach comprehensive read-only policies
aws iam attach-user-policy \
  --user-name easyerp-auditor-readonly \
  --policy-arn arn:aws:iam::aws:policy/ReadOnlyAccess

aws iam attach-user-policy \
  --user-name easyerp-auditor-readonly \
  --policy-arn arn:aws:iam::aws:policy/CloudWatchReadOnlyAccess

aws iam attach-user-policy \
  --user-name easyerp-auditor-readonly \
  --policy-arn arn:aws:iam::aws:policy/CloudTrailReadOnlyAccess

aws iam attach-user-policy \
  --user-name easyerp-auditor-readonly \
  --policy-arn arn:aws:iam::ACCOUNT:policy/EasyERPAuditorPolicy
```

**EasyERPAuditorPolicy**:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "iam:Get*",
        "iam:List*",
        "iam:Generate*",
        "ecr:Describe*",
        "ecr:List*",
        "ecr:GetAuthorizationToken",
        "ecs:Describe*",
        "ecs:List*",
        "cloudformation:Describe*",
        "cloudformation:List*",
        "cloudformation:Get*",
        "secretsmanager:ListSecrets",
        "secretsmanager:DescribeSecret",
        "rds:Describe*",
        "rds:List*",
        "ec2:Describe*",
        "s3:ListBucket",
        "s3:GetBucketPolicy",
        "s3:GetBucketAcl",
        "lambda:List*",
        "lambda:Get*"
      ],
      "Resource": "*"
    },
    {
      "Effect": "Deny",
      "Action": [
        "secretsmanager:GetSecretValue",
        "rds:Connect",
        "iam:Create*",
        "iam:Delete*",
        "iam:Update*",
        "iam:Put*",
        "iam:Attach*",
        "iam:Detach*"
      ],
      "Resource": "*"
    }
  ]
}
```

#### GitHub Auditor Setup
1. Add auditor as read-only collaborator to repository
2. Provide access to Actions logs and workflow history
3. Grant access to security tab for dependency and code scanning results

### Phase 6: Verification & Testing

#### Pre-Training Verification Checklist
- [ ] All EasyCo team member accounts created and accessible
- [ ] Violations planted and verifiable through AWS Console/CLI
- [ ] CloudTrail events generated and searchable in CloudWatch
- [ ] GitHub permissions set with intentional access violations
- [ ] Auditor accounts have appropriate read-only access
- [ ] Emergency workflows accessible to unauthorized users
- [ ] Database credentials shared between staging and production
- [ ] Cross-functional access violations detectable
- [ ] Business users have inappropriate technical access
- [ ] Treasury user can make operational changes

#### Test Scenarios for Each Violation
```bash
# Test 1: Verify junior developer can push to production ECR (tag-based violation)
aws ecr get-login-token --profile alannah-rye
docker tag local-image:latest ACCOUNT.dkr.ecr.us-east-1.amazonaws.com/easyerp-prod:test
docker push ACCOUNT.dkr.ecr.us-east-1.amazonaws.com/easyerp-prod:test

# Test 2: Verify senior developer can access production database (tag-based violation)
aws secretsmanager get-secret-value --secret-id easyerp-prod-db-credentials --profile lorin-richards
# Should succeed due to tag-based policy violation

# Test 3: Verify QA can modify production CloudFormation (tag-based violation)
aws cloudformation describe-stacks --profile kester-ellison | grep -E "Environment.*prod"
aws ecs update-service --cluster easyerp-prod --service webapp --desired-count 2 --profile kester-ellison

# Test 4: Verify shared credentials work across environments  
aws sts get-caller-identity --profile easyerp-shared-deploy
# Should show same user identity accessing both stage and prod resources

# Test 5: Verify business analyst can restart production services (tag-based violation)
aws ecs describe-services --cluster easyerp-prod --profile derek-steele
aws ecs update-service --cluster easyerp-prod --service webapp --force-new-deployment --profile derek-steele

# Test 6: Verify treasury user can stop production instances (tag-based violation)
aws ec2 describe-instances --filters "Name=tag:Environment,Values=prod" --profile susan-darnell
aws ec2 stop-instances --instance-ids i-prod123456789 --profile susan-darnell

# Test 7: Verify DBA can push container images to production
aws ecr describe-repositories --repository-names easyerp-prod --profile greta-dyson
aws ecr put-image --repository-name easyerp-prod --profile greta-dyson

# Test 8: Verify emergency deployment workflow works without environment validation
# Trigger via GitHub Actions UI - should be able to deploy to either stage or prod

# Test 9: Verify cross-environment database passwords are identical (tag-based secrets)
aws secretsmanager get-secret-value --secret-id easyerp-stage-db-credentials
aws secretsmanager get-secret-value --secret-id easyerp-prod-db-credentials
# Compare password values - should be identical (VIOLATION)

# Test 10: Verify bastion host allows broad access with improper tagging
aws ec2 describe-instances --filters "Name=tag:Environment,Values=dev" --profile alannah-rye
# Should show production bastion host tagged as 'dev' environment
ssh -i bastion-key.pem ec2-user@bastion-host
psql -h prod-db-endpoint -U easyerpuser -d easyerpdb

# Test 11: Verify tag-based access control bypass
aws ecs describe-services --cluster easyerp-stage --profile kester-ellison
aws ecs describe-services --cluster easyerp-prod --profile kester-ellison
# Both should succeed due to wildcard tag condition in TagBypassPolicy
```

#### Audit Discovery Commands
```bash
# Find ECR pushes by non-DevOps users to production resources
aws logs filter-log-events \
  --log-group-name CloudTrail/EasyERPManagement \
  --filter-pattern '{ $.eventName = "PutImage" && $.userIdentity.arn != "*joey.kuhnsman*" && $.userIdentity.arn != "*maisy.watts*" && $.requestParameters.repositoryName = "*prod*" }'

# Find direct database connections to production databases
aws logs filter-log-events \
  --log-group-name CloudTrail/EasyERPManagement \
  --filter-pattern '{ $.eventName = "Connect" && $.eventSource = "rds.amazonaws.com" && $.requestParameters.dbInstanceIdentifier = "*prod*" }'

# Find infrastructure changes by non-DevOps users on production resources
aws logs filter-log-events \
  --log-group-name CloudTrail/EasyERPManagement \
  --filter-pattern '{ ($.eventName = "UpdateService" || $.eventName = "UpdateStack") && $.userIdentity.arn != "*joey.kuhnsman*" && $.userIdentity.arn != "*maisy.watts*" && $.requestParameters.clusterName = "*prod*" }'

# Find business users accessing production technical resources
aws logs filter-log-events \
  --log-group-name CloudTrail/EasyERPManagement \
  --filter-pattern '{ ($.userIdentity.arn = "*derek.steele*" || $.userIdentity.arn = "*susan.darnell*") && ($.eventSource = "ecs.amazonaws.com" || $.eventSource = "ec2.amazonaws.com" || $.eventSource = "rds.amazonaws.com") && $.requestParameters contains "prod" }'

# Find shared credential usage patterns across environments
aws logs filter-log-events \
  --log-group-name CloudTrail/EasyERPManagement \
  --filter-pattern '{ $.userIdentity.arn = "*easyerp-shared-deploy*" }' \
  --start-time 1640995200000 \
  --end-time 1641081600000

# Find tag-based access control violations
aws logs filter-log-events \
  --log-group-name CloudTrail/EasyERPManagement \
  --filter-pattern '{ $.errorCode = "UnauthorizedOperation" && $.errorMessage contains "tag" }'

# Find users accessing resources outside their designated environment tags
aws logs filter-log-events \
  --log-group-name CloudTrail/EasyERPManagement \
  --filter-pattern '{ $.userIdentity.arn = "*alannah.rye*" && $.requestParameters contains "prod" }'

# Find improper environment tag usage
aws logs filter-log-events \
  --log-group-name CloudTrail/EasyERPManagement \
  --filter-pattern '{ $.eventName = "CreateTags" && $.requestParameters.tagSet contains "Environment" && $.requestParameters.tagSet contains "dev" && $.requestParameters.resourcesSet contains "prod" }'
```

### Phase 7: Training Scenario Setup

#### Facilitator Preparation
1. **Pre-Session Setup** (30 minutes before training):
   - Verify all user accounts are accessible
   - Confirm CloudTrail logging is active and capturing events
   - Test auditor account access to all necessary resources
   - Validate that violations are detectable through AWS Console

2. **During Training Setup** (5 minutes):
   - Provide auditor credentials to participants
   - Share EasyCo organizational chart and team responsibilities
   - Explain audit scope: Focus on segregation of duties and least privilege

3. **Discovery Phase Hints** (if participants get stuck):
   - Start with IAM user and policy review
   - Look for users with permissions beyond their job roles
   - Check CloudTrail for unusual access patterns
   - Examine GitHub repository permissions and workflow configurations
   - Review database access patterns and credential management

This comprehensive implementation guide provides everything needed to create a realistic EasyCo Manufacturing audit training environment with discoverable control weaknesses that mirror real-world scenarios auditors encounter in cloud environments.
