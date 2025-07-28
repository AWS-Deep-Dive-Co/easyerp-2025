# Activity 2: Hands-On Step Functions Workflow Analysis

## Activity Overview
**Duration**: 10 minutes
**Format**: Individual console exploration followed by group discussion
**Objective**: Navigate AWS Step Functions console to evaluate deployed workflow for audit risks and control gaps

---

## Console Navigation Instructions

### Step 1: Access Step Functions Console (2 minutes)

**Navigate to**: `https://console.aws.amazon.com/states/home`

**Find the Deployed Workflow**:
- Look for: `aws-deep-dive-financial-processing-workflow`
- Click on the workflow name to open details

### Step 2: Examine Workflow Definition (3 minutes)

**In the workflow details page**:
1. **Click on "Definition" tab** to see the visual workflow
2. **Review the workflow diagram** - notice the business process flow
3. **Click on individual states** to see their configuration
4. **Look for**:
   - Decision points and approval logic
   - Error handling and retry mechanisms
   - Integration with other AWS services
   - Timeout configurations

### Step 3: Review Execution History (3 minutes)

**Click on "Executions" tab**:
1. **Examine recent executions** - look for success/failure patterns
2. **Click on a successful execution** to see:
   - Input data and business context
   - Step-by-step execution flow
   - Timing and performance data
   - Output results
3. **Click on a failed execution** (if available) to see:
   - Where the failure occurred
   - Error messages and root causes
   - Retry attempts and recovery mechanisms

### Step 4: Analyze Monitoring Data (2 minutes)

**Look for monitoring information**:
1. **Check "Monitoring" tab** for execution metrics
2. **Note**:
   - Success/failure rates
   - Execution duration trends
   - Error patterns over time
   - Volume of executions

---

## Console Observation Worksheet

**As you navigate the console, complete this analysis**:

### 1. Workflow Structure Analysis

**From the Definition tab, identify**:

**Business Process Steps** (list the main states you see):
1. ________________________________________________
2. ________________________________________________
3. ________________________________________________
4. ________________________________________________

**Decision Points** (where does the workflow branch?):
- ________________________________________________
- ________________________________________________

**Error Handling** (what happens when steps fail?):
- ________________________________________________

**Integration Points** (what other AWS services are called?):
- ________________________________________________

### 2. Execution Pattern Analysis

**From the Executions tab, observe**:s

**Recent Execution Volume**:
- Total executions in last week: ____________________
- Success rate: ____________________________________
- Average execution time: ___________________________

**Failure Analysis** (if failures are visible):
- Most common failure point: _______________________
- Typical failure reason: ____________________________
- Recovery method: _________________________________

### 3. Risk Assessment Based on Console Observations

**Risk #1**: ________________________________________________
**Evidence from Console**: ___________________________________
**Audit Concern**: _______________________________________

**Risk #2**: ________________________________________________
**Evidence from Console**: ___________________________________
**Audit Concern**: _______________________________________

**Risk #3**: ________________________________________________
**Evidence from Console**: ___________________________________
**Audit Concern**: _______________________________________

### 4. Control Evaluation Based on Console Evidence

**For each area, assess based on what you observed in the console**:

**Segregation of Duties**:
Strong / Adequate / Weak / Cannot Determine
**Console Evidence**: ____________________________________

**Authorization Levels**:
Strong / Adequate / Weak / Cannot Determine  
**Console Evidence**: ____________________________________

**Exception Handling**:
Strong / Adequate / Weak / Cannot Determine
**Console Evidence**: ____________________________________

**Data Validation**:
Strong / Adequate / Weak / Cannot Determine
**Console Evidence**: ____________________________________

### 5. Audit Evidence Identification

**What specific evidence would you request from the client?**

□ Step Functions execution logs for completeness testing
□ Workflow definition change history from CloudTrail
□ Input/output data samples for accuracy testing
□ Error handling documentation and procedures
□ IAM permissions for workflow modification access
□ Other: ____________________________________________

### 6. Questions for Client Based on Console Observations

**Questions for Management**:
1. Based on the workflow I observed, how do you ensure _______________?
2. I noticed [specific observation], how is this controlled?
3. What oversight exists over the automated decisions in this workflow?

**Questions for IT**:
1. How do you ensure only authorized personnel can modify this workflow?
2. What monitoring alerts exist for workflow failures or anomalies?
3. How do you validate the business logic implemented in the workflow?

---

## Discussion Questions

