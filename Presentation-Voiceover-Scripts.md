# SOX Auditor Training: Presentation Voiceover Scripts
## CloudWatch & CloudTrail Monitoring - 2 Hour Session

---

## Opening Introduction (5 minutes)

### Slide 1: Welcome & Learning Objectives

**Voiceover Script:**
"Good morning, everyone, and welcome to Day 3 of our SOX IT auditing training. Today we're diving into one of the most critical aspects of modern IT auditing - monitoring scheduled processes in the cloud using AWS CloudWatch and CloudTrail.

By the end of today's session, you'll be confident in interpreting monitoring dashboards, identifying control failures through log analysis, and using CloudTrail for access auditing. Most importantly, you'll know how to gather the audit evidence that supports your SOX testing procedures.

Now, I want to be clear about something from the start - we're not here to make you AWS system administrators. Your role as auditors is to interpret what these systems are telling you about the effectiveness of controls. Think of it like reviewing bank statements - you don't need to know how the bank's core systems work, but you need to understand what the statements reveal about the controls over cash management."

### Slide 2: Why This Matters for SOX Auditors

**Voiceover Script:**
"Let me paint a picture for you. Last year, a Fortune 500 client had a month-end close process that failed silently for three days. The finance team didn't know because they weren't monitoring the right metrics. When we discovered this during our audit, it raised significant questions about management's monitoring controls.

In today's environment, your clients are increasingly moving their financial processes to the cloud. These aren't just simple applications anymore - they're complex, interconnected systems with Lambda functions processing transactions, Glue jobs transforming data, and Step Functions orchestrating entire financial workflows.

The question isn't whether your clients are using these technologies - it's whether you're prepared to audit them effectively."

---

## Section 1: Understanding AWS Services for Financial Processing (20 minutes)

### Slide 3: AWS Services Overview

**Voiceover Script:**
"Before we jump into the hands-on activities, let's establish a common understanding of the AWS services we'll be working with today.

Think of Lambda functions as the modern equivalent of batch jobs. Instead of overnight COBOL programs processing transactions, you now have Lambda functions that can run on schedules, process thousands of records, and integrate with multiple systems. The key difference? They're event-driven, highly scalable, and generate detailed logs.

AWS Glue serves as the modern ETL platform. It's where your clients extract data from their various source systems, transform it according to business rules, and load it into data warehouses for reporting. For SOX purposes, this is where data integrity controls are critical.

Step Functions act as the orchestrator - they coordinate complex business processes that involve multiple steps, systems, and approval workflows. Think of them as the digital equivalent of your client's documented procedures."

### Slide 4: Common Financial Processes in AWS

**Voiceover Script:**
"Today, we'll be working with a live AWS environment that simulates real financial processes you'll encounter at client sites. We have:

A daily transaction processor that runs every morning at 2 AM UTC - this simulates the kind of overnight batch processing that handles daily sales, payments, and journal entries.

A month-end close process that runs on the last day of each month - this is the big one, folks. This process handles account reconciliations, accrual calculations, and all the critical procedures that ensure accurate financial reporting.

We also have ETL jobs that run daily and weekly, extracting data from multiple source systems and preparing it for management reporting.

What makes this training unique is that these processes are designed to fail in realistic ways. You'll see database connection timeouts, validation errors, and access control violations - the same types of issues that can derail your client's financial reporting."

---

## Section 2: Dashboard Interpretation Deep Dive (30 minutes)

### Slide 5: Reading CloudWatch Dashboards

**Voiceover Script:**
"Now we're going to access our live SOX Compliance Dashboard. Everyone should have the URL in their training materials. Go ahead and open that now.

What you're looking at is a real-time view of financial process health. Notice how the dashboard is organized - we have process volume metrics at the top, error rates in the middle, and compliance scores at the bottom. This isn't accidental - it's designed to tell a story.

Look at the 'Daily Transaction Processing' widget in the top left. The blue line shows successfully processed transactions, while the red line shows failures. As auditors, what questions should this raise for you?"

**Pause for responses**

"Exactly - you want to know: What's the normal failure rate? Are failures being investigated? Is there a trend? Are controls working as designed?"

