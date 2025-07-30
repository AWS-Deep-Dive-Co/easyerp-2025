# Facilitator Preparation Checklist
## Setting up Easter Eggs for Change Management & SOD Demo

### Pre-Activity Setup (Complete 24-48 hours before training)

#### 1. GitHub Repository Easter Eggs

##### Change Management Issues to Plant:

- [ ] **Remove Required Reviewers**
  - Navigate to: Settings → Branches → main branch protection
  - Ensure "Require a pull request before merging" is enabled
  - **Remove** "Require approvals" or set to 0
  - Document current setting for restoration

- [ ] **Add Manual Deployment Bypass**
  - File: `.github/workflows/production_deployment.yml`
  - Ensure `workflow_dispatch:` is present (allows manual triggers)
  - Consider adding: `inputs:` section with `skip_tests: boolean` option

- [ ] **Comment Out Test Steps** 
  - File: `.github/workflows/production_deployment.yml` or `stage_deployment.yml`
  - Comment out unit test steps or add `continue-on-error: true`
  - Example: `# - name: Run tests` or `continue-on-error: true`

- [ ] **Create Emergency Deployment Workflow**
  - Create: `.github/workflows/emergency_deploy.yml`
  - Configure to skip all gates and deploy directly
  - Give it broad permissions

##### Sample Emergency Deployment File:
```yaml
name: Emergency Production Deploy
on:
  workflow_dispatch:
    inputs:
      reason:
        description: 'Emergency deployment reason'
        required: true
        type: string

jobs:
  emergency-deploy:
    runs-on: ubuntu-latest
    environment: production
    steps:
      - uses: actions/checkout@v3
      - name: Deploy without tests
        run: echo "DEPLOYING WITHOUT STANDARD CONTROLS"
      # Add actual deployment steps that bypass normal gates
```

#### 2. AWS IAM Easter Eggs

##### SOD Violations to Plant:

- [ ] **Create Developer with Production ECR Access**
  - IAM User: `developer-john-smith` 
  - Attach policy with `ecr:PutImage` on production ECR repository
  - Document for restoration: Note original permissions

- [ ] **Create Overly Permissive DevOps Role**
  - IAM Role: `DevOps-Admin-Role`
  - Attach: `AdministratorAccess` policy
  - Should have: Limited, environment-specific permissions
  - Document: Original role permissions

- [ ] **Share Database Credentials**
  - Secrets Manager: Use same secret for staging and production RDS
  - Alternative: Hard-code same credentials in CloudFormation parameters
  - Document: Separate credential setup for restoration

- [ ] **Cross-Environment Access**
  - IAM Role: `Staging-Developer-Role`
  - Add permissions to production S3 buckets or ECR repositories
  - Document: Original scope for restoration

#### 3. AWS Resource Configuration Easter Eggs

##### Infrastructure Issues to Plant:

- [ ] **Bastion Host Over-Access**
  - Security Group: Allow bastion access to production database from anywhere
  - Original: Should be restricted to specific IP ranges
  - File: `Cloudformation/infrastructure/bastion.yaml` or security groups

- [ ] **Missing Encryption**
  - RDS: Disable encryption at rest for production database
  - S3: Remove default encryption on sensitive buckets
  - Document: Encryption should be enabled

- [ ] **Shared VPC Resources**
  - Configure staging and production to share same VPC/subnets
  - Original: Should have separate VPCs for environment isolation
  - File: `Cloudformation/infrastructure/vpc.yaml`

#### 4. CloudTrail Evidence Setup

- [ ] **Ensure CloudTrail is Logging**
  - Verify CloudTrail is capturing all management events
  - Ensure data events are logged for S3 and other critical services
  - Set appropriate retention (90+ days for audit trail)

- [ ] **Create Suspicious Activity**
  - Generate some ECR pushes from developer account to production
  - Create some infrastructure changes outside normal process
  - Generate database access from non-database accounts
  - Time stamp: Day before training for recent evidence

#### 5. Test Participant Access

