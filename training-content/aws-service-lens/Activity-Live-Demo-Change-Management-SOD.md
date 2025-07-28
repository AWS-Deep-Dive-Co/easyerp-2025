# Live Demo Activity: Change Management & IT SOD Controls
## Easy ERP Application - Mock Audit Walkthrough

### Exercise Introduction

You are auditing the IT environment for a medium-sized commercial client, **EasyCo Manufacturing**. EasyCo recently started seeing the advantages of cloud computing and began moving some of their infrastructure over to AWS as their designated cloud service provider. Their flagship business application, "Easy ERP," handles critical financial processes including accounts payable, inventory management, and financial reporting.

As a recently AWS-certified auditor, EasyCo's management has scheduled a walkthrough with you and provided an account in their AWS environment. The Chief Technology Officer mentioned that they've implemented "modern DevOps practices" and are particularly proud of their automated deployment pipeline. However, during your risk assessment, you identified potential concerns around change management controls and segregation of duties in their cloud environment.

**Your audit objectives today are to**:
- Evaluate the effectiveness of change management controls in their CI/CD pipeline
- Assess segregation of duties between development, staging, and production environments  
- Identify any control weaknesses that could impact financial reporting or operational processes
- Provide recommendations for strengthening IT general controls in their cloud environment

The CTO has arranged for their Senior Architecture Engineer / DevOps Lead to walk you through the system. You have been granted appropriate read-only access to both their GitHub repository and AWS environment for audit evidence collection.

### Activity Overview
**Duration**: 45 minutes total
- **Part 1**: Architecture Overview & Preparation (10 minutes)
- **Part 2**: Live Mock Walkthrough (20 minutes) 
- **Part 3**: Hands-On Audit Testing (15 minutes)

**Scenario**: You are auditing the IT general controls for Easy ERP, a 3-tier web application. Focus on change management processes and segregation of duties (SOD) controls in the CI/CD pipeline.

---

## Part 1: Architecture Overview & Preparation (10 minutes)

### Easy ERP Application Architecture

**3-Tier Architecture Components**:
1. **Presentation Tier**: 
   - Load Balancer (ALB)
   - ECS Fargate containers serving web application
   - CloudFront CDN for static assets

2. **Application Tier**:
   - ECS cluster with Docker containers
   - Auto-scaling groups for high availability
   - ECR (Elastic Container Registry) for image storage

3. **Data Tier**:
   - RDS PostgreSQL database (multi-AZ)
   - S3 buckets for file storage
   - ElastiCache for session management

### CI/CD Pipeline Components
- **Source Control**: GitHub repository with branch protection
- **Build Process**: GitHub Actions workflows
- **Artifact Storage**: ECR for container images
- **Deployment**: Automated through GitHub Actions
- **Infrastructure**: CloudFormation templates
- **Monitoring**: CloudWatch and CloudTrail

### Participant Preparation Tasks (5-10 minutes)
Review the following before the walkthrough:

1. **GitHub Repository Structure**:
   - Main branches: `main` (production), `stage` (staging), `develop`
   - CloudFormation templates in `/Cloudformation` folder
   - Application code structure
   - GitHub Actions workflows in `.github/workflows/`

2. **AWS Environment Access**:
   - AWS Management Console access provided
   - Focus areas: ECS, ECR, CloudFormation, IAM, CloudTrail
   - Note: You have read-only access for audit purposes

3. **Audit Focus Areas**:
   - **Change Management**: How are code changes controlled from development to production?
   - **Segregation of Duties**: Who can do what in the deployment pipeline?
   - **Approval Processes**: What controls exist for production deployments?
   - **Access Controls**: How are permissions managed across environments?

---

## Part 2: Live Mock Walkthrough (20 minutes)

### Facilitator Role: Senior Architecture Engineer / DevOps Lead
*"I'll walk you through our Easy ERP application and deployment process. Feel free to interrupt with questions about controls, approvals, or access. When you ask for audit evidence, I'll show you exactly where to find it."*

### Walkthrough Sequence

#### 1. Development Process (5 minutes)
**Topic**: "How developers make changes"
- Show GitHub repository structure
- Explain branch protection rules
- Demonstrate pull request process
- **Audit Questions to Expect**:
  - "Who can approve pull requests?"
  - "What testing is required before merge?"
  - "How do you prevent direct commits to main?"

#### 2. Build & Test Process (5 minutes)
**Topic**: "Automated testing and building"
- Show GitHub Actions workflows
- Explain test automation
- Demonstrate Docker image building
- **Audit Questions to Expect**:
  - "What happens if tests fail?"
  - "Who can modify workflow files?"
  - "How are build artifacts secured?"

#### 3. Deployment Process (5 minutes)
**Topic**: "Staging and production deployment"
- Show staging deployment workflow
- Explain production deployment process
- Demonstrate environment promotion
- **Audit Questions to Expect**:
  - "What approvals are required for production?"
  - "Can developers deploy directly to production?"
  - "How do you handle emergency deployments?"

