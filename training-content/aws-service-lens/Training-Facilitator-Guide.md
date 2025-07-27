# AWS Service Overview for Auditors - Facilitator Guide

## Training Overview

**Duration**: 2 hours (including activities)
**Format**: Interactive presentation with guided demonstrations
**Audience**: Auditors, compliance professionals, risk managers
**Prerequisites**: General understanding of IT systems and audit concepts

## Training Philosophy

This training provides auditors with a **high-level understanding of AWS services** and how they appear in client environments. Focus is on audit relevance, compliance considerations, and what auditors should look for when evaluating AWS-based systems rather than technical implementation details.

---

## Session Structure (2 Hours Total)

### Pre-Session Setup (10 minutes)
**Facilitator Tasks**:
1. Deploy infrastructure 30+ minutes before session starts
2. Verify dashboard data is populating (wait 15-30 minutes after deployment)
3. Test console access and prepare demonstration screens
4. Prepare audit scenarios and compliance discussion points

**Deployment Verification Checklist**:
```bash
# Verify services are deployed and running
aws events list-rules --name-prefix aws-deep-dive
aws lambda list-functions | grep aws-deep-dive
aws stepfunctions list-state-machines | grep aws-deep-dive
aws glue get-jobs | grep aws-deep-dive
```

### Opening & Context Setting (15 minutes)
**Objectives**:
- Establish relevance for auditors
- Set expectations for service overview level
- Connect to audit frameworks (SOX, COSO, etc.)

### Segment 1: AWS Scheduling & Automation Services (25 minutes)
**Content**: EventBridge and Lambda overview
**Activity**: EventBridge Analysis Activity (10 minutes)
**Audit Focus**: Automated process controls, segregation of duties

### Segment 2: Workflow Orchestration & Data Processing (25 minutes)  
**Content**: Step Functions and Glue overview
**Activity**: Workflow Risk Assessment Activity (10 minutes)
**Audit Focus**: Process flow controls, data integrity

### Segment 3: Monitoring & Compliance (25 minutes)
**Content**: CloudWatch and CloudTrail overview  
**Activity**: Compliance Evidence Gathering Activity (10 minutes)
**Audit Focus**: Audit trails, monitoring controls

### Integration & Wrap-up (25 minutes)
**Content**: How services work together, audit implications
**Activity**: Audit Planning Discussion (15 minutes)
**Focus**: Developing audit programs for AWS environments

---

## Detailed Session Content

### Opening & Context Setting (15 minutes)

**Key Messages**:
- AWS services are increasingly common in client environments
- Understanding service capabilities helps assess control environment
- Focus on "what" services do, not "how" they work technically
- Connect to existing audit frameworks and risk assessment approaches

**Facilitator Script**:
*"Today we'll explore AWS services from an auditor's perspective. We're not learning to implement these services, but rather understanding what they do and how they might impact our audit approach when we encounter them in client environments."*

**Discussion Questions**:
- How many have encountered AWS services in recent audits?
- What challenges have you faced auditing cloud-based systems?
- How do you currently assess automated processes in traditional environments?

### Segment 1: AWS Scheduling & Automation Services (25 minutes)

**EventBridge Overview (8 minutes)**:
- **What it is**: Event-driven scheduling and automation service
- **Audit relevance**: Automates business processes, triggers other systems
- **Control considerations**: Who can modify schedules? How are changes tracked?
- **Evidence**: EventBridge rules show what processes run when

**Live Demonstration (5 minutes)**:
- Show EventBridge console with deployed rules
- Point out scheduling patterns and targets
- Highlight audit trail capabilities

**Lambda Overview (7 minutes)**:
- **What it is**: Serverless compute that runs business logic
- **Audit relevance**: Executes critical business processes automatically
- **Control considerations**: Code review, error handling, access controls
- **Evidence**: CloudWatch logs show execution history and errors

**Live Demonstration (5 minutes)**:
- Show Lambda console with deployed functions
- Demonstrate execution logs in CloudWatch
- Point out error rates and monitoring capabilities

**Activity: EventBridge Analysis (See separate activity file)**

### Segment 2: Workflow Orchestration & Data Processing (25 minutes)

**Step Functions Overview (8 minutes)**:
- **What it is**: Visual workflow orchestration service
- **Audit relevance**: Documents complex business process flows
- **Control considerations**: Who can modify workflows? Error handling adequacy?
- **Evidence**: Visual workflow diagrams, execution history

**Live Demonstration (5 minutes)**:
- Show Step Functions console with visual workflow
- Walk through workflow states and error handling
- Demonstrate execution history and debugging capabilities

**Glue Overview (7 minutes)**:
- **What it is**: Managed data processing and ETL service
- **Audit relevance**: Transforms and validates business data
- **Control considerations**: Data quality, transformation accuracy, job monitoring
- **Evidence**: Job execution logs, data lineage, error reports

**Live Demonstration (5 minutes)**:
- Show Glue console with ETL jobs
- Demonstrate job monitoring and logs
- Point out data processing capabilities

**Activity: Workflow Risk Assessment (See separate activity file)**

### Segment 3: Monitoring & Compliance (25 minutes)

**CloudWatch Overview (10 minutes)**:
- **What it is**: Comprehensive monitoring and alerting service
- **Audit relevance**: Provides operational metrics and business KPIs
- **Control considerations**: Monitoring coverage, alert thresholds, response procedures
- **Evidence**: Dashboards, metrics, automated alerts

