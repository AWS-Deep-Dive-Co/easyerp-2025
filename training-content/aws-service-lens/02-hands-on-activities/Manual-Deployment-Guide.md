# Manual Deployment Guide for AWS Deep Dive Training

## Single Unified Deployment (Recommended)

Deploy the unified template `aws-deep-dive-training-unified.yaml` with these parameters:
- **EnvironmentName**: `aws-deep-dive`
- **S3BucketName**: `your-github-sync-bucket-name`

This single template deploys everything you need:
✅ **Lambda Functions**: 2 financial processes (every 5 & 15 minutes)
✅ **Step Functions**: Complex workflow (every 30 minutes)  
✅ **Glue Jobs**: ETL and compliance validation (every 10 & 20 minutes)
✅ **CloudWatch Dashboards**: Fixed SOX compliance and operational monitoring
✅ **CloudTrail**: Management event auditing
✅ **Optimized Scheduling**: All processes run frequently for training

## Alternative: Individual Stack Deployment

If you prefer to deploy components separately:

### Deploy Individual Stacks in Order:

1. **Lambda Functions Stack**
   - Template: `Cloudformation/functions/lambda.yaml`
   - Parameters: EnvironmentName=`aws-deep-dive`
   - No dependencies

2. **Step Functions Stack**  
   - Template: `Cloudformation/functions/step-functions.yaml`
   - Parameters: EnvironmentName=`aws-deep-dive`
   - No dependencies

3. **Glue Jobs Stack**
   - Template: `Cloudformation/functions/glue-jobs.yaml`
   - Parameters: 
     - EnvironmentName=`aws-deep-dive`
     - S3BucketName=`your-github-sync-bucket-name`
   - **Requires**: Glue scripts already synced to S3 at:
     - `s3://your-bucket/Cloudformation/functions/glue-scripts/financial-etl-script.py`
     - `s3://your-bucket/Cloudformation/functions/glue-scripts/compliance-validation-script.py`

4. **Monitoring Stack**
   - Template: `Cloudformation/functions/monitoring-dashboards.yaml`
   - Parameters: EnvironmentName=`aws-deep-dive`
   - No dependencies

## What You'll Get:

✅ **Lambda Functions**: 2 scheduled financial processes with realistic failures
✅ **Step Functions**: Complex workflow with error handling  
✅ **Glue Jobs**: ETL and compliance validation with financial scenarios
✅ **CloudWatch Dashboards**: Fixed SOX compliance and operational monitoring (no missing data!)
✅ **CloudTrail**: Management event auditing (API calls, logins, configuration changes)
✅ **Training-Optimized Scheduling**: 
   - Transaction Processing: Every 5 minutes
   - Month-End Processing: Every 15 minutes
   - Glue ETL Jobs: Every 10 minutes
   - Compliance Validation: Every 20 minutes
   - Step Functions Workflow: Every 30 minutes
✅ **Fixed Dashboard Issues**: 
   - Critical compliance violations now populate properly
   - Step Functions execution time removed for better visibility
   - Glue job metrics display correctly
✅ **Training Activities**: Complete hands-on exercises with frequent data population

## Post-Deployment Steps:

1. **Trigger Initial Executions** (to populate logs):

   ### Option A: AWS Web Console (Easiest for Training)

   **Lambda Functions:**
   1. Go to AWS Lambda Console: `https://console.aws.amazon.com/lambda/home`
   2. Find and click on these functions:
      - `aws-deep-dive-daily-transaction-processor`
      - `aws-deep-dive-month-end-processor`
   3. For each function:
      - Click the **"Test"** button (orange button)
      - If first time: "Configure test event" → "Create new event"
      - Event name: `training-test`
      - Replace JSON with:
        ```json
        {
          "test": true,
          "source": "web-console-test",
          "timestamp": "2025-07-23T00:00:00Z"
        }
        ```
      - Click **"Save"** then **"Test"**
      - View results in "Execution result" and "Log output" sections

   **Step Functions:**
   1. Go to Step Functions Console: `https://console.aws.amazon.com/states/home`
   2. Click on: `aws-deep-dive-financial-processing-workflow`
   3. Click **"Start execution"**
   4. Input (optional):
      ```json
      {
        "source": "web-console-test",
        "test_mode": true,
        "batch_size": 100
      }
      ```
   5. Click **"Start execution"** and watch the visual workflow

   **Glue Jobs:**
   1. Go to AWS Glue Console: `https://console.aws.amazon.com/glue/home#/jobs`
   2. Find and run these jobs:
      - `aws-deep-dive-financial-etl-job`
      - `aws-deep-dive-compliance-validation-job`
   3. For each job:
      - Click the job name
      - Click **"Run job"** button
      - Monitor progress in "History" tab
      - View logs by clicking on the run and selecting "Logs"
   4. **Expected behavior**: Jobs process sample financial data and create compliance reports

   ### Option C: Forced Failure Testing (Advanced Training)

   **For testing specific failure scenarios, you can force failures using custom input data:**

   **Lambda Functions - Forced Failures:**
   1. Go to AWS Lambda Console and select a function
   2. Click **"Test"** → "Configure test event"
   3. Use these JSON payloads to force specific failures:

   **Force Database Timeout (Daily Transaction Processor):**
   ```json
   {
     "source": "training-forced-failure",
     "forceFailure": {
       "databaseTimeout": true
     },
     "timestamp": "2025-07-27T00:00:00Z"
   }
   ```

   **Force Partial Failure (Daily Transaction Processor):**
   ```json
   {
     "source": "training-forced-failure",
     "forceFailure": {
       "partialFailure": true
     },
     "timestamp": "2025-07-27T00:00:00Z"
   }
   ```

   **Force Compliance Violations (Both Functions):**
   ```json
   {
     "source": "training-forced-failure",
     "forceFailure": {
       "complianceViolations": true
     },
     "timestamp": "2025-07-27T00:00:00Z"
   }
   ```

   **Force Critical Failure (Month-End Processor):**
   ```json
   {
     "source": "training-forced-failure",
     "forceFailure": {
       "criticalFailure": true
     },
     "timestamp": "2025-07-27T00:00:00Z"
   }
   ```

   **Force Material Variance (Month-End Processor):**
   ```json
   {
     "source": "training-forced-failure",
     "forceFailure": {
       "materialVariance": true
     },
     "timestamp": "2025-07-27T00:00:00Z"
   }
   ```

   **Force Specific Process Failure (Month-End Processor):**
   ```json
   {
     "source": "training-forced-failure",
     "forceFailure": {
       "specificProcess": "Account Reconciliation"
     },
     "timestamp": "2025-07-27T00:00:00Z"
   }
   ```
   *Available processes: "Account Reconciliation", "Journal Entry Validation", "Financial Statement Preparation", "Compliance Checks", "Variance Analysis"*

   **Combine Multiple Failures:**
   ```json
   {
     "source": "training-combined-failure",
     "forceFailure": {
       "complianceViolations": true,
       "materialVariance": true,
       "specificProcess": "Compliance Checks"
     },
     "timestamp": "2025-07-27T00:00:00Z"
   }
   ```

   **Step Functions - Forced Failures:**
   1. Go to Step Functions Console → `aws-deep-dive-financial-processing-workflow`
   2. Click **"Start execution"**
   3. Use these input examples:

   **Force Daily Transaction Failure:**
   ```json
   {
     "source": "step-functions-training",
     "forceFailure": {
       "databaseTimeout": true
     }
   }
   ```

   **Force Month-End Critical Failure:**
   ```json
   {
     "source": "step-functions-training",
     "forceFailure": {
       "criticalFailure": true,
       "complianceViolations": true
     }
   }
   ```

   **💡 Training Benefits of Forced Failures:**
   - **Predictable Testing**: Know exactly which failure will occur
   - **Dashboard Population**: Critical violations appear immediately in dashboards
   - **Compliance Training**: Demonstrate specific SOX violation scenarios
   - **Error Handling**: Show how Step Functions handles different failure types
   - **Log Analysis**: Generate specific error patterns for troubleshooting practice

   ### Option B: AWS CLI
   
   **For Linux/Mac:**
   ```bash
   echo '{"test":true,"source":"manual-test"}' > payload.json
   aws lambda invoke --function-name aws-deep-dive-daily-transaction-processor --payload file://payload.json response.json
   aws lambda invoke --function-name aws-deep-dive-month-end-processor --payload file://payload.json response2.json
   
   # Start Glue jobs
   aws glue start-job-run --job-name aws-deep-dive-financial-etl-job
   aws glue start-job-run --job-name aws-deep-dive-compliance-validation-job
   
   rm payload.json
   ```

   **CLI Forced Failure Examples:**
   ```bash
   # Force database timeout
   echo '{"source":"cli-test","forceFailure":{"databaseTimeout":true}}' > failure.json
   aws lambda invoke --function-name aws-deep-dive-daily-transaction-processor --payload file://failure.json response.json
   
   # Force material variance
   echo '{"source":"cli-test","forceFailure":{"materialVariance":true}}' > failure2.json
   aws lambda invoke --function-name aws-deep-dive-month-end-processor --payload file://failure2.json response2.json
   
   # Start Step Functions with forced failure
   aws stepfunctions start-execution \
     --state-machine-arn "arn:aws:states:REGION:ACCOUNT:stateMachine:aws-deep-dive-financial-processing-workflow" \
     --input '{"source":"cli-test","forceFailure":{"criticalFailure":true}}'
   
   rm failure.json failure2.json
   ```
   
   **For Windows PowerShell:**
   ```powershell
   @'
   {
     "test": true,
     "source": "manual-test"
   }
   '@ | Out-File -FilePath "payload.json" -Encoding UTF8
   
   aws lambda invoke --function-name aws-deep-dive-daily-transaction-processor --payload file://payload.json response.json
   aws lambda invoke --function-name aws-deep-dive-month-end-processor --payload file://payload.json response2.json
   
   # Start Glue jobs
   aws glue start-job-run --job-name aws-deep-dive-financial-etl-job
   aws glue start-job-run --job-name aws-deep-dive-compliance-validation-job
   
   Remove-Item "payload.json"
   ```

   **PowerShell Forced Failure Examples:**
   ```powershell
   # Force compliance violations
   @'
   {
     "source": "powershell-test",
     "forceFailure": {
       "complianceViolations": true
     }
   }
   '@ | Out-File -FilePath "failure.json" -Encoding UTF8
   
   aws lambda invoke --function-name aws-deep-dive-daily-transaction-processor --payload file://failure.json response.json
   
   # Force specific process failure
   @'
   {
     "source": "powershell-test",
     "forceFailure": {
       "specificProcess": "Account Reconciliation"
     }
   }
   '@ | Out-File -FilePath "failure2.json" -Encoding UTF8
   
   aws lambda invoke --function-name aws-deep-dive-month-end-processor --payload file://failure2.json response2.json
   
   Remove-Item "failure.json", "failure2.json"
   ```

