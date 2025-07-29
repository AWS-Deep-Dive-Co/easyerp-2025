# PowerPoint Slide Layout - AWS Services for Auditors (2 Hours)

## Slide Deck Overview
**Total Slides**: 19 slides
**Presentation Time**: 60 minutes (60 minutes for activities)
**Design**: Professional audit-focused template with AWS service screenshots

---

## Opening Section (Slides 1-4)

### Slide 1: Title Slide
**Title**: AWS Services Overview for Auditors
**Subtitle**: Understanding Cloud Services in Client Environments
**Footer**: [Date] | [Instructor Name] | Duration: 2 Hours

**Voiceover Notes**:
*"Good morning, everyone. Welcome to our AWS Services Overview for Auditors. I'm [Name] and for the next two hours, we're going to explore the AWS services you're most likely to encounter in your client environments. This isn't a technical deep dive - instead, we're focusing on what these services mean for your audits, what evidence they provide, and how to approach them from an audit perspective. By the end of today, you'll have hands-on experience with the AWS console and a clear framework for auditing cloud-based business processes."*

### Slide 2: Learning Objectives & Agenda
**Header**: What You'll Learn Today
**Two-Column Layout**:
**Left - Objectives**:
- Identify AWS monitoring and audit evidence sources
- Understand automated cloud business processes
- Connect AWS services to audit frameworks
- Develop cloud audit approaches

**Right - Agenda**:
- 0:00-0:20: Monitoring & Compliance Foundation
- 0:20-0:40: Scheduling & Automation Services
- 0:40-0:60: Workflow & Data Processing
- 1:00-2:00: Hands-On Activities (3 activities)

**Voiceover Notes**:
*"Let's look at what we'll accomplish today. Our learning objectives are very practical - you'll learn to identify where audit evidence lives in AWS, understand how automated processes work, and develop approaches for auditing these systems. Notice our agenda starts with monitoring and compliance services - that's intentional. CloudWatch and CloudTrail are your audit evidence hubs, so we'll establish that foundation first. Then we'll explore the services that generate that evidence. The second half is entirely hands-on - you'll get direct experience with the AWS console. Any questions before we dive in?"*

### Slide 3: Demo Environment Overview
**Header**: What We'll Explore Today
**Screenshot**: AWS console overview with deployed services
**Note**: "Live AWS environment with real business processes running"

**Voiceover Notes**:
*"This is what we'll be working with today - a live AWS environment running real business processes. You're looking at the AWS Management Console, which is where auditors typically get access to view these systems. We've deployed a complete financial processing environment that includes scheduled transactions, automated workflows, data processing jobs, and comprehensive monitoring. Everything you see here represents actual business processes that could be running at your clients. The key difference from traditional systems is that everything is automated, integrated, and generates rich audit trails. Let's start by understanding where that audit evidence lives."*

---

## Segment 1: Monitoring & Compliance Foundation (Slides 4-7)

### Slide 4: CloudWatch - Your Audit Evidence Hub
**Header**: AWS CloudWatch
**Split Screen**:
- **Left**: Dashboard screenshot showing business metrics
- **Right**: Key audit capabilities:
  - Real-time operational metrics
  - Custom compliance dashboards  
  - Automated alerting for exceptions
  - Historical trend analysis

**Voiceover Notes**:
*"CloudWatch is your audit evidence hub - this is where all the operational data lives. Think of it as the central monitoring system for AWS environments. On the left, you see a dashboard showing real business metrics - transaction volumes, processing times, error rates, compliance scores. This isn't just technical monitoring; it's business process monitoring. CloudWatch provides real-time operational metrics, custom compliance dashboards that clients can configure for SOX or other requirements, automated alerting when things go wrong, and historical trend analysis. For auditors, this means you have access to comprehensive performance data, exception identification, and trend analysis that would be difficult to get from traditional systems."*

### Slide 5: CloudTrail - Complete Audit Trail
**Header**: AWS CloudTrail
**Split Screen**:
- **Left**: CloudTrail event log screenshot
- **Right**: Audit evidence provided:
  - Who made changes (user identity)
  - What was changed (API calls)
  - When changes occurred (timestamps)
  - Where changes originated (source IP)

