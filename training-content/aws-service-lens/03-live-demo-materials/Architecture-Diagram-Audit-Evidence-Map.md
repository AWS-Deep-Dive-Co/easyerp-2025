# Easy ERP Architecture Diagram & Audit Evidence Map

## Architecture Overview Diagram
*[This would be the visual diagram you show during the overview]*

```
┌─────────────────────────────────────────────────────────────────┐
│                        Internet Users                            │
└─────────────────────┬───────────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────────┐
│                 CloudFront CDN                                  │
│              (Static Assets)                                    │
└─────────────────────┬───────────────────────────────────────────┘
                      │
┌─────────────────────▼───────────────────────────────────────────┐
│                Application Load Balancer                        │
│                  (ALB - Public Subnets)                        │
└─────────────────────┬───────────────────────────────────────────┘
                      │
        ┌─────────────┼─────────────┐
        │             │             │
┌───────▼──────┐ ┌────▼────┐ ┌──────▼───────┐
│   ECS Fargate │ │ECS Fargate│ │  ECS Fargate │
│  Web Server   │ │Web Server │ │  Web Server  │
│(Private Subnet│ │(Private   │ │(Private      │
│     AZ-1)     │ │Subnet AZ-2│ │ Subnet AZ-3) │
└───────┬───────┘ └────┬────┘ └──────┬───────┘
        │              │             │
        └─────────────┬┼─────────────┘
                      ││
               ┌──────▼▼──────┐
               │  RDS Database │
               │  (PostgreSQL) │
               │   Multi-AZ    │
               │(Private Subnet│
               └───────────────┘
```

## CI/CD Pipeline Flow

```
Developer → GitHub → GitHub Actions → ECR → ECS Deployment
    │         │            │          │         │
    │         │            │          │         └─ Production
    │         │            │          └─ Container Images
    │         │            └─ Build & Test
    │         └─ Pull Request → Code Review → Merge
    └─ Feature Branch
```

---

## Audit Evidence Location Map

### 1. Change Management Evidence

#### GitHub Repository Evidence
| Control | Evidence Location | What to Look For |
|---------|------------------|------------------|
| Branch Protection | Settings → Branches | Required reviewers, status checks |
| Pull Request History | Pull requests tab | Review approvals, merge patterns |
| Workflow Controls | .github/workflows/ | Deployment triggers, approvals |
| Code Review Process | Pull request comments | Review quality, approver identity |

#### AWS CloudTrail Evidence
| Event Type | Filter | Audit Significance |
|------------|--------|-------------------|
| ECR Image Push | `eventName = PutImage` | Who deployed what container |
| ECS Deployments | `eventName = UpdateService` | Service updates and timing |
| CloudFormation Changes | `eventSource = cloudformation.amazonaws.com` | Infrastructure modifications |
| IAM Changes | `eventSource = iam.amazonaws.com` | Permission modifications |

### 2. Segregation of Duties Evidence

#### IAM Access Analysis
| Role/User | Expected Access | Red Flags to Look For |
|-----------|----------------|----------------------|
| Developer | ECR read-only, ECS task logs | ECR push to production, RDS access |
| DevOps Engineer | Full ECS, ECR, CloudFormation | Direct database access |
| Database Admin | RDS management only | ECS or ECR permissions |
| Auditor | Read-only CloudTrail, logs | Any write permissions |

#### Environment Separation Check
| Environment | Resource Naming | Access Pattern |
|-------------|----------------|----------------|
| Development | `*-dev-*` | Developers have full access |
| Staging | `*-stage-*` | Limited developer access |
| Production | `*-prod-*` | No developer access |

---