2. **Access Your Dashboards**:
   - SOX Compliance: CloudWatch > Dashboards > aws-deep-dive-sox-compliance-monitoring  
   - Operational: CloudWatch > Dashboards > aws-deep-dive-operational-monitoring

3. **Monitor Your Test Results**:
   - **CloudWatch Logs**: Check function logs at CloudWatch > Log groups > `/aws/lambda/aws-deep-dive-*`
   - **CloudWatch Metrics**: Go to CloudWatch > Metrics > Custom Namespaces > `FinancialProcessing`
   - **Step Functions History**: View execution details in Step Functions console
   - **Glue Job Runs**: Check job status and logs at AWS Glue > Jobs > [job-name] > History tab
   - **CloudTrail Events**: Your console actions appear as API calls in CloudTrail

4. **Enable Failure Simulation** (during training):
   ```bash
   aws events enable-rule --name aws-deep-dive-failure-simulator
   ```

## Training Failure Scenarios

Use these specific scenarios to demonstrate different SOX compliance and operational issues:

### Scenario 1: Database Connectivity Issues
**Purpose**: Demonstrate critical system failures and their impact on compliance
```json
{
  "source": "training-scenario-1",
  "forceFailure": {
    "databaseTimeout": true
  }
}
```
**Expected Result**: 
- Lambda function fails completely
- Critical compliance metrics drop below 85%
- Material variance recorded
- Dashboard shows red alerts