- [ ] **AWS Console Access**
  - Create read-only audit role: `AuditorReadOnly`
  - Permissions: CloudTrail, CloudWatch, IAM (read), ECR (read), ECS (read)
  - Test: Login and verify can view but not modify resources

- [ ] **GitHub Repository Access**
  - Add participants as repository collaborators (read access)
  - Test: Ensure they can view code, workflows, settings
  - Verify: Can see branch protection rules and workflow history

---

## During Activity - Facilitator Responses

### When Participants Ask About Specific Controls:

#### "Show me your branch protection rules"
**Response**: *"Sure, let me show you our GitHub settings."*
**Action**: Navigate to Settings → Branches
**Point Out**: *"We have pull request requirements enabled..."*
**Hidden Issue**: No required reviewers (they should notice this)
**If Missed**: *"What do you think about the approval requirements?"*

#### "How do you prevent unauthorized deployments?"
**Response**: *"Great question. Let me show you our production workflow."*
**Action**: Show `.github/workflows/production_deployment.yml`
**Point Out**: The environment protection and normal triggers
**Hidden Issue**: `workflow_dispatch` allows manual bypass
**If Missed**: *"Look at the triggers section - what do you see?"*

#### "Who can access production resources?"
**Response**: *"Let me show you our IAM setup."*
**Action**: Navigate to IAM → Users/Roles
**Point Out**: Show the different roles and their purposes
**Hidden Issue**: Developer with ECR production access
**If Missed**: *"Check the policies attached to our development users."*

### Handling Discovery of Easter Eggs:

#### When Participant Finds Missing Required Reviewers:
**Response**: *"Good catch! That's definitely a control weakness. How would you test this in a real audit?"*
**Follow-up**: *"What evidence would you look for to see if this has been exploited?"*

#### When Participant Finds Manual Deployment Bypass:
**Response**: *"Excellent finding. This is exactly the kind of thing that might slip through in a fast-moving development environment."*
**Follow-up**: *"How would you determine if this capability has been used inappropriately?"*

#### When Participant Finds SOD Violations:
**Response**: *"You've identified a significant segregation of duties issue. This is actually more common than you might think."*
**Follow-up**: *"What would you recommend to remediate this?"*

---

## Post-Activity Restoration Checklist

### GitHub Repository Restoration:
- [ ] Restore required reviewers on branch protection
- [ ] Remove or comment emergency deployment workflow
- [ ] Restore test steps in deployment workflows
- [ ] Document changes made for future training sessions

### AWS IAM Restoration:
- [ ] Remove production ECR access from developer accounts
- [ ] Restore least-privilege permissions to DevOps roles
- [ ] Separate database credentials between environments
- [ ] Remove cross-environment access permissions

### Infrastructure Restoration:
- [ ] Restore proper bastion host security group rules
- [ ] Re-enable encryption on databases and S3 buckets
- [ ] Separate VPC resources if modified
- [ ] Verify all production security controls are restored

### Documentation:
- [ ] Update training materials with any new findings
- [ ] Document participant feedback for future improvements
- [ ] Record most commonly missed issues for emphasis in future training
- [ ] Update facilitator guide based on experience

---

## Backup Plans

### If Participants Don't Find Easter Eggs:
1. **Provide Hints**: *"Let me show you something interesting I noticed..."*
2. **Ask Leading Questions**: *"What would you expect to see for production deployment approval?"*
3. **Show Directly**: *"Here's something that caught my attention during our security review..."*

### If Technology Issues Arise:
1. **GitHub Access Problems**: Use screenshots and local demo
2. **AWS Console Issues**: Prepare CloudTrail exports and IAM policy screenshots
3. **Internet Connectivity**: Have offline examples and documentation ready

### If Time Runs Short:
1. **Focus on Top 2-3 Issues**: Prioritize manual deployment bypass and SOD violations
2. **Provide Summary**: Give participants list of remaining issues to investigate
3. **Extended Discussion**: Convert remaining time to group discussion about findings

This preparation ensures a realistic, educational experience that demonstrates real-world control weaknesses while maintaining a safe training environment.
