# Mock Team Accounts & Access Matrix
## EasyCo Manufacturing Development Team

### Team Structure & Appropriate Access Levels

#### 1. **Marcus Chen - Director of IT Operations**
**Job Responsibilities**:
- Provides executive oversight for all IT operations, infrastructure, and system reliability across Easy ERP
- Has ultimate authority to approve emergency change requests and production deployments during critical business situations
- Makes strategic decisions on infrastructure investments, technology direction, and operational policies
- Coordinates with C-level executives and business stakeholders on IT strategy and budget planning
- Manages risk assessment for major system changes and ensures compliance with enterprise governance policies
- Has emergency override authority for all production systems during business-critical incidents
- Responsible for disaster recovery execution and business continuity decisions
- Supervises all DevOps, Database, and Infrastructure teams with authority to escalate or de-escalate situations
- Interfaces with external vendors, cloud providers, and enterprise security teams
- Required approver for any changes that could impact business operations or customer-facing services
- Maintains awareness of all production systems but delegates day-to-day operations to specialized teams

**GitHub Access (Expected)**:
- Repository: Owner-level access with emergency override capabilities
- Branch permissions: Can override branch protection rules during emergencies
- Actions: Full access to modify workflows and approve emergency deployments
- Admin: Complete repository administration including security settings
- Audit: Reviews all production-related changes and maintains approval audit trail

**AWS Access (Expected)**:
- **Executive Operations Access**: 
  - Full administrative access to all AWS resources across all environments with comprehensive audit logging
  - Emergency break-glass access to bypass normal approval workflows during critical incidents
  - CloudTrail: Full access to review all AWS actions and maintain security audit trails
  - Organizations: Can manage cross-account policies and emergency access procedures
  - Cost Management: Full access to budgets, cost allocation, and spending controls across all environments
  - Service Health Dashboard: Full access to monitor AWS service status and plan for service disruptions
- **Governance & Compliance**:
  - Config: Full access to compliance monitoring and configuration drift detection
  - Security Hub: Full access to security findings and compliance posture across all accounts
  - IAM: Can create emergency access policies and review all permission changes
- **Emergency Authority**: Can temporarily grant elevated access during confirmed business emergencies with full audit requirements

#### 2. **Alannah Rye - Junior Developer**
**Job Responsibilities**:
- Develops new features for the Easy ERP application under senior developer supervision
- Fixes minor bugs and implements code changes based on detailed specifications
- Writes unit tests for individual functions and components
- Participates in code reviews as a learning exercise
- Works primarily in development environment with occasional staging access for testing
- Reports to Senior Developer and requires approval for all production-related activities
- Focuses on frontend user interface development and basic backend API endpoints

**GitHub Access (Expected)**:
- Repository: Read access to main repository
- Branch permissions: Can create feature branches, cannot push to `main` or `stage`
- Pull requests: Can create PRs, cannot approve own PRs
- Actions: Can view workflow runs, cannot modify workflow files
- Settings: No access to repository settings

**AWS Access (Expected)**:
- **Development Environment Only**:
  - ECS: Read-only access to resources tagged `Environment=dev` only
  - ECR: Pull images from repositories tagged `Environment=dev` 
  - CloudWatch: Read logs for dev environment services (tag-filtered)
  - S3: Read/write access to buckets tagged `Environment=dev` only
- **No Access**: Resources tagged `Environment=stage` or `Environment=prod`, IAM management, database credentials

#### 3. **Lorin Richards - Senior Developer**
**Job Responsibilities**:
- Leads development of complex features and system integrations for Easy ERP
- Mentors junior developers and conducts code reviews for quality assurance
- Designs technical solutions and makes architectural decisions for application components
- Troubleshoots production issues and provides technical guidance during incidents
- Coordinates with DevOps team for deployment planning and release management
- Has authority to approve code changes and merge pull requests from other developers
- Responsible for ensuring code quality standards and development best practices
- Occasionally needs staging environment access to test integration scenarios

**GitHub Access (Expected)**:
- Repository: Read/write access to feature branches
- Branch permissions: Can push to `develop` branch, cannot push to `main` or `stage`
- Pull requests: Can create and approve PRs (but not own PRs)
- Code review: Can review and approve other developers' PRs
- Actions: Can view workflow runs, cannot modify workflow files

**AWS Access (Expected)**:
- **Development + Limited Staging**:
  - ECS: Read access to resources tagged `Environment=dev` or `Environment=stage`, can restart dev tasks
  - ECR: Pull from all repositories, push only to repositories tagged `Environment=dev`
  - CloudWatch: Read logs for resources tagged `Environment=dev` or `Environment=stage`
  - S3: Full access to buckets tagged `Environment=dev`, read-only access to buckets tagged `Environment=stage`