**Voiceover Notes**:
*"CloudTrail is your complete audit trail for changes and access. While CloudWatch shows you what's happening operationally, CloudTrail shows you who did what, when they did it, and from where. Every single action in AWS - whether it's a user clicking in the console, an automated process making changes, or a system integration - gets logged to CloudTrail. You can see who made changes by looking at user identity, what was changed through API call details, when changes occurred with precise timestamps, and where changes originated through source IP addresses. This gives you a level of audit trail completeness that's often superior to traditional systems. For change management testing, access reviews, and segregation of duties assessment, CloudTrail is invaluable."*

### Slide 6: Live Demo - Monitoring Services
**Header**: CloudWatch & CloudTrail in Action
**Note**: [LIVE DEMONSTRATION - 5 minutes]
**Show**:
- Business process dashboards
- Compliance monitoring metrics
- Recent system changes in CloudTrail
- How services integrate for complete visibility

**Voiceover Notes**:
*"Let me show you these services in action. [Switch to live AWS console] Here's our CloudWatch dashboard showing real business processes. You can see transaction processing rates, success percentages, and compliance scores updating in real time. Notice how this gives us immediate visibility into business process health. Now let's look at CloudTrail. [Navigate to CloudTrail] Here you can see recent events - system changes, user actions, automated processes. Each entry shows us the who, what, when, and where I mentioned. This integration between operational monitoring and audit trails gives us comprehensive visibility that supports both control testing and substantive procedures. In your activities, you'll navigate these interfaces directly."*

### Slide 7: Monitoring - Audit Applications
**Header**: How to Use Monitoring for Audit Evidence
**Bullet Points**:
- **Process Understanding**: Use dashboards to understand business flows
- **Exception Testing**: Identify anomalies and control failures
- **Change Management**: Track system modifications and authorizations
- **Compliance Reporting**: Leverage automated compliance metrics

**Voiceover Notes**:
*"Now that you understand what CloudWatch and CloudTrail provide, let's talk about practical audit applications. First, use dashboards for process understanding - instead of requesting process documentation, you can see how business processes actually perform in real time. Second, for exception testing, these tools help you identify anomalies and control failures automatically rather than through sampling. Third, for change management, you get complete tracking of system modifications and can verify proper authorization. Finally, for compliance reporting, you can leverage automated compliance metrics rather than building them from scratch. The key insight is that AWS provides richer audit evidence than many traditional systems, but you need to know where to look and how to interpret it. Now let's see what services generate this monitoring data."*

---

## Segment 2: Scheduling & Automation Services (Slides 8-11)

### Slide 8: EventBridge - Process Scheduling
**Header**: AWS EventBridge
**Split Screen**:
- **Left**: EventBridge rules console screenshot
- **Right**: Audit significance:
  - Controls **when** business processes execute
  - Scheduled vs. event-driven automation
  - **Monitored via CloudWatch** (reference back)
  - Change management through CloudTrail logging

**Voiceover Notes**:
*"EventBridge controls when business processes execute. Think of it as the scheduling engine for automated business processes. It handles both scheduled automation - like month-end closes that run at specific times - and event-driven automation where one process triggers another. From an audit perspective, EventBridge is significant because it controls the timing and triggering of critical business processes. Notice how it's monitored via CloudWatch - remember our foundation? All execution metrics, success rates, and failure patterns flow back to CloudWatch. Changes to schedules and rules are logged in CloudTrail for change management testing. When you're auditing automated processes, EventBridge rules tell you when things should happen and provide evidence of whether they actually did."*

### Slide 9: Lambda - Business Logic Execution  
**Header**: AWS Lambda
**Split Screen**:
- **Left**: Lambda function console with monitoring tab
- **Right**: Audit considerations:
  - Contains critical business rule implementations
  - **Performance tracked in CloudWatch**
  - Execution logs provide audit trail
  - Integration with EventBridge for automation

