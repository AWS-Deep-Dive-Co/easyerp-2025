# SOX Auditor Training: Group Activity Materials
## CloudWatch & CloudTrail Monitoring Session

---

## GROUP ACTIVITY 1: Dashboard Health Check Worksheet

### Team Information
**Team Number:** _____ **Team Members:** _________________________________

### Activity Overview
**Duration:** 15 minutes  
**Objective:** Assess the health of financial processes using CloudWatch dashboards

### Dashboard Access
**SOX Compliance Dashboard URL:** `https://us-east-1.console.aws.amazon.com/cloudwatch/home?region=us-east-1#dashboards:name=sox-training-sox-compliance-monitoring`

### Data Collection Worksheet

#### 1. Daily Transaction Processing Analysis
**Current Status (last 24 hours):**
- Total Transactions Processed: _______________
- Failed Transactions: _______________  
- Success Rate: _______________% 
- Average Processing Time: _______________ seconds

**Observations:**
- Any error spikes? □ Yes □ No  
- If yes, when? _______________
- Pattern concerns? □ Yes □ No
- If yes, describe: _______________

#### 2. Month-End Close Process Review
**Last Month-End Close:**
- Status: □ Success □ Partial Failure □ Complete Failure
- Duration: _______________ minutes
- Reconciliation Issues: □ None □ Minor □ Material
- Variance Amount: $ _______________

#### 3. Compliance Metrics Assessment
**Current Scores:**
- Overall Compliance Score: _______________% 
- Data Completeness Rate: _______________%
- Data Accuracy Rate: _______________%
- Control Effectiveness: _______________%

**Red Flags Identified:**
□ Compliance score below 85%
□ Accuracy rate below 95%
□ Control effectiveness below 90%
□ Material variances detected
□ Other: _______________

### 4. Team Assessment Questions

**A. Process Control Effectiveness:**
Based on the dashboard data, rate the effectiveness of automated controls:
□ Effective (no concerns)
□ Some deficiencies noted
□ Material weaknesses identified

**B. Detective Controls:**
Are monitoring controls adequate to detect and alert on failures?
□ Yes, real-time detection
□ Partially, some delays
□ No, significant gaps

**C. Follow-up Procedures Required:**
If this were a real audit, what additional procedures would you perform?
□ Test exception reports and follow-up
□ Review management's monitoring procedures  
□ Test manual override controls
□ Sample detailed transaction testing
□ Other: _______________

### 5. Key Finding for Presentation
**Most Significant Observation:**
_______________________________________________________________
_______________________________________________________________

**Audit Impact:**
_______________________________________________________________
_______________________________________________________________

**Recommended Action:**
_______________________________________________________________
_______________________________________________________________

---

## GROUP ACTIVITY 2: Log Investigation Worksheet

### Team Information
**Team Number:** _____ **Assignment:** ___________________________________

### Activity Overview
**Duration:** 25 minutes  
**Objective:** Investigate process failures using CloudWatch Logs

### Investigation Framework

#### Phase 1: Initial Log Review (10 minutes)
**CloudWatch Logs URL:** `https://us-east-1.console.aws.amazon.com/cloudwatch/home?region=us-east-1#logsV2:logs-insights`

**Search Query Used:**
```
fields @timestamp, @message
| filter @message like /_______________/
| sort @timestamp desc
| limit 50
```

**Initial Findings:**
- Log entries reviewed: _______________
- Time period covered: _______________
- Process(es) affected: _______________

#### Phase 2: Failure Analysis (10 minutes)

**Error Details:**
- **First error timestamp:** _______________
- **Last error timestamp:** _______________  
- **Total duration of issues:** _______________ minutes
- **Error frequency:** _______________ errors per minute

**Specific Error Messages Found:**
1. _______________________________________________________________
2. _______________________________________________________________
3. _______________________________________________________________

**Root Cause Analysis:**
□ Database connectivity issues
□ Validation rule failures  
□ Timeout/performance problems
□ Data integrity issues
□ Access control violations
□ Other: _______________

#### Phase 3: Impact Assessment (5 minutes)

**Quantified Impact:**
- Transactions affected: _______________
- Dollar amount (if available): $ _______________
- Systems impacted: _______________
- Recovery time: _______________ minutes

**Control Performance:**
- Did automated detection work? □ Yes □ No □ Partially
- Response time to failure: _______________ minutes  
- Manual intervention required? □ Yes □ No
- Escalation followed procedures? □ Yes □ No □ Unknown

### Audit Finding Documentation

