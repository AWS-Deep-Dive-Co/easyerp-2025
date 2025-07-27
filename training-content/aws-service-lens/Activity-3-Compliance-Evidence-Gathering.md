# Activity 3: Compliance Evidence Gathering

## Activity Overview
**Duration**: 10 minutes
**Format**: Paired exercise (2 people per group)
**Objective**: Identify audit evidence sources in CloudWatch and CloudTrail for compliance testing

---

## Participant Materials

### Scenario: Financial Close Process Monitoring

**Background**: 
GlobalCorp uses AWS services to automate their monthly financial close process. As their external auditor, you need to identify appropriate evidence sources for testing management's assertions about process controls and operational effectiveness.

### System Overview
The financial close process includes:
- **Daily transaction processing** (Lambda functions)
- **Month-end journal entries** (Step Functions workflow)
- **Financial reporting** (Glue ETL jobs)
- **Compliance monitoring** (CloudWatch dashboards)
- **Change auditing** (CloudTrail logging)

### Management Assertions to Test

**Management claims the following controls are operating effectively:**

1. **"All daily transaction processing runs successfully with less than 1% failure rate"**
2. **"Month-end journal entry processes are reviewed and approved before posting"**
3. **"Any changes to financial processing systems require CFO approval"**
4. **"System performance issues are detected and resolved within 2 hours"**
5. **"All access to financial processing systems is logged and reviewed monthly"**

---

## CloudWatch Evidence Analysis

### CloudWatch Dashboard: Financial Operations Monitoring

**Available Metrics and Widgets**:

```
Dashboard: "Financial-Operations-Dashboard"
Created: 2024-01-15
Last Updated: 2024-11-30

Widget 1: Daily Transaction Processing Success Rate
- Metric: Custom/FinancialProcessing/SuccessRate
- Time Period: Last 30 days
- Current Value: 98.7%
- Threshold Alert: < 99%

Widget 2: Transaction Processing Volume
- Metric: Custom/FinancialProcessing/TransactionCount  
- Time Period: Last 24 hours
- Current Value: 1,247,892 transactions
- Trend: +3.2% vs. previous day

Widget 3: Month-End Process Duration
- Metric: AWS/StepFunctions/ExecutionTime
- Process: month-end-journal-entry-workflow
- Last Execution: 47 minutes
- Average Duration: 52 minutes

Widget 4: System Error Rate
- Metric: AWS/Lambda/Errors
- All financial processing functions
- Current: 0.3%
- Alert Threshold: > 1%

Widget 5: ETL Job Success Rate  
- Metric: AWS/Glue/JobSuccessRate
- Jobs: financial-reporting-etl, compliance-validation
- Current: 100% (last 7 days)
- Historical: 98.9% (last 90 days)
```

### CloudWatch Alarms Configuration

```
Alarm: "High-Error-Rate-Alert"
- Metric: Custom/FinancialProcessing/ErrorRate
- Threshold: > 1% for 2 consecutive periods
- Action: Send SNS notification to finance-alerts@globalcorp.com
- State: OK (not triggered in last 30 days)

Alarm: "Processing-Delay-Alert"  
- Metric: AWS/Lambda/Duration
- Threshold: > 5 minutes average over 15 minutes
- Action: Send SNS notification to it-ops@globalcorp.com
- State: OK (last triggered: 2024-10-15)

Alarm: "Month-End-Failure-Alert"
- Metric: AWS/StepFunctions/ExecutionsFailed
- Threshold: > 0 for month-end workflow
- Action: Send SNS notification to cfo@globalcorp.com
- State: OK (never triggered)
```

---

## CloudTrail Evidence Analysis

### CloudTrail Event Log Sample

**Recent Events Related to Financial Processing Systems**:

