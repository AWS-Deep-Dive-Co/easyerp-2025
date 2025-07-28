# AWS Deep Dive Training: Service Exploration & Monitoring

## Training Objective
Explore AWS native scheduling, monitoring, and orchestration capabilities through hands-on experience with Lambda, Step Functions, EventBridge, CloudWatch, and Glue services.

## What You'll Learn
- **AWS EventBridge**: Event-driven scheduling and automation
- **AWS Lambda**: Serverless compute patterns and best practices  
- **AWS Step Functions**: Visual workflow orchestration and error handling
- **AWS Glue**: Managed ETL service capabilities
- **AWS CloudWatch**: Comprehensive monitoring, alerting, and observability
- **AWS CloudTrail**: API auditing and governance

---

## Deployment Instructions

Deploy the unified template `aws-deep-dive-training-unified.yaml` with these parameters:
- **EnvironmentName**: `aws-deep-dive`
- **S3BucketName**: `your-github-sync-bucket-name`

This creates a complete AWS service demonstration environment:

### 🚀 **AWS Lambda Functions**
- **2 Functions**: Demonstrate different execution patterns
- **EventBridge Scheduling**: Automated invocation every 5-15 minutes
- **Built-in Error Simulation**: 15% random failure rate for realistic scenarios
- **CloudWatch Integration**: Automatic logging and metrics

### 🔄 **AWS Step Functions**  
- **Visual Workflow**: Complex state machine with branching logic
- **Error Handling**: Retry policies and catch blocks
- **Lambda Integration**: Orchestrates multiple function calls
- **EventBridge Triggering**: Scheduled execution every 30 minutes

### 📊 **AWS Glue Jobs**
- **Managed ETL Service**: Serverless data processing
- **Spark-based Processing**: Scalable data transformation
- **EventBridge Scheduling**: Multiple job frequencies (10-20 minutes)
- **CloudWatch Monitoring**: Job status and performance metrics

### 📈 **CloudWatch Dashboards**
- **Real-time Monitoring**: Service health and performance
- **Custom Metrics**: Application-specific measurements
- **Alerting Integration**: Visual indicators of system state
- **Multi-service Views**: Unified operational visibility

### 🔍 **CloudTrail Auditing**
- **API Call Tracking**: Complete audit trail of service interactions
- **Management Events**: Console actions and API calls
- **Security Monitoring**: Access patterns and configuration changes

---

## Service Exploration Activities

### Activity 1: EventBridge Scheduling Deep Dive

**Objective**: Understand AWS native scheduling capabilities

1. **Navigate to EventBridge Console**: `https://console.aws.amazon.com/events/home`
2. **Examine Rules**: Find rules starting with `aws-deep-dive-`
3. **Key Learning Points**:
   - How EventBridge targets multiple AWS services
   - Cron expressions for complex scheduling
   - Event-driven architecture patterns
   - Integration with Lambda, Step Functions, and Glue

**Hands-on Exploration**:
```bash
# List all EventBridge rules
aws events list-rules --name-prefix aws-deep-dive

# Describe a specific rule
aws events describe-rule --name aws-deep-dive-daily-transaction-schedule

# View rule targets
aws events list-targets-by-rule --rule aws-deep-dive-daily-transaction-schedule
```

### Activity 2: Lambda Function Patterns

**Objective**: Explore serverless compute capabilities and monitoring

1. **Navigate to Lambda Console**: `https://console.aws.amazon.com/lambda/home`
2. **Examine Functions**: 
   - `aws-deep-dive-daily-transaction-processor`
   - `aws-deep-dive-month-end-processor`

**Test Different Execution Patterns**:

**Standard Execution**:
```json
{
  "source": "service-exploration",
  "test_mode": true,
  "timestamp": "2025-01-27T00:00:00Z"
}
```

**Error Simulation** (observe CloudWatch response):
```json
{
  "source": "service-exploration",
  "forceFailure": {
    "databaseTimeout": true
  }
}
```

**Key Learning Points**:
- Lambda execution environment lifecycle
- CloudWatch Logs automatic integration
- Error handling and retry behavior
- Performance monitoring through CloudWatch metrics

### Activity 3: Step Functions Workflow Orchestration

**Objective**: Master visual workflow orchestration

1. **Navigate to Step Functions Console**: `https://console.aws.amazon.com/states/home`
2. **Open Workflow**: `aws-deep-dive-financial-processing-workflow`
3. **Examine Definition**: Study the Amazon States Language (ASL)

**Execute with Different Inputs**:

**Basic Execution**:
```json
{
  "source": "step-functions-exploration",
  "batch_size": 100
}
```

**Error Handling Demonstration**:
```json
{
  "source": "step-functions-exploration",
  "forceFailure": {
    "criticalFailure": true
  }
}
```

**Key Learning Points**:
- Visual workflow design capabilities
- Error handling with Retry and Catch blocks
- Parallel execution patterns
- Integration with multiple AWS services
- State machine execution history and debugging

### Activity 4: CloudWatch Monitoring Mastery

**Objective**: Deep dive into AWS observability

1. **Navigate to CloudWatch Dashboards**: `https://console.aws.amazon.com/cloudwatch/home#dashboards:`
2. **Explore Dashboards**:
   - `aws-deep-dive-operational-monitoring`
   - `aws-deep-dive-sox-compliance-monitoring`