**Voiceover Notes**:
*"Lambda is where the actual business logic executes. If EventBridge controls when processes run, Lambda controls what those processes do. Lambda functions contain the code that implements business rules - calculating financial transactions, applying approval logic, validating data, generating reports. From an audit perspective, Lambda is significant because it houses critical business rule implementations. The performance of every Lambda execution is tracked in CloudWatch - you can see how long functions take to run, error rates, and resource usage. Execution logs provide a complete audit trail of what happened during each run. Lambda integrates with EventBridge for automation, so you can trace the complete flow from trigger to execution. When auditing business processes, Lambda functions often contain the core logic you need to understand and test."*

### Slide 10: Live Demo - Scheduling Services
**Header**: EventBridge & Lambda Integration
**Note**: [LIVE DEMONSTRATION - 5 minutes]
**Show**:
- How EventBridge rules trigger Lambda functions
- **CloudWatch metrics** for execution monitoring
- Error handling and retry mechanisms
- End-to-end process automation

**Voiceover Notes**:
*"Let me show you how these services work together. [Switch to AWS console] Here's an EventBridge rule that triggers every 5 minutes. You can see it targets this Lambda function for daily transaction processing. [Click on Lambda function] Here's the function code - this is implementing business logic for processing financial transactions. Now look at the monitoring tab - [show CloudWatch metrics] you can see execution history, duration trends, and error rates. This gives us complete visibility into automated business process performance. [Show error handling] Notice the retry logic and error handling built into the system. This integration between EventBridge and Lambda, monitored through CloudWatch, represents how modern automated business processes work."*

### Slide 11: Scheduling - Audit Applications
**Header**: Auditing Automated Business Processes
**Key Points**:
- **Process Timing**: Verify schedules match business requirements
- **Error Handling**: Test exception processing and escalation  
- **Performance Monitoring**: Use CloudWatch data for substantive testing
- **Change Controls**: Validate authorization for schedule modifications

**Voiceover Notes**:
*"Now let's talk about practical audit applications for scheduling services. From an auditing perspective, these automated processes require specific control testing. Process timing verification - you need to confirm that automated schedules actually match documented business requirements. A monthly report shouldn't be running daily, and a daily process shouldn't be missing weekends. Error handling testing - you need to validate that exceptions are properly processed and escalated. What happens when a data source is unavailable? Performance monitoring using CloudWatch data provides quantitative evidence for substantive testing - you can analyze actual execution times, failure rates, and resource utilization patterns. Change controls are critical - any modifications to automated schedules should require proper authorization and documentation. These scheduling services represent critical business process controls that require comprehensive audit attention."*

---

## Segment 3: Workflow & Data Processing (Slides 12-15)

### Slide 12: Step Functions - Process Orchestration
**Header**: AWS Step Functions
**Split Screen**:
- **Left**: Visual workflow diagram screenshot
- **Right**: Audit value:
  - Visual documentation of complex business processes
  - Complete execution history and audit trails
  - **Integrated CloudWatch monitoring**
  - Error handling and recovery mechanisms

**Voiceover Notes**:
*"Step Functions takes us from simple automation to complex business process orchestration. While EventBridge and Lambda handle individual tasks, Step Functions coordinates multiple services, decisions, and approval stages into complete business processes. The visual workflow diagram is incredibly valuable for auditors - it's like having a business process flowchart that's automatically maintained and executable. You can see decision points, parallel processing, error handling paths, and approval stages all in one view. Every execution creates a complete audit trail - you can trace exactly which path was taken, how long each step took, what data was processed, and where any failures occurred. The integrated CloudWatch monitoring provides quantitative performance data for every workflow execution. Error handling and recovery mechanisms are explicitly defined and testable. This makes Step Functions perfect for auditing complex processes like order fulfillment, approval workflows, or financial processing."*

### Slide 13: AWS Glue - Data Processing
**Header**: AWS Glue ETL Jobs
**Split Screen**:
- **Left**: Glue job execution console
- **Right**: Data processing controls:
  - Transforms raw data into business information
  - **Performance metrics in CloudWatch**
  - Job execution logs and error tracking
  - Data quality and validation capabilities

