# Activity 2: Workflow Risk Assessment

## Activity Overview
**Duration**: 10 minutes
**Format**: Individual exercise followed by group discussion
**Objective**: Evaluate Step Functions workflow for audit risks and control gaps

---

## Participant Materials

### Scenario: Automated Purchase Order Processing

**Background**: 
TechManufacturing Inc. uses AWS Step Functions to automate their purchase order approval process. Review the workflow diagram and execution data below to assess audit risks.

### Step Functions Workflow: "Purchase Order Approval Process"

```
Step 1: Validate PO Data
├─ Input: Purchase order details, vendor info, amounts
├─ Process: Data validation and completeness check
├─ Success: Continue to Step 2
└─ Failure: Send rejection notice, end process

Step 2: Amount-Based Routing
├─ If amount < $5,000: Go to Step 3 (Department Approval)
├─ If amount $5,000-$25,000: Go to Step 4 (Manager Approval)
└─ If amount > $25,000: Go to Step 5 (Executive Approval)

Step 3: Department Approval (< $5,000)
├─ Process: Automatic approval for pre-approved vendors
├─ Success: Go to Step 6 (Create PO)
└─ Failure: Go to Step 7 (Manual Review Queue)

Step 4: Manager Approval ($5,000-$25,000)
├─ Process: Send email notification, wait for response
├─ Timeout: 24 hours (auto-reject)
├─ Success: Go to Step 6 (Create PO)
└─ Failure: Go to Step 7 (Manual Review Queue)

Step 5: Executive Approval (> $25,000)
├─ Process: Send email notification, wait for response
├─ Timeout: 48 hours (auto-reject)
├─ Success: Go to Step 6 (Create PO)
└─ Failure: Go to Step 7 (Manual Review Queue)

Step 6: Create Purchase Order
├─ Process: Generate PO number, update systems
├─ Success: Send confirmation, end process
└─ Failure: Go to Step 7 (Manual Review Queue)

Step 7: Manual Review Queue
├─ Process: Route to procurement team for manual processing
└─ End: Human intervention required
```

### Recent Execution Data (Last 30 Days)
- **Total Executions**: 847 purchase orders processed
- **Successful Completions**: 789 (93.2%)
- **Failed Executions**: 58 (6.8%)
- **Manual Review Queue**: 142 orders (16.8%)
- **Average Processing Time**: 
  - < $5,000: 3 minutes
  - $5,000-$25,000: 18 hours (including approval wait time)
  - > $25,000: 31 hours (including approval wait time)

### Error Analysis
**Top Failure Reasons**:
1. **Invalid Vendor Data** (31 failures): Vendor not in approved list
2. **Timeout Exceeded** (15 failures): Approval timeout reached
3. **System Integration Error** (8 failures): Unable to create PO in ERP system
4. **Data Validation Error** (4 failures): Missing required fields

### Approval Statistics
- **Auto-approved (< $5,000)**: 623 orders (73.5%)
- **Manager approved**: 156 orders (18.4%)
- **Executive approved**: 68 orders (8.0%)
- **Timeout rejections**: 15 orders (1.8%)

---

## Risk Assessment Worksheet

### 1. Process Control Evaluation

**Control Strength Assessment** (Circle one for each area):

**Segregation of Duties**:
Strong / Adequate / Weak / Cannot Determine

**Authorization Levels**:
Strong / Adequate / Weak / Cannot Determine

**Exception Handling**:
Strong / Adequate / Weak / Cannot Determine

**Data Validation**:
Strong / Adequate / Weak / Cannot Determine

### 2. Identified Risks

**Risk #1**: _________________________________________________
**Impact**: High / Medium / Low
**Likelihood**: High / Medium / Low
**Control Gap**: ____________________________________________

**Risk #2**: _________________________________________________
**Impact**: High / Medium / Low  
**Likelihood**: High / Medium / Low
**Control Gap**: ____________________________________________

**Risk #3**: _________________________________________________
**Impact**: High / Medium / Low
**Likelihood**: High / Medium / Low
**Control Gap**: ____________________________________________

### 3. Control Testing Approach

**What would you test?**
□ Authorization matrix matches workflow approval limits
□ Exception handling for failed processes
□ Completeness of purchase order processing
□ Segregation of duties in approval process
□ Timeout controls and escalation procedures
□ Other: ____________________________________________

**Key Evidence to Request**:
1. ___________________________________________________
2. ___________________________________________________
3. ___________________________________________________

### 4. Red Flag Analysis

**Check any concerning observations**:
□ High percentage of orders requiring manual review (16.8%)
□ Significant timeout failures in approval process
□ Auto-approval for orders under $5,000
□ Long processing times for higher-value orders
□ Integration failures with ERP system
□ Limited evidence of approval authority validation