### GROUP ACTIVITY 1: Dashboard Analysis Challenge (15 minutes)

**Introduction:**
"Alright, let's put this into practice with your first group activity. I'm going to divide you into teams of 3-4 people. Each team will become a SOX audit team that just received access to a client's monitoring dashboard."

**Activity Instructions:**

**GROUP ACTIVITY 1: Dashboard Health Check**

**Scenario:** You're conducting a SOX 404 audit for a manufacturing company that processes 50,000+ financial transactions daily through AWS. Management claims their automated controls are working effectively.

**Your Assignment (15 minutes):**
1. **Navigate to the SOX Compliance Dashboard** (URL provided in chat)
2. **Document your findings** using the worksheet provided
3. **Prepare to present** one key finding to the class

**Questions to Answer:**
- What is the current success rate for daily transaction processing?
- Are there any error spikes in the last 24 hours?
- What does the compliance score trend tell you?
- If you saw these metrics during an audit, what follow-up procedures would you perform?

**Deliverable:** 
Each team will have 2 minutes to present one significant finding and explain what audit procedures it would trigger.

**Facilitator Instructions:**
- Walk around and observe teams
- Point out interesting patterns in the dashboards
- Help teams understand what "normal" vs "concerning" looks like

---

## Section 3: Log Investigation Masterclass (40 minutes)

### Slide 6: The Art of Log Analysis

**Voiceover Script:**
"Now we're moving from the 30,000-foot view to the details that can make or break your audit conclusion. Log analysis is where you'll find the evidence of what really happened when a process failed.

But here's the challenge - modern applications generate massive amounts of log data. A single transaction processing run might generate thousands of log entries. Your job isn't to read every line - it's to know what to look for and how to find it efficiently."

### Slide 7: Log Patterns Every Auditor Should Recognize

**Voiceover Script:**
"Let me show you some patterns you'll see repeatedly. When you see timestamps followed by INFO level messages with words like 'SUCCESS' and 'completed successfully' - that's your green flag. The process worked as designed.

But watch for patterns like this: ERROR level messages with words like 'CRITICAL', 'TIMEOUT', or 'FAILED'. These are your red flags. Even more concerning are messages that mention 'Manual intervention required' or 'Material variance detected' - these indicate control failures that could have SOX implications.

The key is learning to scan quickly for these patterns rather than reading every line sequentially."

### GROUP ACTIVITY 2: Log Investigation Challenge (25 minutes)

**Introduction:**
"Time for some detective work. Each team is going to investigate a different scenario where a financial process encountered issues. Your job is to piece together what happened using CloudWatch Logs and determine the audit implications."

**GROUP ACTIVITY 2: Process Failure Investigation**

**Scenario:** Yesterday morning, the finance team called IT saying that "something seemed wrong" with the daily transaction processing. They couldn't provide specifics, just that "the numbers didn't look right." Management needs to understand what happened before they can finalize their daily reporting.

**Your Investigation (25 minutes):**

**Phase 1: Initial Investigation (10 minutes)**
1. **Access CloudWatch Logs** (URL in training materials)
2. **Search for transaction processing logs** from yesterday 2:00-4:00 AM UTC
3. **Use this query to start:**
   ```
   fields @timestamp, @message
   | filter @message like /transaction/
   | sort @timestamp desc
   | limit 50
   ```

**Phase 2: Deep Dive Analysis (10 minutes)**
4. **Look for ERROR or WARNING messages**
5. **Identify the specific failure point**
6. **Quantify the impact** (how many transactions affected?)
7. **Document the timeline** of events

**Phase 3: Audit Assessment (5 minutes)**
8. **Determine:** Is this a control deficiency?
9. **Consider:** What testing procedures would you perform?
10. **Assess:** How would you rate the severity?

**Team Assignments:**
- **Team 1:** Focus on database connection issues
- **Team 2:** Look for validation failures
- **Team 3:** Investigate processing timeouts
- **Team 4:** Examine reconciliation variances

**Deliverable:**
Prepare a 3-minute "audit finding" presentation including:
- What went wrong?
- When did it happen?
- How many transactions were affected?
- What controls (if any) detected the issue?
- Your recommendation for management

---