**Voiceover Notes**:
*"AWS Glue handles the critical function of data processing and transformation. Raw data from various sources needs to be cleaned, transformed, and structured before it becomes useful business information. From an audit perspective, Glue is significant because data integrity depends on these transformation processes working correctly. Glue jobs have built-in data quality and validation capabilities - they can detect anomalies, validate data formats, and flag quality issues. Performance metrics are tracked in CloudWatch, so you can monitor data processing volumes, execution times, and success rates. Job execution logs provide detailed tracking of what transformations were applied to which data sets. When auditing data-driven business processes, understanding and testing these ETL transformations is critical for ensuring data accuracy and completeness."*

### Slide 14: Live Demo - Workflow Services
**Header**: Step Functions & Glue Integration
**Note**: [LIVE DEMONSTRATION - 5 minutes]
**Show**:
- Step Functions workflow orchestrating business processes
- Glue jobs processing business data
- **CloudWatch dashboards** showing end-to-end monitoring
- How services work together in integrated processes

**Voiceover Notes**:
*"Let me demonstrate how these workflow services integrate to create comprehensive business processes. [Switch to AWS console] Here's a Step Functions workflow that coordinates a complete data processing pipeline. [Show workflow diagram] You can see it starts with data validation, moves through multiple transformation steps, includes approval checkpoints, and ends with report generation. [Click on execution history] Each execution shows complete traceability - every step, timing, and decision. [Switch to Glue console] The Glue jobs handle the heavy data processing work. [Show job runs] You can see execution history, data volumes processed, and performance trends. [Switch to CloudWatch] The real power is in the integrated monitoring - [show dashboard] this CloudWatch dashboard shows end-to-end visibility across the entire process, from workflow orchestration to data processing performance. This integrated approach gives auditors complete visibility into complex business processes."*

### Slide 15: Workflow - Audit Applications
**Header**: Auditing Complex Business Processes
**Focus Areas**:
- **Process Documentation**: Use visual workflows for understanding
- **Data Integrity**: Test ETL processes and data transformations
- **End-to-End Monitoring**: Leverage integrated CloudWatch visibility
- **Control Testing**: Validate approval checkpoints and error handling

**Voiceover Notes**:
*"Workflow services create powerful opportunities for comprehensive audit testing. Process documentation becomes visual and automatically maintained - Step Functions diagrams show you exactly how business processes work, including decision points and approval stages. Data integrity testing can focus on the ETL processes themselves - you can validate data transformations, test error handling, and verify that data quality controls are working effectively. End-to-end monitoring through integrated CloudWatch visibility means you can track complete business processes from initiation to completion, with quantitative performance data at every step. Control testing becomes more comprehensive because you can validate approval checkpoints, test exception handling, and verify that segregation of duties is properly implemented in automated workflows. These services transform audit testing from sampling-based approaches to comprehensive process validation."*
- **Process Completeness**: Validate all steps execute as designed

---

## Integration & Activities (Slides 16-19)

### Slide 16: How Services Work Together
**Header**: Integrated AWS Business Processes
**Visual**: Service integration diagram showing:
EventBridge → Lambda → Step Functions → Glue → CloudWatch/CloudTrail
**Key Message**: "All services feed monitoring data to CloudWatch and change logs to CloudTrail"

**Voiceover Notes**:
*"Before we dive into hands-on practice, let's see how all these services work together in integrated business processes. EventBridge schedules and triggers processes, Lambda executes the business logic, Step Functions orchestrates complex workflows, and Glue handles data processing. The critical point for auditors is that all services feed monitoring data to CloudWatch and change logs to CloudTrail. This creates a comprehensive audit trail across the entire business process ecosystem. You're not auditing individual services in isolation - you're auditing integrated business processes where each service contributes to the overall control environment. This integration is what makes cloud-based business processes both powerful and auditable."*

