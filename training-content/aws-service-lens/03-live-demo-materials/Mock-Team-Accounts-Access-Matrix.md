# Mock Team Accounts & Access Matrix
## EasyCo Manufacturing Development Team

### Team Structure & Appropriate Access Levels

#### 1. **Alannah Rye - Junior Developer**
**Job Responsibilities**:
- Develops new features for the Easy ERP application under senior developer supervision
- Fixes minor bugs and implements code changes based on detailed specifications
- Writes unit tests for individual functions and components
- Participates in code reviews as a learning exercise
- Works primarily in development environment with occasional staging access for testing
- Reports to Senior Developer and requires approval for all production-related activities
- Focuses on frontend user interface development and basic backend API endpoints

**GitHub Access (Appropriate)**:
- Repository: Read access to main repository
- Branch permissions: Can create feature branches, cannot push to `main` or `stage`
- Pull requests: Can create PRs, cannot approve own PRs
- Actions: Can view workflow runs, cannot modify workflow files
- Settings: No access to repository settings

**AWS Access (Appropriate)**:
- **Development Environment Only**:
  - ECS: Read-only access to resources tagged `Environment=dev` only
  - ECR: Pull images from repositories tagged `Environment=dev` 
  - CloudWatch: Read logs for dev environment services (tag-filtered)
  - S3: Read/write access to buckets tagged `Environment=dev` only
- **No Access**: Resources tagged `Environment=stage` or `Environment=prod`, IAM management, database credentials

#### 2. **Lorin Richards - Senior Developer**
**Job Responsibilities**:
- Leads development of complex features and system integrations for Easy ERP
- Mentors junior developers and conducts code reviews for quality assurance
- Designs technical solutions and makes architectural decisions for application components
- Troubleshoots production issues and provides technical guidance during incidents
- Coordinates with DevOps team for deployment planning and release management
- Has authority to approve code changes and merge pull requests from other developers
- Responsible for ensuring code quality standards and development best practices
- Occasionally needs staging environment access to test integration scenarios

**GitHub Access (Appropriate)**:
- Repository: Read/write access to feature branches
- Branch permissions: Can push to `develop` branch, cannot push to `main` or `stage`
- Pull requests: Can create and approve PRs (but not own PRs)
- Code review: Can review and approve other developers' PRs
- Actions: Can view workflow runs, cannot modify workflow files

**AWS Access (Appropriate)**:
- **Development + Limited Staging**:
  - ECS: Read access to resources tagged `Environment=dev` or `Environment=stage`, can restart dev tasks
  - ECR: Pull from all repositories, push only to repositories tagged `Environment=dev`
  - CloudWatch: Read logs for resources tagged `Environment=dev` or `Environment=stage`
  - S3: Full access to buckets tagged `Environment=dev`, read-only access to buckets tagged `Environment=stage`
- **No Access**: Resources tagged `Environment=prod`, IAM policies, RDS master credentials

#### 3a. **Kester Ellison - QA Analyst**
#### 3b. **Alex Guenther - QA Analyst**
**Job Responsibilities**:
- Develops and executes comprehensive test plans for Easy ERP application releases
- Performs manual and automated testing across development and staging environments
- Creates and maintains test data sets and validates data integrity after deployments
- Documents bugs, tracks defect resolution, and verifies fixes before release approval
- Conducts user acceptance testing and validates business requirements compliance
- Coordinates with development team to understand new features and testing requirements
- Ensures all testing is completed in non-production environments only
- Reports quality metrics and testing progress to project management
- Has no responsibility for production systems or infrastructure changes

**GitHub Access (Appropriate)**:
- Repository: Read access to all branches
- Pull requests: Can comment on PRs, cannot approve code changes
- Actions: Can trigger test workflows, view test results
- Issues: Can create and manage issues/bugs

**AWS Access (Appropriate)**:
- **Testing Environments**:
  - ECS: Read access to resources tagged `Environment=dev` or `Environment=stage`, can restart staging tasks for testing
  - CloudWatch: Read logs and metrics for resources tagged `Environment=dev` or `Environment=stage`
  - S3: Read access to buckets tagged `DataType=test-data`, write access to buckets tagged `DataType=qa-results`
  - RDS: Read-only access to databases tagged `Environment=stage` through application connection