### 5. Audit Questions

**Questions for Management**:
1. How is the $5,000 auto-approval threshold determined and approved?
2. What controls exist over the "pre-approved vendor" list?
3. How are timeout failures investigated and resolved?
4. Who has access to modify the workflow approval process?

**Questions for IT**:
1. How is the Step Functions workflow secured and change-controlled?
2. What monitoring exists for process failures and exceptions?
3. How is data integrity maintained throughout the workflow?
4. What backup procedures exist if the automated process fails?

---

## Discussion Questions

**For Group Discussion**:
1. **Biggest Audit Concern**: What's the highest risk you identified?
2. **Control Design**: How would you improve this process from a control perspective?
3. **Testing Approach**: What specific tests would you perform?
4. **Traditional vs. Automated**: How does auditing this differ from manual purchase order processes?

---

## Facilitator Instructions

### Setup (1 minute)
- Distribute scenario materials to each participant
- Emphasize this is **individual work** for first 8 minutes
- Set timer and remind participants to focus on audit risks, not technical details

### During Individual Work (8 minutes)
- **Circulate quietly** to observe participant approaches
- **Don't provide answers** but can clarify scenario questions
- **Note common patterns** in responses for discussion
- **Give 2-minute warning**

### Group Discussion (2 minutes)
- **Ask for volunteers** to share key findings
- **Focus on practical audit approaches**
- **Connect to familiar audit concepts**

### Key Facilitator Prompts:
**If participants struggle**: "Think about this like any other automated process you've audited - what could go wrong?"

**If too technical**: "Focus on the business impact - what matters for the financial statements?"

**If too abstract**: "What specific evidence would you look at during fieldwork?"

---

## Expected Responses & Teaching Points

### Risk Assessment - Expected Answers:

**High Risk Areas**:
1. **Auto-approval without human oversight** (orders < $5,000)
   - Control Gap: Lack of periodic review of auto-approved transactions
   - Testing: Sample auto-approved orders for appropriateness

2. **High manual exception rate** (16.8% to manual queue)
   - Control Gap: Process design may be inadequate for business needs
   - Testing: Analyze root causes of manual reviews

3. **Timeout-based rejections without investigation**
   - Control Gap: Valid purchase orders may be inappropriately rejected
   - Testing: Review timeout rejections for business necessity

### Control Testing - Key Focus Areas:

**Authorization Controls**:
- Test approval matrix matches workflow thresholds
- Verify executive approval for high-value items
- Validate pre-approved vendor list maintenance

**Completeness Controls**:
- Test that all purchase orders are processed through the workflow
- Verify failed processes are appropriately handled
- Check for bypass procedures and their authorization

**Exception Handling**:
- Review manual queue processing procedures
- Test escalation for timeout failures
- Validate error resolution and reprocessing

### Common Discussion Points:

**"How is this different from manual processes?"**
- **Volume and Speed**: Automated processes handle more volume faster
- **Consistency**: Less variation but potential for systematic errors
- **Audit Trail**: Better logging but requires different evidence gathering
- **Control Points**: Fewer manual checkpoints, rely on system controls

**"What if we don't understand the technology?"**
- **Focus on Business Logic**: Understand what the process does, not how
- **Use Available Documentation**: Workflow diagrams provide process maps
- **Leverage IT Specialists**: Work with IT auditors for technical aspects
- **Test Outputs**: Focus on results rather than technical implementation

### Key Teaching Points:

**Workflow Benefits for Auditors**:
- **Visual Documentation**: Step Functions provide clear process maps
- **Execution History**: Complete audit trail of all process executions
- **Exception Tracking**: Detailed logging of failures and manual interventions
- **Performance Metrics**: Built-in monitoring of process efficiency

**Audit Approach Adaptations**:
- **Continuous Processing**: Tests need to account for high-volume, continuous operation
- **System-Generated Evidence**: Greater reliance on automated logs and reports
- **Control Design Focus**: Emphasis on preventive controls built into workflow
- **Exception Analysis**: Statistical sampling of exceptions rather than individual review

### Common Misconceptions to Address:

**"Automated processes are inherently riskier"**
- Automated processes can provide better consistency and audit trails
- Risk comes from control design, not automation itself
- Focus on control effectiveness rather than manual vs. automated

**"We need to understand the technical implementation"**
- Business process understanding is more important than technical details
- Workflow diagrams provide sufficient detail for most audit purposes
- Partner with IT specialists when technical expertise is needed

This activity effectively demonstrates how to approach workflow analysis from an audit perspective while connecting to familiar business process audit concepts.