**Finding Title:** _______________________________________________________________

**Condition (What happened):**
_______________________________________________________________________________
_______________________________________________________________________________

**Criteria (What should have happened):**
_______________________________________________________________________________
_______________________________________________________________________________

**Cause (Why it happened):**
_______________________________________________________________________________
_______________________________________________________________________________

**Effect (Impact on financial reporting):**
_______________________________________________________________________________
_______________________________________________________________________________

**Severity Rating:**
□ Material Weakness
□ Significant Deficiency  
□ Control Deficiency
□ No deficiency noted

**Recommended Management Action:**
_______________________________________________________________________________
_______________________________________________________________________________

---

## GROUP ACTIVITY 3: Access Control Investigation Worksheet

### Team Information
**Team Number:** _____ **Focus Area:** ___________________________________

### Activity Overview
**Duration:** 20 minutes  
**Objective:** Investigate access controls using CloudTrail events

### Investigation Parameters
**CloudTrail URL:** `https://us-east-1.console.aws.amazon.com/cloudtrail/home?region=us-east-1#/events`

**Time Period:** Last Friday 6 PM - Monday 6 AM
**Key Events to Search:** InvokeFunction, StartExecution, ModifyFunctionConfiguration, CreateUser, AttachUserPolicy

### Phase 1: Event Discovery (8 minutes)

#### After-Hours Activity Log
| Time | Event Name | User Identity | Source IP | Resource | Authorized? |
|------|------------|---------------|-----------|----------|-------------|
| | | | | | □ Yes □ No |
| | | | | | □ Yes □ No |
| | | | | | □ Yes □ No |
| | | | | | □ Yes □ No |
| | | | | | □ Yes □ No |

#### Authorized Personnel List
**Finance Process Administrators:**
- John Smith (Operations Manager)
- Sarah Johnson (Finance Director)  
- Mike Chen (IT Finance Lead)

**Emergency Contact:**
- David Wilson (IT Director) - weekends only

### Phase 2: Access Analysis (7 minutes)

**Segregation of Duties Review:**
□ Same user initiated and approved transactions
□ Non-finance personnel accessed financial processes
□ Administrative changes made without approval
□ No violations detected

**Geographic/Timing Anomalies:**
□ Access from unusual IP addresses
□ Activity outside normal business hours
□ Patterns suggesting automated/bot access
□ No anomalies detected

**Permission Escalation:**
□ Users granted elevated privileges
□ Temporary access not revoked timely
□ Unauthorized role assumptions
□ No escalation issues

### Phase 3: Control Assessment (5 minutes)

**Access Control Effectiveness:**

**A. User Access Reviews:**
□ Effective - only authorized users accessed systems
□ Deficient - unauthorized access occurred
□ Cannot determine from available evidence

**B. Segregation of Duties:**
□ Effective - proper separation maintained
□ Deficient - same person performed incompatible functions
□ Cannot determine from available evidence

**C. Change Management:**
□ Effective - all changes properly authorized
□ Deficient - unauthorized changes occurred
□ Cannot determine from available evidence

### Risk Assessment Matrix
**Likelihood of Control Failure:**
□ Remote □ Reasonably Possible □ Probable

**Magnitude of Potential Impact:**
□ Inconsequential □ Minor □ Moderate □ Major

**Overall Risk Rating:**
□ Low □ Medium □ High □ Critical

### Findings Summary
**Control Violations Identified:**
_______________________________________________________________________________
_______________________________________________________________________________

**Evidence of Adequate Controls:**
_______________________________________________________________________________
_______________________________________________________________________________

**Recommendations for Management:**
_______________________________________________________________________________
_______________________________________________________________________________

---

## CAPSTONE ACTIVITY: Month-End Close Investigation

### Team Information
**Team Number:** _____ **Team Members:** _________________________________

### Scenario Context
**CFO Email:** Month-end close process failed last night. Normal completion: 3 AM. Actual completion: 6:30 AM. Possible data integrity issues. Need analysis before financial statement preparation.

**Investigation Duration:** 15 minutes total

### Phase 1: Dashboard Assessment (5 minutes)

**SOX Compliance Dashboard Review:**
- Month-end process status: □ Success □ Warning □ Failed
- Active alerts: _______________
- Compliance score impact: _______________
- Performance anomalies: _______________

**Immediate Red Flags:**
□ Material variance alerts
□ Control effectiveness drops
□ Processing time significantly elevated
□ Data completeness issues

### Phase 2: Log Analysis (6 minutes)