- **No Access**: Resources tagged `Environment=prod`, infrastructure changes, user management

#### 4. **Maisy Watts - DevOps Engineer**
**Job Responsibilities**:
- Manages CI/CD pipelines and automated deployment processes for Easy ERP
- Maintains and updates infrastructure-as-code templates and deployment scripts
- Monitors application performance and system health across development and staging environments
- Implements security best practices and manages non-production environment configurations
- Coordinates with development team for deployment planning and release scheduling
- Troubleshoots deployment issues and provides technical support for development workflows
- Manages development and staging environment resources and access controls
- Requires approval from Senior DevOps Engineer for any production-related changes
- Responsible for maintaining deployment documentation and runbooks

**GitHub Access (Appropriate)**:
- Repository: Full access to infrastructure code and workflows
- Branch permissions: Can push to `develop` and `stage`, requires PR for `main`
- Actions: Can modify workflow files, manage secrets (non-production)
- Settings: Can modify branch protection rules for non-production branches

**AWS Access (Appropriate)**:
- **Infrastructure Management**:
  - CloudFormation: Full access to stacks tagged `Environment=dev` or `Environment=stage`, read-only to stacks tagged `Environment=prod`
  - ECS: Full access to clusters tagged `Environment=dev` or `Environment=stage`, limited production access
  - ECR: Full access to repositories tagged `Environment=dev` or `Environment=stage`, read-only to repositories tagged `Environment=prod`
  - IAM: Can manage roles for non-production environments, cannot modify production IAM
  - CloudWatch/CloudTrail: Full access for monitoring setup across all environments
- **Production**: Requires approval workflow for changes to resources tagged `Environment=prod`

#### 5. **Joey Kuhnsman - Senior DevOps Engineer**
**Job Responsibilities**:
- Oversees all production infrastructure and deployment operations for Easy ERP
- Makes final approval decisions for production deployments and infrastructure changes
- Manages enterprise-level security policies and compliance requirements
- Handles emergency production incidents and has authority for emergency deployments
- Designs and implements disaster recovery and business continuity procedures
- Manages production monitoring, alerting, and performance optimization
- Supervises junior DevOps engineers and reviews all infrastructure changes
- Coordinates with security team and management for compliance and audit requirements
- Has ultimate responsibility for production system stability and security
- Authority to override normal approval processes during critical business emergencies

**GitHub Access (Appropriate)**:
- Repository: Full access including settings
- Branch permissions: Can push to all branches with approval
- Actions: Full workflow management, can manage production secrets
- Admin: Can modify repository settings and branch protection

**AWS Access (Appropriate)**:
- **Production Access**: Full access to resources in all environments with approval requirements
- **Emergency Access**: Can bypass normal approval for critical issues on resources tagged `Environment=prod`
- **IAM Management**: Can create/modify roles but with logging requirements
- **Audit Trail**: All actions logged and reviewed monthly, especially for production-tagged resources

#### 6. **Greta Dyson - Database Administrator**
**Job Responsibilities**:
- Manages all database systems including design, optimization, and maintenance for Easy ERP
- Performs database backups, recovery procedures, and disaster recovery planning
- Monitors database performance, implements tuning, and manages capacity planning
- Handles database security including user access management and credential rotation
- Coordinates with development team for database schema changes and migrations
- Ensures database compliance with data retention and security policies
- Manages database patching, upgrades, and maintenance windows
- Provides database expertise for troubleshooting and performance optimization
- Has no responsibilities for application code, containers, or infrastructure deployment
- Focus is exclusively on data tier management and database operations

**GitHub Access (Appropriate)**:
- Repository: Read access to database migration scripts
- Branch permissions: Can create PRs for database changes
- Pull requests: Required reviewer for database-related changes

**AWS Access (Appropriate)**:
- **Database Focus**:
  - RDS: Full access to manage databases in all environments (tag-independent for data operations)
  - S3: Access to buckets tagged `Purpose=database-backup`
  - CloudWatch: Database performance monitoring across all environment tags
  - Secrets Manager: Can rotate database credentials for all environments