### Scenario 2: Partial Processing Failures  
**Purpose**: Show how systems handle degraded performance
```json
{
  "source": "training-scenario-2", 
  "forceFailure": {
    "partialFailure": true
  }
}
```
**Expected Result**:
- 70% of transactions process successfully
- Processing success rate drops to ~70%
- Compliance score near threshold (82-87%)

### Scenario 3: SOX Compliance Violations
**Purpose**: Trigger segregation of duties and access control violations
```json
{
  "source": "training-scenario-3",
  "forceFailure": {
    "complianceViolations": true
  }
}
```
**Expected Result**:
- SOD violations appear in dashboard
- Privileged access violations recorded
- Access control violations logged
- Compliance score decreases

### Scenario 4: Month-End Close Failure
**Purpose**: Demonstrate critical financial reporting failures
```json
{
  "source": "training-scenario-4",
  "forceFailure": {
    "criticalFailure": true,
    "materialVariance": true
  }
}
```
**Expected Result**:
- Month-end process fails completely
- Material variance of $50,000-$200,000
- Step Functions workflow terminates in failure state
- Critical compliance alerts

### Scenario 5: Specific Process Testing
**Purpose**: Test individual financial processes
```json
{
  "source": "training-scenario-5",
  "forceFailure": {
    "specificProcess": "Compliance Checks"
  }
}
```
**Expected Result**:
- Only the specified process fails
- Other processes continue normally
- Targeted failure analysis possible

### Scenario 6: Multi-Process Cascade Failure
**Purpose**: Show how failures cascade through systems
**Step 1** - Start Step Functions with daily transaction failure:
```json
{
  "source": "training-cascade-1",
  "forceFailure": {
    "databaseTimeout": true
  }
}
```
**Step 2** - Observe that month-end process never executes due to failure handling

**Training Discussion Points**:
- How do system failures propagate?
- What controls prevent cascading failures?
- How do we maintain audit trails during failures?

   💡 **Training Tips**:
   - Functions have built-in 15% failure rate for realistic scenarios
   - Run functions multiple times to see different failure patterns
   - Each execution populates different metrics in the dashboards
   - **OPTIMIZED FOR TRAINING**: All processes run every 5-30 minutes, so you'll see fresh data quickly!
   - Critical compliance violations will appear in the dashboard as functions run
   - Web console method is perfect for hands-on training activities

## Training URLs You'll Need:

- **CloudWatch Dashboards**: `https://console.aws.amazon.com/cloudwatch/home#dashboards:`
- **CloudWatch Logs**: `https://console.aws.amazon.com/cloudwatch/home#logsV2:logs-insights`
- **CloudTrail Events**: `https://console.aws.amazon.com/cloudtrail/home#/events`
- **Step Functions**: `https://console.aws.amazon.com/states/home#/statemachines`
- **Glue Jobs**: `https://console.aws.amazon.com/glue/home#/jobs`

## Manual Cleanup After Training:

Delete stacks in this order:
1. `aws-deep-dive-monitoring-stack`
2. `aws-deep-dive-stepfunctions-stack`
3. `aws-deep-dive-glue-stack`
4. `aws-deep-dive-lambda-stack`

That's it! The manual deployment is actually simpler since you avoid the S3 upload complexity.