```
Event 1:
Timestamp: 2024-12-01 14:23:17 UTC
User: cfo@globalcorp.com
Action: events:PutRule
Resource: month-end-processing-schedule
Source IP: 192.168.1.45 (Corporate Network)
Result: Success
Details: Modified schedule from monthly to bi-weekly

Event 2:  
Timestamp: 2024-11-28 09:15:33 UTC
User: finance.analyst@globalcorp.com
Action: lambda:UpdateFunctionCode  
Resource: daily-transaction-processor
Source IP: 203.0.113.12 (External IP)
Result: Access Denied
Details: Insufficient permissions for code modification

Event 3:
Timestamp: 2024-11-25 16:42:29 UTC  
User: it.admin@globalcorp.com
Action: stepfunctions:UpdateStateMachine
Resource: month-end-journal-entry-workflow
Source IP: 192.168.1.67 (Corporate Network)  
Result: Success
Details: Updated approval step timeout from 24 to 48 hours

Event 4:
Timestamp: 2024-11-20 11:07:44 UTC
User: external.consultant@techfirm.com
Action: cloudwatch:PutDashboard
Resource: Financial-Operations-Dashboard
Source IP: 198.51.100.8 (External IP)
Result: Success  
Details: Added new compliance monitoring widget

Event 5:
Timestamp: 2024-11-15 08:33:12 UTC
User: system.service@globalcorp.com
Action: glue:StartJobRun
Resource: financial-reporting-etl
Source IP: 10.0.0.15 (AWS Internal)
Result: Success
Details: Automated execution via EventBridge schedule
```

---

## Evidence Evaluation Worksheet

### Part A: Evidence Sufficiency Analysis

**For each management assertion, evaluate the available evidence:**

**Assertion 1**: "All daily transaction processing runs successfully with less than 1% failure rate"

Available Evidence:
□ CloudWatch success rate metric (98.7% current)
□ Historical trend data available
□ Automated alerting for thresholds
□ Custom metrics from business process

**Evidence Assessment**:
Sufficient / Insufficient / Requires Additional Testing

**Additional Evidence Needed**: _________________________________

---

**Assertion 2**: "Month-end journal entry processes are reviewed and approved before posting"

Available Evidence:
□ Step Functions execution history
□ Workflow timeout configurations  
□ CloudTrail approval step modifications
□ Process duration metrics

**Evidence Assessment**:  
Sufficient / Insufficient / Requires Additional Testing

**Additional Evidence Needed**: _________________________________

---

**Assertion 3**: "Any changes to financial processing systems require CFO approval"

Available Evidence:
□ CloudTrail shows CFO making system changes
□ Access denied events for unauthorized users
□ Change timestamps and user attribution
□ System modification audit trail

**Evidence Assessment**:
Sufficient / Insufficient / Requires Additional Testing  

**Additional Evidence Needed**: _________________________________

---

**Assertion 4**: "System performance issues are detected and resolved within 2 hours"

Available Evidence:
□ CloudWatch alarm configurations
□ Alert notification setup to IT operations
□ Historical alarm trigger data
□ Performance metric thresholds

**Evidence Assessment**:
Sufficient / Insufficient / Requires Additional Testing

**Additional Evidence Needed**: _________________________________

---

**Assertion 5**: "All access to financial processing systems is logged and reviewed monthly"

Available Evidence:
□ CloudTrail comprehensive event logging
□ User identity and session information
□ Source IP and timestamp data
□ Success/failure status of operations

**Evidence Assessment**:
Sufficient / Insufficient / Requires Additional Testing

**Additional Evidence Needed**: _________________________________

### Part B: Red Flag Analysis

**Check any concerning observations from the evidence:**

□ **CFO directly modifying system schedules** (Event 1)
□ **External consultant accessing financial dashboards** (Event 4)  
□ **Finance analyst attempting unauthorized code changes** (Event 2)
□ **IT admin changing approval timeouts** (Event 3)
□ **External IP addresses accessing financial systems**
□ **No evidence of regular access reviews in CloudTrail**
□ **Alarm thresholds may be too permissive** (1% error rate threshold)

### Part C: Additional Testing Requirements

**What additional audit procedures would you perform?**

1. **Control Testing**: ___________________________________________
2. **Substantive Testing**: ______________________________________
3. **IT General Controls**: ____________________________________
4. **Management Review Controls**: _______________________________

---

## Discussion Questions

**For Paired Discussion**:
1. **Evidence Quality**: Is CloudWatch/CloudTrail evidence reliable for audit purposes?
2. **Completeness**: What evidence gaps did you identify?
3. **Red Flags**: Which observations would you investigate further?
4. **Testing Strategy**: How would you structure your audit testing?

---

## Facilitator Instructions

### Setup (1 minute)
- **Pair participants** (preferably with different experience levels)
- **Distribute materials** and emphasize focus on audit evidence evaluation
- **Set expectations**: This is about evidence sufficiency, not technical understanding