**Be prepared to discuss**:
1. **Biggest Audit Concern**: What was the highest risk you identified from the console?
2. **Console Evidence**: What evidence was most/least useful for audit purposes?
3. **Audit Approach**: How would you test the controls you observed?
4. **Practical Challenges**: What was difficult to assess from the console alone?

---

## Facilitator Instructions

### Pre-Activity Setup (Before session)
- **Verify console access** for all participants to Step Functions
- **Execute the workflow manually** 30 minutes before session to ensure recent executions
- **Test console navigation** to confirm all participants can access the deployed workflow
- **Prepare backup screenshots** in case of access issues

### Activity Setup (1 minute)
- **Ensure participants have console access** and are logged in
- **Guide them to Step Functions console**: `https://console.aws.amazon.com/states/home`
- **Verify everyone can see** `aws-deep-dive-financial-processing-workflow`
- **Set timer for 8 minutes** of individual console exploration

### During Console Exploration (8 minutes)
- **Circulate and assist** with console navigation issues
- **Guide participants to key areas**: "Look at the Definition tab," "Check recent executions"
- **Don't provide answers** but help with technical navigation
- **Observe common findings** for discussion
- **Give 2-minute warning** before discussion

### Group Discussion Facilitation (2 minutes)
- **Ask volunteers to share** their key observations
- **Focus on audit implications**: "What would you test based on what you saw?"
- **Connect console observations to audit evidence**: "How reliable is this evidence?"

### Key Facilitator Prompts:

**If participants struggle with console navigation**:
*"Focus on what you can see and understand - you don't need to know every technical detail"*

**If they get lost in technical details**:
*"Think like an auditor - what business process risks do you see?"*

**If they can't find information**:
*"That's important feedback - what would you ask the client to provide?"*

### Troubleshooting:

**Console Access Issues**:
- Have screenshots ready as backup
- Pair participants with console access issues
- Focus discussion on observations from successful participants

**No Recent Executions Visible**:
- Manually trigger workflow execution during break if needed
- Use execution history screenshots as backup
- Focus on workflow definition analysis

---

## Expected Console Observations & Teaching Points

### Typical Workflow Structure Findings:

**Participants Should Observe**:
- **Daily Transaction Processing**: Lambda function integration
- **Month-End Processing**: More complex approval workflow  
- **Error Handling**: Retry policies and catch blocks
- **Monitoring Integration**: CloudWatch metrics collection

### Common Risk Identifications:

**From Console Observations**:
1. **Automated Decision Making**: No human oversight in daily processing
   - **Console Evidence**: Workflow shows direct Lambda execution
   - **Audit Implication**: Need to test automated business logic

2. **Integration Dependencies**: Multiple AWS service dependencies
   - **Console Evidence**: Workflow calls Lambda, then other services
   - **Audit Implication**: Failure in one service affects entire process

3. **Error Recovery**: May not handle all error scenarios appropriately
   - **Console Evidence**: Limited error states visible in workflow
   - **Audit Implication**: Need to test exception handling procedures

### Key Teaching Points from Console Experience:

**Console-Based Audit Evidence**:
- **Visual Workflows**: Step Functions provide clear process documentation
- **Execution History**: Complete audit trail of all process runs
- **Real-Time Monitoring**: Current performance and error data
- **Change Tracking**: Integration with CloudTrail for modification history

**Limitations of Console Evidence**:
- **Business Context**: Console shows technical process, not business authorization
- **Complete Picture**: May need additional documentation for full control assessment  
- **Data Validation**: Console shows structure but not data quality controls
- **Human Oversight**: Automated processes may lack adequate human review

**Practical Audit Applications**:
1. **Use Visual Workflows**: As process documentation for audit understanding
2. **Leverage Execution Logs**: For sampling and testing process completeness
3. **Analyze Error Patterns**: To identify control weaknesses and risks
4. **Verify Change Controls**: Through CloudTrail integration for workflow modifications

### Common Questions & Responses:

**Q**: "The console is overwhelming - how do I know what to focus on?"
**A**: "Focus on the business process flow first, then look for control points and exception handling"

**Q**: "How do I know if what I'm seeing is accurate?"
**A**: "Great audit question - this is why we need to validate system-generated evidence through testing"

**Q**: "What if the client won't give me console access?"
**A**: "That's a red flag for the control environment - document that as a limitation and request alternative evidence"

This hands-on console activity gives auditors practical experience with Step Functions while maintaining focus on audit-relevant observations and risk assessment skills.
