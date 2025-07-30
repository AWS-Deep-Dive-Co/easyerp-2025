# Live Demo Activity: Change Management & IT SOD Controls
## Easy ERP Application - Mock Audit Walkthrough
### **PARTICIPANT VERSION**

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
   - Main branches: `main` (production), `stage` (staging)
   - Branch protection rules configured for `main` and `stage` branches
   - GitHub environments set up with protection rules and environment-specific secrets
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

### Pre-Walkthrough Notes
*Use this space to jot down initial observations and questions as you review the architecture:*

**Initial Questions for the Walkthrough:**
_____________________________________________________________________________________
_____________________________________________________________________________________
_____________________________________________________________________________________

**Areas of Potential Risk I Want to Explore:**
_____________________________________________________________________________________
_____________________________________________________________________________________
_____________________________________________________________________________________

---

## Part 2: Live Mock Walkthrough (20 minutes)

### Your Role as Auditor
You'll be observing the DevOps Lead's walkthrough while actively asking questions about controls and gathering audit evidence. Think critically about what you're seeing and don't hesitate to dig deeper into areas that seem concerning.

### Walkthrough Topics & Your Focus Areas

#### 1. Development Process (5 minutes)
**Topic Overview**: How developers make changes to the application
- Observe the GitHub repository structure and branch management
- Learn about the pull request and code review process
- Understand how changes flow from development to higher environments

**Consider what questions you might ask about:**
- Authorization and approval requirements for branch merges
- Code review processes and who can perform them
- Branch protection mechanisms and their effectiveness
- Testing requirements before code integration

**Think about potential control risks in this area:**
- Unauthorized code changes bypassing branch protection
- Inadequate review processes
- Missing required reviewers or insufficient review requirements

**Notes & Questions:**
_____________________________________________________________________________________
_____________________________________________________________________________________
_____________________________________________________________________________________

#### 2. Build & Test Process (5 minutes)
**Topic Overview**: Automated testing and artifact creation
- Observe GitHub Actions workflows and automation
- Learn about test execution and quality gates
- Understand how application artifacts (Docker images) are created

**Consider what questions you might ask about:**
- Test coverage and failure handling
- Who can modify automated workflows
- Security of build artifacts and storage
- Validation steps before promoting builds

**Think about potential control risks in this area:**
- Insufficient testing or test bypasses
- Unauthorized workflow modifications
- Insecure artifact handling

**Notes & Questions:**
_____________________________________________________________________________________
_____________________________________________________________________________________
_____________________________________________________________________________________

#### 3. Deployment Process (5 minutes)
**Topic Overview**: How applications move from staging to production
- Observe staging and production deployment workflows
- Learn about environment promotion processes
- Understand deployment authorization and rollback procedures

**Consider what questions you might ask about:**
- Production deployment approvals and GitHub environment protection rules
- Emergency deployment procedures and override capabilities
- Environment separation and how secrets are managed per environment
- Rollback and recovery processes
- How environment-specific configurations are controlled

**Think about potential control risks in this area:**
- Unauthorized production deployments bypassing environment protection
- Inadequate approval processes for environment promotions
- Poor environment segregation or shared secrets across environments
- Emergency procedures that bypass normal controls

**Notes & Questions:**
_____________________________________________________________________________________
_____________________________________________________________________________________
_____________________________________________________________________________________

#### 4. Infrastructure Management (5 minutes)
**Topic Overview**: Infrastructure as Code and change management
- Observe CloudFormation templates and infrastructure deployment
- Learn about infrastructure change tracking and approval
- Understand how infrastructure changes are managed

**Consider what questions you might ask about:**
- Who can modify infrastructure configurations
- Infrastructure change approval processes
- Tracking and auditing of infrastructure changes
- Recovery and rollback procedures for infrastructure

**Think about potential control risks in this area:**
- Unauthorized infrastructure changes
- Inadequate change management for infrastructure
- Poor tracking of infrastructure modifications

**Notes & Questions:**
_____________________________________________________________________________________
_____________________________________________________________________________________
_____________________________________________________________________________________

### Areas to Watch For During the Walkthrough

**Change Management Red Flags:**
- Look for ways to bypass branch protection rules or environment protection
- Watch for missing or weak approval requirements in GitHub environments
- Notice any shortcuts or "backdoors" in the deployment process

**Segregation of Duties Concerns:**
- Pay attention to accounts with excessive permissions across environments
- Look for shared secrets between staging and production environments
- Notice if the same people/accounts can perform conflicting duties
- Observe access patterns that violate SOD principles
- Check if environment-specific secrets are properly segregated

---

## Part 3: Hands-On Audit Testing (15 minutes)