**CloudWatch Logs Investigation:**
**Search timeframe:** Last night 11 PM - 7 AM

**Critical Events Timeline:**
| Time | Event Description | Severity | Impact |
|------|------------------|----------|---------|
| | | □ Info □ Warn □ Error | |
| | | □ Info □ Warn □ Error | |
| | | □ Info □ Warn □ Error | |
| | | □ Info □ Warn □ Error | |

**Root Cause Determination:**
□ Database performance/connectivity
□ Reconciliation variance exceeded threshold
□ Validation rule failures
□ Resource capacity constraints
□ Data source availability
□ Other: _______________

**Quantified Impact:**
- Records processed: _______________
- Records failed: _______________  
- Dollar variance: $ _______________
- Accounts affected: _______________

### Phase 3: Access Audit (4 minutes)

**CloudTrail Review for Manual Interventions:**
**Manual actions during incident:**
| Time | User | Action | Authorized? |
|------|------|--------|-------------|
| | | | □ Yes □ No |
| | | | □ Yes □ No |
| | | | □ Yes □ No |

**Incident Response Assessment:**
□ Proper escalation procedures followed
□ Authorized personnel only involved  
□ Changes documented and approved
□ No manual interventions detected

### CFO Briefing Preparation

#### Executive Summary (Business Impact)
**What Happened:** _______________________________________________________________
_______________________________________________________________________________

**Financial Impact:** ____________________________________________________________
_______________________________________________________________________________

**Risk Assessment:** □ No Risk □ Low Risk □ Moderate Risk □ High Risk □ Material

#### Technical Root Cause
**Primary Cause:** ______________________________________________________________
_______________________________________________________________________________

**Contributing Factors:** _______________________________________________________
_______________________________________________________________________________

#### Control Assessment
**Detective Controls:** □ Effective □ Partially Effective □ Ineffective
**Why:** ____________________________________________________________________

**Corrective Controls:** □ Effective □ Partially Effective □ Ineffective  
**Why:** ____________________________________________________________________

#### Recommendations

**Immediate Actions (next 24 hours):**
1. ________________________________________________________________________
2. ________________________________________________________________________

**Short-term Actions (next 30 days):**
1. ________________________________________________________________________
2. ________________________________________________________________________

**Long-term Improvements (next quarter):**
1. ________________________________________________________________________
2. ________________________________________________________________________

#### Management Response Required
**Questions for Management:**
1. ________________________________________________________________________
2. ________________________________________________________________________

**Documentation Needed:**
□ Incident response procedures
□ Management monitoring reports
□ Exception handling documentation
□ User access reviews
□ Other: ________________________________________________________________

---

## Presentation Guidelines

### Team Presentation Structure
**Time Limit:** 2-3 minutes per team  
**Format:** Standing presentation to full group

### Required Elements:
1. **Opening:** "Team [X] investigated [scenario]"
2. **Key Finding:** Most significant discovery
3. **Evidence:** What data supports your conclusion
4. **Impact:** Business/audit significance  
5. **Recommendation:** Specific action for management

### Presentation Tips:
- Speak confidently and clearly
- Use specific numbers/data when available
- Connect technical findings to business impact
- Be prepared for follow-up questions
- Stay within time limit

### Evaluation Criteria:
- **Analysis Quality:** Did you identify key issues?
- **Evidence Support:** Is your conclusion data-driven?
- **Risk Assessment:** Appropriate severity rating?
- **Recommendations:** Actionable and specific?
- **Professional Communication:** Clear, concise delivery?

---

## Quick Reference: Key Patterns to Recognize

### Success Indicators in Logs:
- "SUCCESS: All [X] transactions processed"
- "Processing completed in [X] seconds"  
- "✓ Completed: [Process Name]"
- "No validation errors detected"

### Warning Indicators:
- "PARTIAL FAILURE"
- "TIMEOUT" 
- "Validation issues detected but proceeding"
- Processing time > normal range

### Critical Failure Indicators:
- "CRITICAL:" prefix
- "FATAL ERROR"
- "Manual intervention required"
- "Material variance detected"
- "Connection timeout"
- "Database unavailable"

### CloudTrail Red Flags:
- Administrative actions by non-admin users
- Financial processes executed outside business hours
- API calls from unusual geographic locations
- Same user performing incompatible functions
- Permission changes without documentation

### Dashboard Thresholds:
- **Compliance Score:** <85% requires investigation
- **Success Rate:** <95% indicates control concerns  
- **Processing Time:** >150% of normal warrants review
- **Error Rate:** >5% suggests systematic issues