## Section 4: CloudTrail for Access Auditing (25 minutes)

### Slide 8: CloudTrail - Your Digital Audit Trail

**Voiceover Script:**
"If CloudWatch tells you 'what happened,' CloudTrail tells you 'who did it.' This is where you'll find evidence of segregation of duties violations, unauthorized access, and changes to critical systems.

CloudTrail captures every API call made to AWS services. When someone starts a Lambda function, modifies a Glue job, or even just views a dashboard - it's all recorded with timestamps, user identities, and source IP addresses.

For SOX auditors, CloudTrail is your best friend for testing access controls and change management procedures."

### Slide 9: Key CloudTrail Events for SOX

**Voiceover Script:**
"Let me show you the events you should focus on as a SOX auditor. 

InvokeFunction events tell you when someone manually triggered a financial process. Was it authorized? Was it during business hours? 

CreateUser and AttachPolicy events reveal changes to access rights. These are critical for testing your client's user access reviews and segregation of duties controls.

ModifyFunction and UpdateStateMachine events show changes to the actual processing logic. Without proper change management controls, these could represent significant risks to financial reporting."

### GROUP ACTIVITY 3: Access Control Investigation (20 minutes)

**Introduction:**
"Your final group activity puts you in the role of auditors testing access controls. You've just learned that someone made unauthorized changes to a critical financial process last Friday evening. Your job is to find out who, what, and when."

**GROUP ACTIVITY 3: Unauthorized Access Investigation**

**Scenario:** During your SOX audit, you're testing the "User Access Review" control. Management states that only authorized personnel can execute or modify financial processing functions. However, the IT director mentioned there was some "unusual activity" last Friday evening that they're investigating.

**Your Investigation (20 minutes):**

**Phase 1: Identify Suspicious Activity (8 minutes)**
1. **Access CloudTrail Event History** (URL provided)
2. **Filter events for last Friday 6 PM - Monday 6 AM**
3. **Look for these event names:**
   - `InvokeFunction`
   - `StartExecution`
   - `ModifyFunctionConfiguration`
   - `CreateUser` or `AttachUserPolicy`

**Phase 2: Analyze User Activity (7 minutes)**
4. **For each suspicious event, document:**
   - User name/identity
   - Source IP address
   - Time of activity
   - What action was performed
5. **Cross-reference with authorized user list** (provided in materials)

**Phase 3: Control Assessment (5 minutes)**
6. **Evaluate:** Did segregation of duties work as designed?
7. **Determine:** Were any unauthorized personnel able to access critical functions?
8. **Assess:** Are there patterns suggesting systematic control failures?

**Red Flags to Watch For:**
- ❌ Administrative actions by non-admin users
- ❌ Financial process execution outside business hours
- ❌ API calls from unfamiliar IP addresses
- ❌ Same user both executing and approving processes

**Team Focus Areas:**
- **Team 1:** Financial process executions after hours
- **Team 2:** Permission/policy changes
- **Team 3:** Unusual geographic access patterns
- **Team 4:** Segregation of duties violations

**Deliverable:**
Each team presents a 2-minute "control testing result" including:
- Summary of access activity reviewed
- Any control violations identified
- Risk assessment (high/medium/low)
- Recommended management action

---

## Section 5: Comprehensive Scenario Challenge (20 minutes)

### The Big Challenge: Month-End Close Failure

**Voiceover Script:**
"Now we're going to put everything together with a comprehensive scenario that mirrors what you might face during a real SOX audit. This morning, you received an email from the CFO stating that last night's month-end close process 'had some issues' and they need to understand the impact before filing their 10-K.

This is it, folks - this is where theory meets practice. You have all the tools we've covered today: dashboards, logs, and audit trails. Your job is to piece together what happened and provide a recommendation to the CFO."

### CAPSTONE GROUP ACTIVITY: Month-End Close Investigation (15 minutes)

**Introduction:**
"Each team will conduct a complete investigation of a month-end close failure. You'll need to use all three monitoring tools we've covered today to build a complete picture of what went wrong."

**CAPSTONE ACTIVITY: Complete Process Investigation**

