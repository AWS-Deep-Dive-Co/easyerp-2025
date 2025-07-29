# Team Access Review - EasyCo Manufacturing
## Easy ERP Development Team Structure

**Your Task**: Review each team member's access levels and identify any violations of segregation of duties or least privilege principles.

---

## Team Members & Their Roles

### **1. Alannah Rye - Junior Developer**
**Job Responsibilities**:
- Develops new features for the Easy ERP application under senior developer supervision
- Fixes minor bugs and implements code changes based on detailed specifications
- Writes unit tests for individual functions and components
- Participates in code reviews as a learning exercise
- Works primarily in development environment with occasional staging access for testing
- Reports to Senior Developer and requires approval for all production-related activities
- Focuses on frontend user interface development and basic backend API endpoints

**Expected Access Levels**:
- **GitHub**: Read access, can create feature branches, cannot push to main/stage, cannot approve own PRs
- **AWS**: Development environment only - ECS/ECR/CloudWatch/S3 for dev environment
- **Should NOT have**: Production access, staging access, IAM management, database credentials

---

### **2. Lorin Richards - Senior Developer**
**Job Responsibilities**:
- Leads development of complex features and system integrations for Easy ERP
- Mentors junior developers and conducts code reviews for quality assurance
- Designs technical solutions and makes architectural decisions for application components
- Troubleshoots production issues and provides technical guidance during incidents
- Coordinates with DevOps team for deployment planning and release management
- Has authority to approve code changes and merge pull requests from other developers
- Responsible for ensuring code quality standards and development best practices
- Occasionally needs staging environment access to test integration scenarios

**Expected Access Levels**:
- **GitHub**: Read/write to feature branches, can push to develop, can approve PRs (not own), cannot push to main/stage
- **AWS**: Development + limited staging - ECS/ECR/CloudWatch/S3 for dev and staging environments
- **Should NOT have**: Production resources, IAM policies, RDS master credentials

---

### **3a. Kester Ellison - QA Analyst**
### **3b. Alex Guenther - QA Analyst**
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

**Expected Access Levels**:
- **GitHub**: Read access to all branches, can comment on PRs, can trigger test workflows, cannot approve code changes
- **AWS**: Testing environments only - ECS/CloudWatch/S3 for dev and staging, read-only staging database access
- **Should NOT have**: Production access, infrastructure changes, user management

---

### **4. Maisy Watts - DevOps Engineer**
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

**Expected Access Levels**:
- **GitHub**: Full access to infrastructure code, can push to develop/stage, requires PR for main, can modify workflows
- **AWS**: Infrastructure management for dev/staging, read-only production access, cannot modify production IAM
- **Should NOT have**: Unrestricted production access, ability to bypass approval processes

---

### **5. Joey Kuhnsman - Senior DevOps Engineer**
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

**Expected Access Levels**:
- **GitHub**: Full access including settings, can manage production secrets, admin rights
- **AWS**: Full access to all environments with approval requirements, emergency access capabilities, IAM management with logging
- **Should have**: All actions logged and reviewed monthly

---

### **6. Greta Dyson - Database Administrator**
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

**Expected Access Levels**:
- **GitHub**: Read access to database migration scripts, can create PRs for database changes, required reviewer for database changes
- **AWS**: Database focus only - RDS, S3 backup buckets, CloudWatch database monitoring, Secrets Manager for credentials
- **Should NOT have**: ECS, ECR, or application deployment permissions

---

### **7. Derek Steele - Business Analyst**
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

**Expected Access Levels**:
- **GitHub**: Read-only access to documentation, can create business requirement issues
- **AWS**: Business monitoring only - CloudWatch dashboards (read-only), Cost Explorer (read-only), S3 business reports (read-only)
- **Should NOT have**: Infrastructure resources, databases, deployment tools, system configuration access

---

### **8. Susan Darnell - Treasury/Cost Management Specialist**
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

**Expected Access Levels**:
- **GitHub**: Read-only access to infrastructure documentation for cost planning, can create cost-related issues
- **AWS**: Financial management focus - Cost Explorer (full access), CloudWatch utilization metrics (read-only), Resource Groups (read-only), Trusted Advisor (read-only)
- **Should NOT have**: Infrastructure deployment, application services, databases, system modifications

---

## Your Audit Tasks

### **1. Access Review Checklist**
For each team member, verify:
- [ ] **Job Function Alignment**: Does their access align with their job responsibilities?
- [ ] **Least Privilege**: Do they have only the minimum access needed for their role?
- [ ] **Environment Separation**: Are development, staging, and production properly segregated?
- [ ] **Approval Processes**: Are appropriate approval workflows in place for sensitive actions?
- [ ] **Cross-Functional Boundaries**: Can team members access systems outside their expertise area?

### **2. Key Questions to Investigate**
1. Can any team member deploy to production without proper approval?
2. Do any non-technical users have technical system access?
3. Are database credentials properly segregated between environments?
4. Can business users make operational changes that could affect system stability?
5. Are there shared accounts or credentials being used across environments?
6. Do developers have direct access to production databases?
7. Can QA analysts modify production infrastructure?
8. Are emergency deployment processes properly controlled?

### **3. Where to Find Evidence**

#### **GitHub Repository Evidence**:
- Settings → Branches → Branch protection rules
- Settings → Manage access → Collaborator permissions
- Actions tab → Workflow runs and permissions
- .github/workflows/ → Workflow file contents
- Pull requests → Review and approval history

#### **AWS Console Evidence**:
- IAM → Users → Attached policies and permissions
- IAM → Roles → Trust relationships and attached policies
- ECR → Repositories → Permissions
- CloudTrail → Event history → Filter by user and service
- CloudFormation → Stacks → Events and resource changes
- ECS → Clusters → Services → Deployment history
- Secrets Manager → Secrets → Access policies

### **4. Documentation Template**

#### **Access Violations Found**:
| Team Member | Role | Violation Identified | Severity | Evidence Location |
|-------------|------|---------------------|----------|-------------------|
| | | | | |
| | | | | |
| | | | | |

#### **Recommendations**:
1. **Immediate Actions Required**:
   - 
   - 
   -

2. **Process Improvements**:
   - 
   - 
   -

3. **Ongoing Monitoring**:
   - 
   - 
   -

---

## Audit Approach Guidelines

### **Risk-Based Focus Areas**:
1. **High Risk**: Production access by non-production roles
2. **Medium Risk**: Cross-functional access beyond job requirements  
3. **Low Risk**: Excessive permissions within appropriate environments

### **Testing Methodology**:
1. **Review job descriptions** against actual access granted
2. **Trace sample transactions** through the deployment pipeline
3. **Test segregation of duties** by attempting unauthorized actions
4. **Validate approval processes** by reviewing recent deployment history
5. **Check for shared credentials** across multiple environments

### **Red Flags to Watch For**:
- Junior staff with senior-level permissions
- Business users with technical system access
- Same credentials used across multiple environments
- Emergency procedures that bypass all controls
- Cross-role access that enables privilege escalation

Use this guide to systematically evaluate each team member's access and identify control weaknesses in EasyCo's cloud environment.
