# Activity 1: Hands-On EventBridge and Lambda Integration Analysis

## Activity Overview
**Duration**: 10 minutes
**Format**: Small groups (3-4 people) exploring AWS Console
**Objective**: Navigate EventBridge and Lambda consoles to understand integrated automation controls and identify key IT control risks

---

## Console Navigation Instructions

### Step 1: EventBridge Overview (3 minutes)

**Navigate to**: `https://console.aws.amazon.com/events/home`

**Quick Rule Analysis**:
- Click on **"Rules"** in the left navigation
- Look for rules starting with `aws-deep-dive-`
- **Review all the rules** and note for each:
  - **Trigger type**: Schedule vs Event Pattern
  - **Target**: What Lambda function does it trigger?
  - **Status**: Enabled/Disabled

### Step 2: Lambda Function Investigation (4 minutes)

**Navigate to**: `https://console.aws.amazon.com/lambda/home`

**Function Analysis**:
- Look for functions starting with `aws-deep-dive-`
- **Click on 2-3 functions** and examine:
  - **Triggers tab**: What EventBridge rules trigger this function?
  - **Monitoring tab**: Recent execution patterns
  - **Configuration**: Runtime and basic settings

### Step 3: Integration Assessment (3 minutes)

**Trace the flow**:
1. **Pick one EventBridge rule** from Step 1
2. **Find its target Lambda function** from Step 2
3. **Document the complete flow**: Trigger → Rule → Function
4. **Identify potential control gaps**: What could go wrong in this chain?

---

## Console Observation Worksheet

**As your group explores the console, document your findings**:

### 1. EventBridge Integration Map

**Integration 1**: 
- **EventBridge Rule**: _____________________________
- **Trigger Type**: Schedule / Event Pattern
- **Target Lambda Function**: _____________________________
- **Function Status**: Active / Inactive

**Integration 2**:
- **EventBridge Rule**: _____________________________
- **Trigger Type**: Schedule / Event Pattern  
- **Target Lambda Function**: _____________________________
- **Function Status**: Active / Inactive

**Integration 3**:
- **EventBridge Rule**: _____________________________
- **Trigger Type**: Schedule / Event Pattern  
- **Target Lambda Function**: _____________________________
- **Function Status**: Active / Inactive

### 2. Control Questions

**Scheduling**:
What would you ask about how these automated processes are scheduled and timed?
_______________________________________________

**Monitoring**: 
What would you ask about how failures are detected and handled?
_______________________________________________

**Integration**:
What would you ask about the EventBridge → Lambda integration reliability?
_______________________________________________

---

## Group Discussion Preparation

**Be ready to share with the class**:
1. **Integration Understanding**: How do EventBridge and Lambda work together in the examples you found?
2. **Scheduling Questions**: What would you ask the client about how these automated processes are timed?
3. **Monitoring Questions**: What would you ask about how the client detects and handles failures?
4. **Testing Strategy**: How would you approach testing the scheduling or monitoring controls?
5. **Evidence Gaps**: What information couldn't you get from the console alone?

---

## Facilitator Instructions

### Pre-Session Setup (2 minutes)
- Ensure all participants have AWS console access with EventBridge and Lambda viewing permissions
- Verify the aws-deep-dive infrastructure is deployed with EventBridge rules and Lambda functions
- Confirm console displays are set to the correct AWS region (match infrastructure deployment)

### Activity Flow
This streamlined activity focuses on practical console observation to assess EventBridge and Lambda integration controls in just 10 minutes.

**Step 1 (3 minutes)**: Guide participants to EventBridge console to identify rule types and targets
**Step 2 (4 minutes)**: Navigate to Lambda console to examine function configurations and EventBridge connections  
**Step 3 (3 minutes)**: Quick assessment of integration patterns and control risks

### Key Talking Points During Activity
- "Focus on what you can observe directly in the console, not deep technical details"
- "Look for patterns that indicate good or poor IT governance practices"
- "EventBridge rules should have clear business purposes and proper error handling"
- "Lambda functions should show appropriate monitoring and logging configurations"

### Expected Outcomes
Participants should be able to:
- Understand how EventBridge rules trigger Lambda functions (basic integration concept)
- Identify key scheduling and monitoring control areas for automated processes
- Formulate appropriate audit questions about timing and failure detection
- Develop practical testing approaches for scheduling and monitoring controls

## Comprehensive Debrief Guide

### Discussion Question 1: Integration Understanding
**Ask**: "How do EventBridge and Lambda work together in the examples you found?"