**Scenario Email from CFO:**
*"Audit Team - Last night's month-end close process encountered some problems. The process normally completes by 3 AM, but this morning we discovered it didn't finish until 6:30 AM and there may have been some data integrity issues. We need a complete analysis before we can proceed with financial statement preparation. Please investigate and provide recommendations by noon today."*

**Your Complete Investigation (15 minutes):**

**Phase 1: Dashboard Assessment (5 minutes)**
1. **Check month-end process status** on SOX Compliance Dashboard
2. **Identify any active alerts or error conditions**
3. **Review compliance metrics** for anomalies

**Phase 2: Log Analysis (6 minutes)**
4. **Find month-end processing logs** from last night
5. **Identify the specific failure point(s)**
6. **Quantify data impact** (dollar amounts, record counts)
7. **Document timeline** of the failure

**Phase 3: Access Audit (4 minutes)**
8. **Review CloudTrail** for manual interventions
9. **Verify authorized personnel** were involved in resolution
10. **Check for any unauthorized access** during the incident

**Critical Questions to Answer:**
- What specifically failed and when?
- How much data was affected?
- Were proper controls followed during incident response?
- Is there risk of material misstatement?
- What corrective actions should management take?

**Deliverable:**
Each team prepares a 3-minute "CFO briefing" including:
- **Executive Summary:** What happened in business terms
- **Technical Details:** Root cause and timeline
- **Financial Impact:** Quantified risk assessment
- **Control Assessment:** Did detective controls work?
- **Recommendations:** Immediate and long-term actions

---

## Closing & Wrap-Up (5 minutes)

### Slide 10: Key Takeaways

**Voiceover Script:**
"Let's bring this all together. Today you've learned to read the language of cloud monitoring - the dashboards that reveal process health, the logs that tell the story of what went wrong, and the audit trails that show who did what.

But more importantly, you've practiced thinking like auditors in a cloud environment. You've learned to ask the right questions: Are controls working as designed? Are failures being detected and resolved appropriately? Is there adequate segregation of duties?

These skills will serve you well as more of your clients move their financial processes to the cloud. Remember, your role isn't to become cloud engineers - it's to understand what these systems tell you about the effectiveness of internal controls."

### Slide 11: Next Steps and Resources

**Voiceover Script:**
"As you continue to encounter cloud-based financial systems in your audits, remember these key principles:

Focus on business processes, not just technology. A failed transaction is a failed transaction, whether it's in COBOL or Python.

Look for patterns in the data. One error might be an anomaly, but repeated errors suggest control deficiencies.

Always trace back to management's monitoring. The real question isn't whether systems fail - it's whether management knows when they fail and responds appropriately.

Your training materials include quick reference guides for the log patterns and CloudTrail events we covered today. Use these as checklists during your audits.

Finally, don't hesitate to ask your clients' IT teams to walk through their monitoring procedures with you. Most are happy to explain their systems, and this collaboration often reveals control gaps they hadn't considered."

### Activity Debrief & Q&A

**Voiceover Script:**
"Before we close, let's hear from each team about their capstone investigation findings. Remember, in real audits, these conversations with your audit teams are where you refine your understanding and identify areas for additional testing.

Team 1, what did your investigation reveal about the month-end close process?"

*[Allow each team to present their findings]*

"Excellent work, everyone. These presentations demonstrate exactly the kind of analytical thinking that makes for effective SOX auditing in cloud environments.

Any final questions about today's material? Remember, mastering these skills takes practice, but you now have the foundation to audit cloud-based financial processes with confidence."

---

## Facilitator Notes:

### Timing Management:
- Keep group activities to strict time limits
- Use timers visible to participants
- Have backup scenarios ready if teams finish early

### Technical Support:
- Have AWS console URLs ready in chat
- Prepare sample queries for teams that get stuck
- Monitor team progress and provide hints as needed

### Engagement Techniques:
- Walk around during group work
- Ask probing questions to deepen analysis
- Connect findings back to real SOX requirements
- Share relevant war stories from actual audits

### Assessment Points:
- Observe team collaboration and analytical thinking
- Note questions that reveal understanding gaps
- Track which concepts need reinforcement in follow-up sessions

This comprehensive approach ensures your SOX auditors leave with practical skills they can immediately apply in client environments.