- **No Access**: Resources tagged `Environment=prod`, IAM policies, RDS master credentials

#### 4a. **Kester Ellison - QA Analyst**
#### 4b. **Alex Guenther - QA Analyst**
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

**GitHub Access (Expected)**:
- Repository: Read access to all branches
- Pull requests: Can comment on PRs, cannot approve code changes
- Actions: Can trigger test workflows, view test results
- Issues: Can create and manage issues/bugs

**AWS Access (Expected)**:
- **Testing Environments**:
  - ECS: Read access to resources tagged `Environment=dev` or `Environment=stage`, can restart staging tasks for testing
  - CloudWatch: Read logs and metrics for resources tagged `Environment=dev` or `Environment=stage`
  - S3: Read access to buckets tagged `DataType=test-data`, write access to buckets tagged `DataType=qa-results`
  - RDS: Read-only access to databases tagged `Environment=stage` through application connection
- **No Access**: Resources tagged `Environment=prod`, infrastructure changes, user management

#### 5. **Maisy Watts - DevOps Engineer**
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

**GitHub Access (Expected)**:
- Repository: Full access to infrastructure code and workflows
- Branch permissions: Can push to `develop` and `stage`, requires PR for `main`
- Actions: Can modify workflow files, manage secrets (non-production)
- Settings: Can modify branch protection rules for non-production branches

**AWS Access (Expected)**:
- **Infrastructure Management**:
  - CloudFormation: Full access to stacks tagged `Environment=dev` or `Environment=stage`, read-only to stacks tagged `Environment=prod`
  - ECS: Full access to clusters tagged `Environment=dev` or `Environment=stage`, limited production access
  - ECR: Full access to repositories tagged `Environment=dev` or `Environment=stage`, read-only to repositories tagged `Environment=prod`
  - IAM: Can manage roles for non-production environments, cannot modify production IAM
  - CloudWatch/CloudTrail: Full access for monitoring setup across all environments
- **Production**: Requires approval workflow for changes to resources tagged `Environment=prod`

#### 6. **Joey Kuhnsman - Senior DevOps Engineer**
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

**GitHub Access (Expected)**:
- Repository: Full access including settings
- Branch permissions: Can push to all branches with approval
- Actions: Full workflow management, can manage production secrets
- Admin: Can modify repository settings and branch protection

**AWS Access (Expected)**:
- **Production Access**: Full access to resources in all environments with approval requirements
- **Emergency Access**: Can bypass normal approval for critical issues on resources tagged `Environment=prod`
- **IAM Management**: Can create/modify roles but with logging requirements
- **Audit Trail**: All actions logged and reviewed monthly, especially for production-tagged resources

#### 7. **Greta Dyson - Database Administrator**
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

**GitHub Access (Expected)**:
- Repository: Read access to database migration scripts
- Branch permissions: Can create PRs for database changes
- Pull requests: Required reviewer for database-related changes

**AWS Access (Expected)**:
- **Database Focus**:
  - RDS: Full access to manage databases in all environments (tag-independent for data operations)
  - S3: Access to buckets tagged `Purpose=database-backup`
  - CloudWatch: Database performance monitoring across all environment tags
  - Secrets Manager: Can rotate database credentials for all environments
- **Limited Access**: No ECS, ECR, or application deployment permissions regardless of environment tags

#### 8. **Derek Steele - Business Analyst**
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

**GitHub Access (Expected)**:
- Repository: Read-only access to documentation and requirements
- Issues: Can create business requirement issues and feature requests
- No access to code, workflows, or repository settings

**AWS Access (Expected)**:
- **Business Monitoring Only**:
  - CloudWatch: Read-only access to business metric dashboards and application performance (environment-independent for business metrics)
  - Cost Explorer: Read-only access to view cost trends and usage patterns across all environments
  - S3: Read-only access to buckets tagged `DataType=business-reports`
- **No Access**: Infrastructure resources, databases, deployment tools, or system configuration regardless of environment tags

#### 9. **Susan Darnell - Treasury/Cost Management Specialist**
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

**GitHub Access (Expected)**:
- Repository: Read-only access to infrastructure documentation for cost planning
- Issues: Can create cost-related issues and optimization suggestions
- No access to code, workflows, or technical configurations

**AWS Access (Expected)**:
- **Financial Management Focus**:
  - Cost Explorer: Full access to cost analysis, budgets, and billing dashboards across all environments
  - CloudWatch: Read-only access to resource utilization metrics (tag-independent for cost analysis)
  - Resource Groups: Read-only access to view resource tagging and organization
  - Trusted Advisor: Read-only access to cost optimization recommendations
  - S3: Read-only access to buckets tagged `DataType=cost-reports`
- **No Access**: Infrastructure deployment, application services, databases, or system modifications regardless of environment tags