#### 4. Infrastructure Management (5 minutes)
**Topic**: "Infrastructure as Code"
- Show CloudFormation templates
- Explain infrastructure deployment
- Demonstrate change tracking
- **Audit Questions to Expect**:
  - "Who can modify infrastructure?"
  - "How are infrastructure changes approved?"
  - "What's the rollback process?"

### Hidden "Easter Eggs" for Audit Discovery

#### Change Management Issues:
1. **Forced Deployment**: Production workflow has `workflow_dispatch` allowing manual deployment bypass
2. **Missing Approval**: No required reviewers on critical branch protection
3. **Test Bypass**: Commented out test steps in GitHub Actions
4. **Direct Database Access**: Bastion host with overly broad access

#### SOD Violations:
1. **Developer ECR Access**: Developer account has `ecr:PutImage` permissions to production ECR
2. **Shared Secrets**: Same AWS credentials used across multiple environments
3. **Admin Access**: Single "DevOps" role with excessive permissions
4. **Production Database**: Same credentials for staging and production databases

---

## Part 3: Hands-On Audit Testing (15 minutes)

### Individual/Team Tasks
**Instructions**: "Now it's your turn to audit. Use your AWS console access and GitHub repository access to validate controls."

### Testing Checklist

#### Change Management Controls Testing
- [ ] **Branch Protection**: Verify main branch requires pull request reviews
- [ ] **Required Reviews**: Check if production deployments require approval
- [ ] **Test Gates**: Confirm tests must pass before deployment
- [ ] **Deployment Authorization**: Validate who can trigger production deployments
- [ ] **Change Documentation**: Review if changes are properly documented
- [ ] **Rollback Procedures**: Verify rollback capabilities exist

#### Segregation of Duties Testing  
- [ ] **Developer Permissions**: Check if developers can deploy to production
- [ ] **Environment Separation**: Verify staging and production use different credentials
- [ ] **Administrative Access**: Review who has admin rights to AWS resources
- [ ] **Database Access**: Check if same accounts access staging and production data
- [ ] **Infrastructure Changes**: Verify who can modify CloudFormation templates
- [ ] **Secret Management**: Review how sensitive credentials are managed

### Where to Find Evidence

#### GitHub Repository Evidence:
- **Branch Protection**: Settings → Branches → Branch protection rules
- **Workflow Permissions**: `.github/workflows/` files → permissions sections
- **Required Reviews**: Pull request settings and history
- **Deployment History**: Actions tab → Workflow runs

#### AWS Console Evidence:
- **IAM Permissions**: IAM → Users/Roles → Attached policies
- **ECR Access**: ECR → Repository → Permissions
- **CloudTrail Logs**: CloudTrail → Event history (filter by service)
- **CloudFormation**: CloudFormation → Stacks → Events and Resources
- **ECS Deployments**: ECS → Clusters → Services → Deployment history

### Audit Questions to Research
1. Can a single developer deploy code to production without approval?
2. Do staging and production environments use the same database credentials?
3. Can someone modify infrastructure without going through the standard process?
4. Are there adequate controls to prevent unauthorized ECR image pushes?
5. Is there proper separation between development and production environments?

---

## Facilitator Guidance

### Responses to Common Audit Questions

#### "Show me your change management process"
- Navigate to GitHub repository settings
- Show branch protection rules
- Demonstrate pull request workflow
- **Hidden Issue**: Point out missing required reviewers

#### "How do you control production deployments?"
- Show GitHub Actions production workflow
- Explain environment protection rules
- **Hidden Issue**: Show `workflow_dispatch` bypass option

#### "What prevents developers from accessing production?"
- Show IAM roles and policies
- Explain environment separation
- **Hidden Issue**: Show developer with ECR production access

#### "How do you track infrastructure changes?"
- Show CloudFormation stacks and events
- Demonstrate CloudTrail logging
- **Hidden Issue**: Show bastion host with excessive access

### Debrief Discussion Points (5 minutes)
1. **What control weaknesses did you identify?**
2. **How would you test these controls in a real audit?**
3. **What additional evidence would you request?**
4. **How do cloud environments change traditional SOD approaches?**
5. **What recommendations would you make to strengthen controls?**

---

## Activity Materials Needed

### Technology Access:
- [ ] AWS Management Console (read-only audit access)
- [ ] GitHub repository access
- [ ] Projector/screen for live demonstration
- [ ] Individual devices for hands-on testing

### Documentation:
- [ ] Architecture diagram (provide during overview)
- [ ] AWS account details and login instructions
- [ ] GitHub repository URL and access instructions
- [ ] This activity guide for each participant

### Facilitator Preparation:
- [ ] Review hidden "easter eggs" locations
- [ ] Test AWS console access and GitHub repository access
- [ ] Prepare architecture diagram presentation
- [ ] Set up proper IAM permissions for audit scenario

This activity provides hands-on experience with real CI/CD audit challenges while demonstrating how to find evidence in modern cloud environments.
