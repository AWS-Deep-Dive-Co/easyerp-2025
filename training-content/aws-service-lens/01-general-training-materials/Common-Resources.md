# Shared Training Resources

## Infrastructure Template
**Location**: `aws-deep-dive-training-unified.yaml`
**Purpose**: Complete AWS training infrastructure that supports multiple training approaches
**Status**: Production-ready, fully tested

### Deployed Services:
- **AWS Lambda**: 2 functions with comprehensive error simulation
- **AWS Step Functions**: Complex workflow with error handling
- **AWS Glue**: 2 ETL jobs with realistic data processing
- **AWS EventBridge**: Automated scheduling for all services
- **AWS CloudWatch**: Complete monitoring dashboards and custom metrics
- **AWS CloudTrail**: API auditing and compliance tracking

### Key Features:
- **Training-Optimized Scheduling**: All processes run every 5-30 minutes for rapid data population
- **Forced Failure Capabilities**: Predictable error scenarios for teaching
- **Comprehensive Monitoring**: Real-time dashboards and alerting
- **Cost-Efficient**: Designed for training sessions, not continuous production

---

## Common Deployment Parameters

```yaml
EnvironmentName: aws-deep-dive
S3BucketName: your-github-sync-bucket-name
```

These parameters work for both financial process and AWS service training approaches.

---

## Universal Console URLs

These URLs work regardless of training approach:

### AWS Service Consoles:
- **EventBridge**: `https://console.aws.amazon.com/events/home`
- **Lambda**: `https://console.aws.amazon.com/lambda/home`
- **Step Functions**: `https://console.aws.amazon.com/states/home`
- **Glue**: `https://console.aws.amazon.com/glue/home`
- **CloudWatch Dashboards**: `https://console.aws.amazon.com/cloudwatch/home#dashboards:`
- **CloudWatch Logs**: `https://console.aws.amazon.com/cloudwatch/home#logsV2:logs-insights`
- **CloudTrail**: `https://console.aws.amazon.com/cloudtrail/home#/events`

### Deployed Resources:
- **Lambda Functions**:
  - `aws-deep-dive-daily-transaction-processor`
  - `aws-deep-dive-month-end-processor`
- **Step Functions Workflow**: `aws-deep-dive-financial-processing-workflow`
- **Glue Jobs**:
  - `aws-deep-dive-financial-etl-job`
  - `aws-deep-dive-compliance-validation-job`
- **CloudWatch Dashboards**:
  - `aws-deep-dive-operational-monitoring`
  - `aws-deep-dive-sox-compliance-monitoring`

---

## Standard Test Payloads

### Basic Function Testing:
```json
{
  "test": true,
  "source": "training-test",
  "timestamp": "2025-01-27T00:00:00Z"
}
```

### Error Simulation:
```json
{
  "source": "training-error-demo",
  "forceFailure": {
    "databaseTimeout": true
  }
}
```

### Step Functions Input:
```json
{
  "source": "training-workflow",
  "test_mode": true,
  "batch_size": 100
}
```

---

## Common CLI Commands

### Deployment Verification:
```bash
# Check EventBridge rules
aws events list-rules --name-prefix aws-deep-dive

# Verify Lambda functions
aws lambda list-functions | grep aws-deep-dive

# Confirm Step Functions
aws stepfunctions list-state-machines | grep aws-deep-dive

# Check Glue jobs
aws glue get-jobs | grep aws-deep-dive
```

### Manual Execution:
```bash
# Trigger Lambda function
echo '{"test":true,"source":"manual-test"}' > payload.json
aws lambda invoke --function-name aws-deep-dive-daily-transaction-processor --payload file://payload.json response.json

# Start Step Functions execution
aws stepfunctions start-execution \
  --state-machine-arn "arn:aws:states:REGION:ACCOUNT:stateMachine:aws-deep-dive-financial-processing-workflow" \
  --input '{"source":"manual-test","test_mode":true}'

# Run Glue job
aws glue start-job-run --job-name aws-deep-dive-financial-etl-job
```