## Hidden "Easter Eggs" Reference Guide
*[For facilitator use - don't share with participants]*

### Change Management Violations

#### 1. Forced Production Deployment
**Location**: `.github/workflows/production_deployment.yml`
**Line**: `workflow_dispatch:` 
**Issue**: Allows manual bypass of normal deployment controls
**Evidence**: GitHub Actions history showing manual triggers

#### 2. Missing Required Reviewers  
**Location**: GitHub Settings → Branches → main branch protection
**Issue**: No required reviewers configured
**Evidence**: Pull requests merged without reviews

#### 3. Test Bypass Capability
**Location**: `.github/workflows/` files
**Issue**: Commented out test steps or continue-on-error
**Evidence**: Workflow files with disabled tests

#### 4. Direct Database Access
**Location**: CloudFormation bastion.yaml
**Issue**: Bastion host with overly broad security group access
**Evidence**: Security group rules, CloudTrail database access

### SOD Violations

#### 1. Developer ECR Production Access
**Location**: IAM User/Role policies
**Issue**: Developer account has `ecr:PutImage` to production registry
**Evidence**: IAM policy analysis, CloudTrail ECR events

#### 2. Shared Environment Credentials
**Location**: GitHub Secrets, IAM roles
**Issue**: Same AWS credentials used for staging and production
**Evidence**: GitHub repository secrets, IAM role trust policies

#### 3. Excessive DevOps Permissions
**Location**: IAM DevOps role
**Issue**: Single role with admin access across all environments
**Evidence**: IAM policy analysis showing broad permissions

#### 4. Database Credential Sharing
**Location**: CloudFormation parameters, Secrets Manager
**Issue**: Same database credentials for staging and production
**Evidence**: RDS configuration, Secrets Manager entries

---

## Facilitator Demo Script

### Opening (2 minutes)
*"Welcome to Easy ERP - our 3-tier web application. This represents a typical modern cloud application you'll encounter in your audits. Let me show you how we develop, test, and deploy changes, and I want you to think like auditors - what controls do you see, what evidence would you collect, and what could go wrong?"*

### Architecture Walkthrough (3 minutes)
- **Presentation Tier**: *"Users access through ALB, static content via CloudFront"*
- **Application Tier**: *"ECS containers auto-scale based on demand"*  
- **Data Tier**: *"RDS with multi-AZ for high availability"*
- **Key Audit Point**: *"Notice the separation between public and private subnets - this is a security control"*

### CI/CD Process Demo (10 minutes)

#### Development Flow:
1. *"Developers create feature branches"* - Show GitHub branches
2. *"Pull requests require reviews"* - Show PR process (**Easter Egg**: No required reviewers)
3. *"Automated tests run on every commit"* - Show GitHub Actions (**Easter Egg**: Tests can be bypassed)

#### Deployment Flow:
1. *"Staging deploys automatically on stage branch"* - Show staging workflow
2. *"Production requires manual approval"* - Show production workflow (**Easter Egg**: Manual bypass available)
3. *"Container images stored in ECR"* - Show ECR repositories (**Easter Egg**: Developer access to prod ECR)

### Infrastructure Management (5 minutes)
- *"Infrastructure as Code using CloudFormation"* - Show templates
- *"Changes tracked in CloudTrail"* - Show CloudTrail events
- *"Environment separation through naming conventions"* - Show resource naming (**Easter Egg**: Shared credentials)

---

## Participant Discovery Worksheet

### Change Management Assessment
| Control Area | Evidence Found | Pass/Fail | Notes |
|--------------|----------------|-----------|-------|
| Code Reviews Required | | | |
| Test Gates Enforced | | | |
| Production Deployment Approval | | | |
| Change Documentation | | | |
| Rollback Procedures | | | |

### SOD Assessment  
| Separation Area | Evidence Found | Pass/Fail | Notes |
|-----------------|----------------|-----------|-------|
| Dev vs Prod Access | | | |
| Database Access Controls | | | |
| Infrastructure Permissions | | | |
| Container Registry Access | | | |
| Cross-Environment Isolation | | | |

### Red Flags Identified
1. ________________________________
2. ________________________________  
3. ________________________________
4. ________________________________
5. ________________________________

### Recommendations
1. ________________________________
2. ________________________________
3. ________________________________

This comprehensive activity provides realistic audit experience with actual control weaknesses that participants must discover and evaluate.