### Slide 17: Audit Approach Summary
**Header**: Your AWS Audit Toolkit
**Table Format**:
| Service | What It Does | Where to Find Evidence | How CloudWatch/CloudTrail Help |
|---------|--------------|------------------------|--------------------------------|
| EventBridge | Schedules processes | Rules and targets | Execution metrics and change logs |
| Lambda | Executes business logic | Function logs and metrics | Performance data and modifications |
| Step Functions | Orchestrates workflows | Execution history | Success rates and updates |
| Glue | Processes data | Job execution logs | Processing metrics and job changes |

**Voiceover Notes**:
*"Here's your practical AWS audit toolkit summarized in one view. For each service, you know what it does in business processes, where to find audit evidence, and how the monitoring services support your testing. EventBridge scheduling evidence comes from rules and targets, with CloudWatch providing execution metrics and CloudTrail logging any changes. Lambda business logic evidence is in function logs and metrics, with performance data and modification history available through monitoring. Step Functions workflow evidence is in execution history, with success rates and updates tracked comprehensively. Glue data processing evidence comes from job execution logs, with processing metrics and job changes fully documented. This systematic approach ensures you can audit any AWS-based business process effectively."*

### Slide 18: Hands-On Activities Introduction
**Header**: Time to Explore
**Three Activities Overview**:
- **Activity 1**: EventBridge + CloudWatch (Scheduling & Monitoring)
- **Activity 2**: Step Functions + CloudWatch (Workflows & Performance)  
- **Activity 3**: Glue + CloudWatch (Data Processing & Comprehensive Monitoring)
**Note**: "Each activity integrates monitoring to show real audit applications"

**Voiceover Notes**:
*"Now it's time to put everything into practice with three comprehensive hands-on activities. Activity 1 focuses on EventBridge and CloudWatch, exploring scheduling and monitoring integration. You'll see how automated processes are scheduled and how their performance is tracked. Activity 2 covers Step Functions and CloudWatch, diving into workflow orchestration and performance monitoring. You'll explore complex business processes and understand how they're audited end-to-end. Activity 3 examines Glue and CloudWatch, focusing on data processing and comprehensive monitoring. You'll see how data transformations are tracked and validated. Each activity integrates monitoring services to show real audit applications. These aren't theoretical exercises - they're practical explorations of the audit evidence you'll encounter in real AWS environments."*

### Slide 19: Questions & Next Steps
**Header**: Thank You & Resources
**Split Layout**:
**Left - Q&A**: Open discussion time
**Right - Resources**:
- Training materials and AWS documentation
- Follow-up learning opportunities
- Contact information for continued support

**Voiceover Notes**:
*"Thank you for your attention and participation in today's AWS services deep dive. We've covered the monitoring foundation with CloudWatch and CloudTrail, explored scheduling services through EventBridge and Lambda, examined workflow processing with Step Functions and Glue, and seen how these services integrate to create comprehensive, auditable business processes. You now have practical experience with the AWS console and understand how to find audit evidence in cloud-based business processes. The training materials and AWS documentation will continue to be available for your reference. We've also identified follow-up learning opportunities for those who want to deepen their AWS audit skills. Please don't hesitate to reach out with questions as you begin applying these concepts in your audit work. Your feedback on today's training will help us continue improving this program for future participants."*

---

## Slide Design Guidelines

### Visual Standards:
- **Professional Color Scheme**: Navy blue, gray, and white with AWS orange accents
- **Consistent Fonts**: Arial or Calibri for readability
- **High-Quality Screenshots**: Current AWS console interfaces
- **Minimal Text**: Key points only, rely on demos for detail

### Interactive Elements:
- **Live Demo Slides**: 5-minute focused demonstrations
- **Split Screen Layouts**: Service overview + audit significance
- **Integration Focus**: Every service connected back to monitoring

### Audit-Focused Approach:
- **Evidence-Oriented**: Emphasize what auditors can observe and test
- **Risk-Based Framing**: Connect all content to audit risk assessment
- **Monitoring Integration**: CloudWatch/CloudTrail referenced throughout
- **Practical Application**: Clear connection to hands-on activities

This streamlined 19-slide approach provides focused content delivery in 60 minutes, leaving a full hour for hands-on exploration with proper monitoring foundation established upfront.