### Monitoring:
```bash
# List custom metrics
aws cloudwatch list-metrics --namespace FinancialProcessing

# Check recent Lambda invocations
aws logs describe-log-groups --log-group-name-prefix /aws/lambda/aws-deep-dive
```

---

## PowerShell Commands (Windows)

### Manual Function Testing:
```powershell
@'
{
  "test": true,
  "source": "powershell-test"
}
'@ | Out-File -FilePath "payload.json" -Encoding UTF8

aws lambda invoke --function-name aws-deep-dive-daily-transaction-processor --payload file://payload.json response.json

Remove-Item "payload.json"
```

### Error Simulation:
```powershell
@'
{
  "source": "powershell-error-test",
  "forceFailure": {
    "complianceViolations": true
  }
}
'@ | Out-File -FilePath "failure.json" -Encoding UTF8

aws lambda invoke --function-name aws-deep-dive-month-end-processor --payload file://failure.json response.json

Remove-Item "failure.json"
```

---

## Standard Cleanup Procedure

**For Single Unified Stack**:
```bash
aws cloudformation delete-stack --stack-name aws-deep-dive-training-stack
```

**For Individual Stacks** (delete in this order):
```bash
aws cloudformation delete-stack --stack-name aws-deep-dive-monitoring-stack
aws cloudformation delete-stack --stack-name aws-deep-dive-stepfunctions-stack
aws cloudformation delete-stack --stack-name aws-deep-dive-glue-stack
aws cloudformation delete-stack --stack-name aws-deep-dive-lambda-stack
```

---

## Troubleshooting Guide

### Common Issues:

**Functions Not Appearing in Console**:
- Verify correct AWS region
- Check CloudFormation stack status
- Confirm IAM permissions

**No Data in Dashboards**:
- Wait 15-30 minutes after deployment
- Manually trigger functions to populate metrics
- Verify custom metrics namespace exists

**Permission Errors**:
- Check CloudTrail for specific permission denials
- Verify IAM roles attached to resources
- Confirm execution role policies

**Step Functions Execution Failures**:
- Check input JSON format
- Verify Lambda function exists and is enabled
- Review Step Functions execution history

### Debug Commands:
```bash
# Check CloudFormation stack status
aws cloudformation describe-stacks --stack-name aws-deep-dive-training-stack

# View recent errors in Lambda logs
aws logs filter-log-events --log-group-name /aws/lambda/aws-deep-dive-daily-transaction-processor --filter-pattern ERROR

# Check Step Functions execution status
aws stepfunctions list-executions --state-machine-arn <state-machine-arn> --status-filter FAILED
```

---

## Cost Optimization Notes

**Training-Specific Optimizations**:
- EventBridge rules run frequently (5-30 minutes) for rapid data generation
- Lambda functions have minimal memory allocation (128-256 MB)
- Glue jobs use minimal DPU allocation (2-5 DPUs)
- CloudWatch log retention set to 7 days

**Expected Training Costs**:
- **4-hour session**: $5-15 USD
- **Full-day workshop**: $10-25 USD
- **Multi-day training**: $25-50 USD

**Cost Monitoring**:
- Enable billing alerts before training
- Monitor AWS Cost Explorer during extended sessions
- Clean up resources immediately after training

---

## Training Data and Scenarios

**Built-in Failure Rates**:
- All functions have 15% random failure rate
- Step Functions includes retry and error handling
- Glue jobs simulate realistic processing times

**Forced Failure Types**:
- `databaseTimeout`: Complete function failure
- `partialFailure`: 70% success rate
- `complianceViolations`: Regulatory violation simulation
- `criticalFailure`: System-wide failure scenario
- `materialVariance`: Financial discrepancy simulation
- `specificProcess`: Targeted component failure

**Custom Metrics Generated**:
- Processing success rates
- Transaction volumes
- Compliance scores
- Error rates by category
- Processing durations

These shared resources ensure consistency across different training approaches while maximizing reusability and cost-effectiveness.
