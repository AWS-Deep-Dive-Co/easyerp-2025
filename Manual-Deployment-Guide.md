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