**Possible Participant Answers**:
- "EventBridge acts like a scheduler that triggers Lambda functions to run"
- "EventBridge rules watch for events or time schedules, then call Lambda functions"
- "Lambda functions wait for EventBridge to tell them when to execute"
- "It's like having an automated system where EventBridge is the timer/trigger and Lambda does the work"
- "EventBridge sets up the 'when' and Lambda handles the 'what'"

**Facilitator Follow-up**: "Exactly! This trigger-worker pattern is common in automated systems. EventBridge handles timing and event detection, Lambda handles the actual processing."

### Discussion Question 2: Scheduling Questions
**Ask**: "What would you ask the client about how these automated processes are timed?"

**Possible Participant Answers**:
- "How often do these processes run?"
- "Who decides the timing schedule?"
- "What happens if the timing is wrong?"
- "How do you know if a scheduled process didn't run?"
- "Can the schedule be changed easily?"
- "Are there any dependencies between different scheduled processes?"
- "What happens if a process runs too frequently or not frequently enough?"
- "How do you handle scheduling conflicts?"
- "Who gets notified if schedules change?"

**Facilitator Follow-up**: "These are great audit questions! The key is understanding whether the timing controls support the business process requirements and whether there's proper oversight of schedule changes."

### Discussion Question 3: Monitoring Questions  
**Ask**: "What would you ask about how the client detects and handles failures?"

**Possible Participant Answers**:
- "How do you know if a Lambda function failed?"
- "Who gets alerted when something goes wrong?"
- "How quickly do you detect failures?"
- "What logs are kept of successes and failures?"
- "Is there automatic retry if something fails?"
- "How do you handle partial failures?"
- "Who is responsible for monitoring these processes?"
- "How often do you review the monitoring data?"
- "What constitutes a 'failure' vs. just a warning?"
- "How do you prevent the same failure from happening again?"

**Facilitator Follow-up**: "Excellent monitoring questions! The key control principle is that automated processes need the same oversight as manual processes - someone needs to be watching and responding to problems."

### Discussion Question 4: Testing Strategy
**Ask**: "How would you approach testing the scheduling or monitoring controls?"

**Possible Participant Answers**:

**For Scheduling Controls**:
- "Check if the actual run times match the scheduled times"
- "Review logs to see if processes run when expected"
- "Test what happens when you change a schedule"
- "Verify who can modify schedules and how changes are approved"
- "Check if there are alerts for missed scheduled runs"

**For Monitoring Controls**:
- "Create a test failure and see if it gets detected"
- "Review alert logs to see if monitoring is working"
- "Check who receives failure notifications"
- "Verify how quickly failures are detected"
- "Test if retry mechanisms work properly"

**For Integration Reliability**:
- "Test what happens when EventBridge can't reach Lambda"
- "Check error handling when Lambda functions fail"
- "Verify backup or fallback procedures"
- "Review dependency documentation"

**Facilitator Follow-up**: "Great testing approaches! Notice how you're thinking about testing both the design (does the control exist?) and the operating effectiveness (is the control working in practice?)."

### Discussion Question 5: Evidence Gaps
**Ask**: "What information couldn't you get from the console alone?"

**Possible Participant Answers**:
- "Who approved these automated processes?"
- "What's the business justification for the timing?"
- "Who gets notified when things fail?"
- "How are changes to these processes managed?"
- "What happens to the data that gets processed?"
- "Are there any manual overrides or exceptions?"
- "How often are these processes reviewed?"
- "What testing was done before deployment?"
- "Who has access to modify these configurations?"
- "How do failures get escalated?"

**Facilitator Follow-up**: "Perfect! The console shows you the 'what' and 'when,' but auditing requires understanding the 'who,' 'why,' and 'how' - which means you need to interview people and review documentation beyond what AWS shows you."

### Common Teaching Moments During Debrief

**If participants focus too much on technical details**:
"Remember, as IT auditors, you don't need to become AWS experts. Focus on the control principles - does the organization have proper oversight of automated processes?"

**If participants struggle with control concepts**:
"Think of this like any automated system in your organization - you'd want to know: When does it run? How do you know it worked? Who can change it? What happens when it fails?"

**If participants ask about complex technical configurations**:
"Great observation! That's exactly the kind of complexity that would make you ask the client: 'How do you ensure this configuration is correct and how do you test changes before implementing them?'"

### Wrap-up Key Messages (2 minutes)
1. **Integration Pattern**: "EventBridge + Lambda creates automated processes that need traditional IT general controls"
2. **Audit Approach**: "Focus on control principles, not technical expertise - timing, monitoring, change management"
3. **Evidence Strategy**: "Console observation gets you started, but auditing requires interviewing people and reviewing documentation"
4. **Control Questions**: "The best audit questions focus on 'how do you know it's working?' and 'what happens when it doesn't?'"