- **Limited Access**: No ECS, ECR, or application deployment permissions regardless of environment tags

#### 7. **Derek Steele - Business Analyst**
**Job Responsibilities**:
- Analyzes Easy ERP application performance metrics to support business decision-making
- Creates reports on system usage, user adoption, and business process efficiency
- Monitors application performance dashboards to identify business impact of technical issues
- Coordinates with development team to gather requirements for new features based on usage data
- Validates that system performance meets business requirements and SLA commitments
- Provides business context for prioritizing technical improvements and bug fixes 
- Reviews CloudWatch dashboards to understand business process performance trends
- Has no responsibility for system configuration, deployments, or technical infrastructure
- Focus is exclusively on business impact analysis and requirements gathering

**GitHub Access (Appropriate)**:
- Repository: Read-only access to documentation and requirements
- Issues: Can create business requirement issues and feature requests
- No access to code, workflows, or repository settings

**AWS Access (Appropriate)**:
- **Business Monitoring Only**:
  - CloudWatch: Read-only access to business metric dashboards and application performance (environment-independent for business metrics)
  - Cost Explorer: Read-only access to view cost trends and usage patterns across all environments
  - S3: Read-only access to buckets tagged `DataType=business-reports`
- **No Access**: Infrastructure resources, databases, deployment tools, or system configuration regardless of environment tags

#### 8. **Susan Darnell - Treasury/Cost Management Specialist**
**Job Responsibilities**:
- Monitors and analyzes AWS spending across all environments to ensure budget compliance
- Creates cost allocation reports by department, project, and environment for financial planning
- Identifies cost optimization opportunities and works with technical teams on implementation
- Manages AWS budgets, alerts, and cost controls to prevent unexpected spending
- Coordinates with finance team for monthly cloud spending reconciliation and reporting
- Reviews resource utilization to identify unused or underutilized AWS resources
- Ensures proper cost tagging and allocation across business units and projects
- Provides financial impact analysis for proposed infrastructure changes
- Has no responsibility for technical implementation or system configuration
- Focus is exclusively on financial management and cost optimization of cloud resources

**GitHub Access (Appropriate)**:
- Repository: Read-only access to infrastructure documentation for cost planning
- Issues: Can create cost-related issues and optimization suggestions
- No access to code, workflows, or technical configurations

**AWS Access (Appropriate)**:
- **Financial Management Focus**:
  - Cost Explorer: Full access to cost analysis, budgets, and billing dashboards across all environments
  - CloudWatch: Read-only access to resource utilization metrics (tag-independent for cost analysis)
  - Resource Groups: Read-only access to view resource tagging and organization
  - Trusted Advisor: Read-only access to cost optimization recommendations
  - S3: Read-only access to buckets tagged `DataType=cost-reports`
- **No Access**: Infrastructure deployment, application services, databases, or system modifications regardless of environment tags

---

## Easter Egg Access Violations

### **HIGH SEVERITY - Clear SOD Violations**

#### 1. **Alannah Rye (Junior Developer) - Excessive Production Access**
**Violation**: Production ECR push permissions through tag-based policy bypass
**GitHub**: 
- Added as repository admin (can modify settings)
- Can approve own pull requests (bypass review)
**AWS**:
- `ecr:PutImage` permission on repositories tagged `Environment=prod`
- Read access to production RDS credentials in Secrets Manager tagged `Environment=prod`
- Write access to S3 buckets tagged `Environment=prod`

**Audit Trail Evidence**:
```json
{
  "eventName": "PutImage",
  "userIdentity": {
    "userName": "alannah.rye",
    "type": "IAMUser"
  },
  "sourceIPAddress": "192.168.1.100",
  "requestParameters": {
    "repositoryName": "easyerp-prod"
  },
  "resources": [
    {
      "resourceName": "easyerp-prod-ecr",
      "tags": {
        "Environment": "prod"
      }
    }
  ]
}
```