### During Activity (8 minutes)
- **Circulate between pairs** to listen to discussions
- **Guide toward audit evidence concepts**: "Is this evidence sufficient? Reliable? Relevant?"
- **Encourage practical thinking**: "What would you actually do with this evidence?"
- **Time management**: Give 3-minute and 1-minute warnings

### Common Questions & Facilitator Responses:

**Q**: "How do we know if CloudWatch data is accurate?"
**A**: "Great question - how would you test the reliability of any automated report?"

**Q**: "What if management won't give us access to CloudTrail?"
**A**: "What does that tell you about the control environment?"

**Q**: "This seems like a lot of data to review"
**A**: "How would you use audit sampling or automated analytics?"

### Debrief Discussion (2 minutes)
**Key Questions to Ask**:
1. "What was the strongest evidence you found?"
2. "What evidence gaps concerned you most?"
3. "How does this compare to traditional IT audit evidence?"

---

## Expected Responses & Teaching Points

### Evidence Sufficiency Analysis - Expected Responses:

**Assertion 1 (Transaction Processing Success)**:
- **Evidence Assessment**: Sufficient for design, insufficient for operating effectiveness
- **Additional Testing**: Sample individual transaction logs, test alert responsiveness
- **Key Point**: Metrics show results but not underlying data quality

**Assertion 2 (Review and Approval)**:
- **Evidence Assessment**: Insufficient - no evidence of actual human approval
- **Additional Testing**: Review Step Functions execution details, interview approvers
- **Key Point**: Process existence ≠ control operation

**Assertion 3 (CFO Approval Requirement)**:
- **Evidence Assessment**: Insufficient - shows CFO made changes but not approval process
- **Additional Testing**: Review change management procedures, approval documentation
- **Key Point**: CloudTrail shows what happened, not whether it was properly authorized

**Assertion 4 (2-Hour Response Time)**:
- **Evidence Assessment**: Insufficient - shows alert setup but not response performance
- **Additional Testing**: Review incident response logs, test alert functionality
- **Key Point**: Preventive controls need testing of detective and corrective components

**Assertion 5 (Access Logging and Review)**:
- **Evidence Assessment**: Sufficient for logging, insufficient for review process
- **Additional Testing**: Evidence of monthly access reviews, follow-up on exceptions
- **Key Point**: Distinguish between automated logging and manual review controls

### Red Flag Analysis - Teaching Points:

**High-Risk Observations**:
1. **CFO directly modifying systems** - Potential segregation of duties issue
2. **External consultant dashboard access** - Inappropriate third-party access
3. **Unauthorized change attempts** - Control breakdown in access management
4. **External IP system access** - Network security concerns

**Audit Investigation Areas**:
- **Change Management**: Who authorizes system modifications?
- **Access Controls**: How is user provisioning and deprovisioning managed?
- **Segregation of Duties**: Are operational and oversight roles properly separated?
- **Third-Party Access**: How are consultant and vendor accesses managed?

### Key Teaching Points:

**Evidence Reliability**:
- **AWS-Generated Logs**: Generally reliable but need validation procedures
- **Custom Metrics**: Require understanding of calculation methodology
- **Automated Reports**: Need testing of underlying data and calculations
- **Integration Points**: Verify data integrity across system boundaries

**Audit Approach Adaptations**:
- **Volume Considerations**: Use data analytics for large-volume evidence
- **Continuous Monitoring**: Test both point-in-time and ongoing effectiveness
- **System-Generated Evidence**: Develop procedures for automated audit evidence
- **Real-Time Testing**: Leverage continuous monitoring for ongoing assurance

**Common Audit Challenges**:
1. **Evidence Volume**: Too much data to review manually
   - **Solution**: Use sampling, analytics, and risk-based approaches

2. **Technical Complexity**: Understanding system-generated evidence
   - **Solution**: Focus on business impact, leverage specialists as needed

3. **Continuous Processing**: Traditional point-in-time testing inadequacy
   - **Solution**: Develop continuous auditing procedures and monitoring

4. **Control Design vs. Operation**: Automated controls may be designed well but operate poorly
   - **Solution**: Test both design and operating effectiveness with appropriate evidence

This activity effectively bridges traditional audit evidence evaluation skills with cloud-based evidence sources while maintaining practical audit focus.
