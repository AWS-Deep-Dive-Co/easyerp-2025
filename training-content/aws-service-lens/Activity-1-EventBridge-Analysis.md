# Activity 1: EventBridge Analysis

## Activity Overview
**Duration**: 10 minutes
**Format**: Small groups (3-4 people)
**Objective**: Analyze EventBridge rules to identify audit risks and control considerations

---

## Participant Materials

### Scenario: Regional Sales Processing System

**Background**: 
Your client, RetailCorp, uses AWS EventBridge to automate their daily sales processing. Review the following EventBridge rule configurations and identify potential audit risks.

### EventBridge Rule #1: Daily Sales Processing
```
Rule Name: daily-sales-processing
Schedule: cron(0 2 * * ? *)  [Runs daily at 2:00 AM]
Target: Lambda function "process-daily-sales"
Status: Enabled
Created: 2024-01-15
Last Modified: 2024-06-20
Modified By: sales.admin@retailcorp.com
```

### EventBridge Rule #2: Month-End Reconciliation
```
Rule Name: month-end-reconciliation
Schedule: cron(0 1 L * ? *)  [Runs on last day of month at 1:00 AM]
Target: Step Functions workflow "month-end-process"
Status: Enabled
Created: 2024-02-01
Last Modified: 2024-11-30
Modified By: finance.manager@retailcorp.com
```

### EventBridge Rule #3: Inventory Adjustment
```
Rule Name: inventory-adjustment
Schedule: rate(4 hours)  [Runs every 4 hours]
Target: Lambda function "adjust-inventory"
Status: Disabled
Created: 2024-03-10
Last Modified: 2024-12-01
Modified By: it.admin@retailcorp.com
```

### Access Control Information
- **EventBridge Admin Role**: Can create, modify, and delete rules
- **Process Admin Role**: Can enable/disable existing rules
- **Read-Only Role**: Can view rules but not modify
- **Current Users with Admin Access**: 
  - sales.admin@retailcorp.com
  - finance.manager@retailcorp.com
  - it.admin@retailcorp.com
  - cto@retailcorp.com

---

## Analysis Questions

### 1. Risk Assessment
Identify **three potential audit risks** based on these EventBridge configurations:

**Risk 1**: ________________________________
**Business Impact**: ________________________
**Likelihood**: High / Medium / Low

**Risk 2**: ________________________________  
**Business Impact**: ________________________
**Likelihood**: High / Medium / Low

**Risk 3**: ________________________________
**Business Impact**: ________________________
**Likelihood**: High / Medium / Low

### 2. Control Considerations
What **control questions** would you ask during your audit?

a) **Change Management**:
   Question: _______________________________________________
   What evidence to request: _______________________________

b) **Access Controls**:
   Question: _______________________________________________
   What evidence to request: _______________________________

c) **Process Monitoring**:
   Question: _______________________________________________
   What evidence to request: _______________________________

### 3. Audit Evidence
List **specific AWS evidence sources** you would examine:

- [ ] EventBridge rule configurations and history
- [ ] CloudTrail logs for rule modifications
- [ ] Target service execution logs
- [ ] IAM policies and role assignments
- [ ] Other: ___________________________________________

### 4. Red Flags
Circle any concerning observations from the scenario:

a) **Schedule Complexity**: Some schedules use cron expressions that may be difficult to validate
b) **Cross-Department Access**: Multiple departments can modify automation rules
c) **Disabled Rules**: Critical processes may be disabled without proper approval
d) **Recent Changes**: Month-end process was modified just before period-end
e) **Broad Permissions**: Too many users have administrative access

---

## Discussion Preparation
Be ready to share:
1. **Top audit risk** your group identified
2. **One specific control test** you would perform
3. **Key evidence** you would request from the client

---

## Facilitator Instructions

### Setup (2 minutes)
- Divide participants into groups of 3-4
- Distribute scenario materials
- Set timer for 10 minutes
- Clarify that they should focus on audit risks, not technical configuration

### During Activity (8 minutes)
- **Circulate between groups** to answer questions
- **Keep discussions audit-focused**: Guide away from technical implementation details
- **Encourage practical thinking**: "What would you actually do in this situation?"
- **Time warnings**: Give 2-minute warning before ending

### Common Questions & Responses:
**Q**: "What does this cron expression mean?"
**A**: "Focus on the business impact - when does this process run and what could go wrong?"

**Q**: "How do we test if the controls are working?"
**A**: "Great question - what evidence would prove the control is operating effectively?"

**Q**: "Is this a high risk?"
**A**: "What's the business impact if this process fails or is modified inappropriately?"

### Debrief Discussion (5 minutes after activity)
**Facilitator Questions**:
1. "What was the biggest audit risk your group identified?"
2. "What evidence would you request to test controls over automated processes?"
3. "How does this compare to auditing traditional batch processing?"

---

## Expected Responses & Teaching Points

### Risk Assessment - Sample Answers:

**Risk 1: Unauthorized Process Changes**
- **Business Impact**: Critical sales/financial processes could be modified inappropriately
- **Likelihood**: Medium (multiple users have access)
- **Controls to Test**: Change approval process, segregation of duties

**Risk 2: Process Failure Going Undetected**
- **Business Impact**: Failed processes could result in incomplete financial reporting
- **Likelihood**: Medium (depends on monitoring adequacy)
- **Controls to Test**: Exception reporting, failure notifications, manual oversight

**Risk 3: Inappropriate Access to Critical Processes**
- **Business Impact**: Lack of segregation of duties in automated processes
- **Likelihood**: High (cross-department access observed)
- **Controls to Test**: User access reviews, role-based permissions

### Control Questions - Sample Answers:

**Change Management**: 
- Question: "What approval process exists for modifying EventBridge rules?"
- Evidence: Change tickets, approval workflows, rule modification history

**Access Controls**:
- Question: "How is access to EventBridge administration controlled and reviewed?"
- Evidence: IAM policies, user access reviews, principle of least privilege documentation

**Process Monitoring**:
- Question: "How does management monitor the success/failure of automated processes?"
- Evidence: CloudWatch dashboards, alert configurations, exception reports

### Red Flags - Teaching Points:

**Focus on Business Risk**:
- Emphasize that technical complexity isn't the issue - business control is
- Connect to traditional IT general controls (access, change management, operations)
- Highlight that automation increases the impact of control deficiencies

**Audit Evidence**:
- AWS provides comprehensive audit trails through CloudTrail
- EventBridge rule history shows all changes and who made them
- Target service logs provide evidence of process execution
- Integration with traditional audit approaches is possible

### Common Misconceptions to Address:

**"We can't audit what we can't see"**
- AWS provides extensive logging and audit trails
- Focus on output and business impact rather than technical implementation

**"This is too technical for auditors"**
- Emphasize business process focus, not technical configuration
- Connect to familiar concepts like batch processing and job scheduling

**"Cloud services are inherently riskier"**
- Discuss how cloud services can provide better audit trails than traditional systems
- Focus on control design rather than technology platform

This activity effectively introduces auditors to AWS automation services while maintaining focus on practical audit considerations and familiar risk assessment approaches.