#### 2. **Lorin Richards (Senior Developer) - Database Access**
**Violation**: Direct database access to production databases through tag-based policy
**AWS**:
- RDS master user credentials for databases tagged `Environment=prod`
- Can connect directly to production database bypassing application
- CloudFormation permissions to modify security groups tagged `Environment=prod`

**Evidence Location**: CloudTrail events showing direct RDS connections to production-tagged databases from developer IP

#### 3. **Kester Ellison (QA) - Infrastructure Modification**
**Violation**: Can modify production infrastructure through tag-based access bypass
**GitHub**:
- Push access to `main` branch (can deploy to production)
- Can modify GitHub Actions workflow files
**AWS**:
- CloudFormation permissions for stacks tagged `Environment=prod`
- Can modify ECS task definitions for services tagged `Environment=prod`
- Tag-based policy bypass allowing wildcard environment access

### **MEDIUM SEVERITY - Shared Access Violations**

#### 4. **Maisy Watts (DevOps) - Shared Service Account**
**Violation**: Using shared AWS credentials across environment tags
**AWS**:
- Same IAM access keys used for dev, staging, and production deployments
- Shared access key stored in multiple GitHub repositories
- No rotation policy on shared credentials
- Can access resources across all environment tags with single credential set

**Evidence**: Same access key ID appearing in CloudTrail across resources tagged with different environments

#### 5. **Cross-Environment Database Credentials**
**Violation**: Same database password for staging and production environments
**AWS**:
- Secrets Manager showing identical database credentials for resources tagged `Environment=stage` and `Environment=prod`
- Connection strings pointing to different endpoints but same authentication
**GitHub**:
- Hard-coded database passwords in workflow files that work across environment tags

### **SUBTLE VIOLATIONS - Requires Deep Analysis**

#### 6. **Emergency Deployment Bypass**
**Violation**: Any developer can trigger "emergency" deployments to any environment
**GitHub**:
- Emergency deployment workflow with no approval gates
- Accessible to all repository contributors
- No audit trail requirement for emergency justification
- Can target any environment (`stage` or `prod`) without validation

**Workflow File Example**:
```yaml
name: Emergency Production Deploy
on:
  workflow_dispatch:
    inputs:
      reason:
        description: 'Emergency reason'
        required: false  # Not even required!
      target_environment:
        description: 'Target environment'
        default: 'prod'  # Defaults to production!
```

#### 7. **Bastion Host Over-Privilege**
**Violation**: Bastion host allows broad database access with improper environment tagging
**AWS**:
- Security group allows bastion access from 0.0.0.0/0
- Bastion can connect to production database from any IP
- Multiple team members have bastion SSH keys
- Bastion host tagged as `Environment=dev` but actually accesses production resources

#### 8. **Cross-Role Access**
**Violation**: Roles have excessive cross-functional permissions across environment tags
**AWS**:
- QA role can modify ECS services tagged `Environment=prod`
- Developer role can read CloudTrail logs (potential evidence tampering)
- Database admin can push container images to repositories tagged `Environment=prod`
- Tag-based policies with wildcard conditions allowing broader access than intended

#### 9. **Derek Steele (Business Analyst) - Technical Infrastructure Access**
**Violation**: Business user with technical system access to production-tagged resources
**AWS**:
- ECS permissions to restart services tagged `Environment=prod`
- IAM read access to view all user permissions and roles
- CloudFormation read access to stacks tagged `Environment=prod`
- S3 write access to buckets tagged `DataType=system-config`

**Evidence Location**: CloudTrail events showing business user accessing production-tagged technical infrastructure

#### 10. **Susan Darnell (Treasury/Cost) - Operational System Access**
**Violation**: Financial user with operational system permissions on production-tagged resources
**AWS**:
- EC2 permissions to start/stop instances tagged `Environment=prod` (for "cost savings")
- RDS permissions to modify database instance sizes for databases tagged `Environment=prod`
- Lambda permissions to view and modify function configurations
- ECS permissions to change service scaling settings for services tagged `Environment=prod`

**Evidence Location**: CloudTrail showing cost management user making operational changes to production-tagged resources

---

## Account Setup Instructions