**Key Monitoring Capabilities**:
- **Lambda Metrics**: Duration, errors, invocations, throttles
- **Step Functions Metrics**: Executions, failures, duration
- **Glue Job Metrics**: Success rate, duration, DPU usage
- **Custom Application Metrics**: Business logic measurements
- **Cross-service Correlation**: Understanding service dependencies

**Explore CloudWatch Features**:
```bash
# List custom metrics
aws cloudwatch list-metrics --namespace FinancialProcessing

# Get metric statistics
aws cloudwatch get-metric-statistics \
  --namespace FinancialProcessing \
  --metric-name ProcessingSuccessRate \
  --dimensions Name=ProcessType,Value=DailyTransaction \
  --start-time 2025-01-27T00:00:00Z \
  --end-time 2025-01-27T23:59:59Z \
  --period 300 \
  --statistics Average
```

### Activity 5: CloudTrail API Auditing

**Objective**: Understand AWS API auditing and governance

1. **Navigate to CloudTrail**: `https://console.aws.amazon.com/cloudtrail/home#/events`
2. **Search Events**: Your console actions appear as API calls
3. **Key Learning Points**:
   - Complete API call audit trail
   - Security and compliance monitoring
   - Troubleshooting service interactions
   - Change tracking and accountability

---

## Advanced Service Integration Scenarios

### Scenario 1: EventBridge → Lambda Integration
**Purpose**: Understand event-driven architecture
1. Observe how EventBridge schedules trigger Lambda functions
2. Examine payload transformation between services
3. Study error handling when Lambda functions fail

### Scenario 2: Step Functions Service Orchestration
**Purpose**: Master multi-service workflows
1. Watch Step Functions coordinate Lambda and Glue jobs
2. Observe parallel execution patterns
3. Study error propagation and recovery mechanisms

### Scenario 3: CloudWatch Cross-Service Monitoring
**Purpose**: Implement comprehensive observability
1. Correlate metrics across Lambda, Step Functions, and Glue
2. Understand service dependency visualization
3. Practice troubleshooting using CloudWatch insights

### Scenario 4: Failure Recovery Patterns
**Purpose**: Study AWS service resilience
1. Force failures in different services
2. Observe automatic retry mechanisms
3. Study how services isolate and recover from failures

---

## Service Capabilities Exploration

### AWS Lambda Deep Dive
- **Execution Models**: Synchronous vs asynchronous invocation
- **Scaling Behavior**: Automatic concurrency management
- **Integration Patterns**: Event sources and destinations
- **Monitoring**: CloudWatch metrics and X-Ray tracing
- **Cost Optimization**: Right-sizing and efficient execution

### AWS Step Functions Mastery
- **State Types**: Task, Choice, Wait, Parallel, Map states
- **Error Handling**: Comprehensive retry and catch mechanisms
- **Integration Patterns**: Request-response, run job, wait for callback
- **Visual Debugging**: Execution history and state inspection
- **Service Integration**: Native AWS service connectors

### AWS EventBridge Event-Driven Architecture
- **Event Patterns**: Content-based routing
- **Scheduling**: Cron and rate expressions
- **Cross-Account Events**: Multi-account integration patterns
- **Custom Event Buses**: Application-specific event routing
- **Archive and Replay**: Event history management

### AWS Glue Data Processing
- **Serverless Spark**: Managed Apache Spark execution
- **Data Catalog**: Metadata management and discovery
- **ETL Patterns**: Extract, transform, load operations
- **Performance Optimization**: DPU allocation and job tuning
- **Cost Management**: Efficient resource utilization

### CloudWatch Observability
- **Metrics**: Standard and custom metric collection
- **Dashboards**: Visual monitoring and alerting
- **Logs**: Centralized log aggregation and analysis
- **Alarms**: Automated notification and response
- **Insights**: Log query and analysis capabilities

---

## Training URLs Quick Reference

- **EventBridge Console**: `https://console.aws.amazon.com/events/home`
- **Lambda Console**: `https://console.aws.amazon.com/lambda/home`
- **Step Functions Console**: `https://console.aws.amazon.com/states/home`
- **Glue Console**: `https://console.aws.amazon.com/glue/home`
- **CloudWatch Dashboards**: `https://console.aws.amazon.com/cloudwatch/home#dashboards:`
- **CloudWatch Logs**: `https://console.aws.amazon.com/cloudwatch/home#logsV2:logs-insights`
- **CloudTrail Events**: `https://console.aws.amazon.com/cloudtrail/home#/events`

---

## Service-Focused Learning Outcomes

After completing this training, participants will:

1. **Understand AWS Native Scheduling**: Master EventBridge for complex automation scenarios
2. **Implement Serverless Patterns**: Design efficient Lambda-based solutions
3. **Orchestrate Multi-Service Workflows**: Use Step Functions for complex business processes
4. **Monitor Production Systems**: Implement comprehensive CloudWatch observability
5. **Process Data at Scale**: Leverage AWS Glue for ETL operations
6. **Ensure Governance**: Use CloudTrail for audit and compliance requirements

This hands-on exploration provides practical experience with AWS services that are fundamental to modern cloud architectures and serverless applications.