**Live Demonstration (8 minutes)**:
- Show CloudWatch dashboards with business metrics
- Demonstrate custom metrics and alerting
- Point out compliance-relevant monitoring

**CloudTrail Overview (7 minutes)**:
- **What it is**: API auditing and governance service
- **Audit relevance**: Complete audit trail of system changes
- **Control considerations**: Log integrity, retention, analysis capabilities
- **Evidence**: API call logs, user activity, configuration changes

**Activity: Compliance Evidence Gathering (See separate activity file)**

### Integration & Wrap-up (25 minutes)

**Service Integration Discussion (10 minutes)**:
- How services work together to create business processes
- Importance of understanding service dependencies
- Audit implications of integrated vs. standalone services

**Activity: Audit Planning Discussion (15 minutes)**:
- Small group discussion: How would you audit a process using these services?
- Share approaches and challenges
- Develop audit program considerations

---

## Facilitator Tips & Techniques

### Engagement Strategies

**Audit-Focused Approach**:
- Connect every service capability to audit implications
- Use audit terminology familiar to participants
- Emphasize "what to look for" rather than "how to configure"
- Relate to traditional IT audit concepts they already know

**Interactive Demonstration**:
- Show real AWS consoles rather than just slides
- Point out specific areas auditors should examine
- Highlight audit-relevant information in each interface
- Connect demonstrations to audit evidence concepts

**Experience-Based Learning**:
- Ask participants about their current audit challenges
- Connect AWS capabilities to solving those challenges
- Encourage sharing of experiences with cloud auditing
- Build on existing audit knowledge and frameworks

### Managing Time Constraints (2 Hours)

**Stay High-Level**:
- Focus on business impact, not technical details
- Use the "so what?" test for every technical point
- Spend more time on audit implications than service features
- Keep demonstrations brief and audit-focused

**Efficient Activity Management**:
- Use timer for all activities (10 minutes maximum each)
- Circulate during activities to answer questions quickly
- Have example answers ready to share if groups struggle
- Keep discussions focused on audit relevance

### Common Challenges & Solutions

**Challenge**: "This is too technical for our audit background"
**Solution**: Emphasize that you're showing what to look for, not how to configure

**Challenge**: "How do we audit something we can't see?"
**Solution**: Focus on available audit evidence and monitoring capabilities

**Challenge**: "Our clients don't use AWS"
**Solution**: Discuss how these concepts apply to any automated systems

**Challenge**: "We don't have time to learn new technology"
**Solution**: Connect to existing audit procedures and frameworks they already use

### Presentation Tips

**Visual Focus**:
- Use actual AWS console screenshots in slides
- Show before/after states for key concepts
- Include audit trail examples in presentations
- Use flow diagrams to show process connections

**Audit Language**:
- Use terms like "controls," "evidence," "risk," "compliance"
- Avoid technical jargon like "serverless," "orchestration," "ETL"
- Connect to audit standards (COSO, COBIT, SOX)
- Frame discussions around audit objectives

---

## Learning Outcomes & Next Steps

### Key Takeaways for Auditors
1. **EventBridge**: Automated scheduling creates process controls to evaluate
2. **Lambda**: Serverless functions execute business logic that needs audit attention
3. **Step Functions**: Visual workflows provide process documentation and audit trails
4. **Glue**: Data processing services affect data integrity and quality controls
5. **CloudWatch**: Monitoring provides operational metrics and compliance evidence
6. **CloudTrail**: API logging creates comprehensive audit trails for all changes

### Immediate Application
- **Risk Assessment**: How to evaluate AWS service risks in client environments
- **Control Testing**: What evidence to look for when testing automated controls
- **Audit Programs**: How to modify audit procedures for AWS-based processes
- **Documentation**: What AWS artifacts provide audit evidence

### Follow-up Resources
- AWS audit and compliance documentation
- Industry-specific AWS compliance guides  
- Cloud audit frameworks and methodologies
- Professional development in cloud auditing

---

## Quick Troubleshooting for Facilitators

### Pre-Session Issues

**Dashboard Shows No Data**:
- Wait 30+ minutes after deployment for metrics to populate
- Manually trigger Lambda functions if needed
- Verify EventBridge rules are enabled and functioning

**Console Access Problems**:
- Verify correct AWS region is selected
- Check IAM permissions for demonstration account
- Test console links before session starts

### During-Session Issues

**Participants Overwhelmed by Technical Detail**:
- Refocus on audit implications rather than technical features
- Use more familiar audit terminology
- Connect back to traditional audit concepts

**Running Over Time**:
- Skip optional demonstrations
- Shorten activity discussion time
- Focus on most audit-relevant services (CloudWatch, CloudTrail)

**Technology Not Working**:
- Have screenshot backups of all demonstrations
- Use shared-resources documentation for manual examples
- Focus on conceptual understanding rather than live demos

### Post-Session Cleanup

**Resource Cleanup**:
```bash
# Clean up demonstration environment
aws cloudformation delete-stack --stack-name aws-deep-dive-training-stack
```

**Cost Management**:
- Verify all services are deleted to prevent ongoing charges
- Monitor AWS billing for unexpected costs from session
- Document actual costs for future session planning

This facilitator guide enables effective delivery of AWS service overview training specifically designed for audit professionals within a 2-hour timeframe.