### Individual/Team Tasks
**Instructions**: Now it's your turn to audit. Use your AWS console access and GitHub repository access to validate the controls you observed during the walkthrough.

### Testing Checklist

#### Change Management Controls Testing
- [ ] **Branch Protection**: Verify main branch requires pull request reviews
  - *Notes:* ________________________________________________________________
- [ ] **Required Reviews**: Check if production deployments require approval
  - *Notes:* ________________________________________________________________
- [ ] **Test Gates**: Confirm tests must pass before deployment
  - *Notes:* ________________________________________________________________
- [ ] **Deployment Authorization**: Validate who can trigger production deployments
  - *Notes:* ________________________________________________________________
- [ ] **Change Documentation**: Review if changes are properly documented
  - *Notes:* ________________________________________________________________
- [ ] **Rollback Procedures**: Verify rollback capabilities exist
  - *Notes:* ________________________________________________________________

#### Segregation of Duties Testing  
- [ ] **Developer Permissions**: Check if developers can deploy to production
  - *Notes:* ________________________________________________________________
- [ ] **Environment Separation**: Verify staging and production use different secrets and configurations
  - *Notes:* ________________________________________________________________
- [ ] **Administrative Access**: Review who has admin rights to AWS resources
  - *Notes:* ________________________________________________________________
- [ ] **Database Access**: Check if same accounts access staging and production data
  - *Notes:* ________________________________________________________________
- [ ] **Infrastructure Changes**: Verify who can modify CloudFormation templates
  - *Notes:* ________________________________________________________________
- [ ] **Secret Management**: Review how environment-specific secrets are managed and segregated
  - *Notes:* ________________________________________________________________

### Where to Find Evidence

#### GitHub Repository Evidence:
- **Branch Protection**: Settings → Branches → Branch protection rules; OR Settings → Rules (for main and stage branches)
- **Environment Protection**: Settings → Environments → Protection rules and required reviewers
- **Environment Secrets**: Settings → Environments → Environment secrets (note separation)
- **Required Reviews**: Pull request settings and history
- **Deployment History**: Actions tab → Workflow runs and environment deployments

#### AWS Console Evidence:
- **IAM Permissions**: IAM → Users/Roles → Attached policies
- **ECR Access**: ECR → Repository → Permissions
- **CloudTrail Logs**: CloudTrail → Event history (filter by service)
- **CloudFormation**: CloudFormation → Stacks → Events and Resources
- **ECS Deployments**: ECS → Clusters → Services → Deployment history

### Key Audit Questions to Research
1. Can a single developer deploy code to production without approval?
   - *Your findings:* ________________________________________________________
2. Do staging and production environments use different secrets and configurations?
   - *Your findings:* ________________________________________________________
3. Can someone modify infrastructure without going through the standard process?
   - *Your findings:* ________________________________________________________
4. Are there adequate controls to prevent unauthorized ECR image pushes?
   - *Your findings:* ________________________________________________________
5. Is there proper separation between development and production environments?
   - *Your findings:* ________________________________________________________

### Control Weaknesses Discovery Log
*Document any control weaknesses you identify during your testing:*

**Weakness #1:**
- **Description:** _____________________________________________________________
- **Risk Impact:** ____________________________________________________________
- **Evidence Location:** ______________________________________________________

**Weakness #2:**
- **Description:** _____________________________________________________________
- **Risk Impact:** ____________________________________________________________
- **Evidence Location:** ______________________________________________________

**Weakness #3:**
- **Description:** _____________________________________________________________
- **Risk Impact:** ____________________________________________________________
- **Evidence Location:** ______________________________________________________

### Recommendations Worksheet
*Based on your findings, what would you recommend to strengthen IT general controls?*

**Recommendation #1:**
_____________________________________________________________________________________
_____________________________________________________________________________________

**Recommendation #2:**
_____________________________________________________________________________________
_____________________________________________________________________________________

**Recommendation #3:**
_____________________________________________________________________________________
_____________________________________________________________________________________

---

## Activity Materials Needed

### Technology Access:
- [ ] AWS Management Console (read-only audit access)
- [ ] GitHub repository access
- [ ] Individual devices for hands-on testing

### Documentation:
- [ ] Architecture diagram (provided during overview)
- [ ] AWS account details and login instructions
- [ ] GitHub repository URL and access instructions
- [ ] This participant guide

---

## Debrief Discussion Points (5 minutes)
*Be prepared to discuss:*

1. **What control weaknesses did you identify?**
2. **How would you test these controls in a real audit?**
3. **What additional evidence would you request from the client?**
4. **How do cloud environments change traditional SOD approaches?**
5. **What recommendations would you make to strengthen controls?**

---

*This activity provides hands-on experience with real CI/CD audit challenges while demonstrating how to find evidence in modern cloud environments.*