### GitHub Repository Setup
```bash
# Add users as collaborators with different permission levels
- alannah.rye@easyco.com (Write access) # Should be Read
- lorin.richards@easyco.com (Write access) 
- kester.ellison@easyco.com (Write access) # Should be Read  
- maisy.watts@easyco.com (Admin access)
- joey.kuhnsman@easyco.com (Admin access)
- greta.dyson@easyco.com (Write access)
- derek.steele@easyco.com (Read access) # Business user - appropriate
- susan.darnell@easyco.com (Read access) # Business user - appropriate
```

### AWS IAM Setup Commands
```json
{
  "Users": [
    {
      "UserName": "alannah.rye",
      "AttachedPolicies": [
        "DeveloperAccess",
        "ProductionECRPush"  // VIOLATION
      ]
    },
    {
      "UserName": "lorin.richards", 
      "AttachedPolicies": [
        "SeniorDeveloperAccess",
        "RDSDirectAccess"  // VIOLATION
      ]
    },
    {
      "UserName": "kester.ellison",
      "AttachedPolicies": [
        "QAAccess",
        "CloudFormationFullAccess"  // VIOLATION  
      ]
    },
    {
      "UserName": "derek.steele",
      "AttachedPolicies": [
        "BusinessAnalystAccess",
        "TechnicalInfrastructureRead"  // VIOLATION
      ]
    },
    {
      "UserName": "susan.darnell",
      "AttachedPolicies": [
        "CostManagementAccess", 
        "ProductionOperationalAccess"  // VIOLATION
      ]
    }
  ]
}
```

---

## Audit Discovery Worksheet

### Team Member Access Review
| Name | Role | Expected Access | Actual Access | Violation? | Severity |
|------|------|----------------|---------------|-----------|----------|
| Alannah Rye | Jr Developer | Dev only | Prod ECR push | ✓ | High |
| Lorin Richards | Sr Developer | Dev + staging | Prod DB access | ✓ | High |
| Kester Ellison | QA Analyst | Test envs only | Prod infrastructure | ✓ | High |
| Maisy Watts | DevOps | Infra mgmt | Shared credentials | ✓ | Medium |
| Joey Kuhnsman | Sr DevOps | Full with approval | Emergency bypass | ✓ | Medium |
| Greta Dyson | DBA | Database only | Container access | ✓ | Low |
| Derek Steele | Business Analyst | Business metrics only | Technical infrastructure | ✓ | Medium |
| Susan Darnell | Treasury/Cost | Cost management only | Operational controls | ✓ | High |

### Questions for Auditors to Investigate
1. **Can a junior developer deploy code to production without approval?** 
   - Answer: Yes, through ECR push permissions to repositories tagged `Environment=prod` and emergency workflow

2. **Are database credentials properly segregated between environments?**
   - Answer: No, same credentials used for resources tagged `Environment=stage` and `Environment=prod`

3. **Can non-infrastructure team members modify production infrastructure?**
   - Answer: Yes, QA analyst has CloudFormation permissions for stacks tagged `Environment=prod`

4. **Are shared service accounts properly managed?**
   - Answer: No, same AWS keys used across all environment tags

5. **Is there proper oversight on emergency deployments?**
   - Answer: No, any contributor can trigger emergency deployment to any environment (stage/prod)

6. **Do business users have appropriate least-privilege access?**
   - Answer: No, business analyst has technical infrastructure access to production-tagged resources and treasury user can modify operational systems

7. **Can financial users make operational changes that affect system stability?**
   - Answer: Yes, treasury user can modify production-tagged resources for "cost savings"

8. **Are tag-based access controls properly implemented?**
   - Answer: No, multiple policies use wildcard conditions that bypass intended environment restrictions

9. **Is environment segregation enforced through resource tagging?**
   - Answer: No, users can access resources across environment tags through policy violations and shared credentials

10. **Are production-tagged resources properly protected from unauthorized access?**
    - Answer: No, multiple users have inappropriate access to resources tagged `Environment=prod`

This setup provides multiple layers of realistic access violations that mirror common real-world issues auditors encounter in cloud environments.
