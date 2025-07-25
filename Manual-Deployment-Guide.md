# Manual Deployment Guide for SOX Auditor Training

## Option 1: Using Master Template (Recommended)

Deploy `sox-training-master.yaml` with these parameters:
- **EnvironmentName**: `aws-deep-dive`
- **S3BucketName**: `your-github-sync-bucket-name`
- **DeployLambdaExamples**: `Yes`
- **DeployGlueExamples**: `Yes` (now works with your S3 bucket!)
- **DeployStepFunctionsExamples**: `Yes`
- **DeployMonitoringDashboards**: `Yes`

## Option 2: Individual Stack Deployment

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
✅ **CloudWatch Dashboards**: SOX compliance and operational monitoring
✅ **CloudTrail**: Management event auditing (API calls, logins, configuration changes)
✅ **Scheduled Events**: All processes run on realistic schedules
✅ **Training Activities**: Complete hands-on exercises focused on management event investigation

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

   ### Option B: AWS CLI
   
   **For Linux/Mac:**
   ```bash
   echo '{"test":true,"source":"manual-test"}' > payload.json
   aws lambda invoke --function-name aws-deep-dive-daily-transaction-processor --payload file://payload.json response.json
   aws lambda invoke --function-name aws-deep-dive-month-end-processor --payload file://payload.json response2.json
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
   
   Remove-Item "payload.json"
   ```

2. **Access Your Dashboards**:
   - SOX Compliance: CloudWatch > Dashboards > aws-deep-dive-sox-compliance-monitoring  
   - Operational: CloudWatch > Dashboards > aws-deep-dive-operational-monitoring

3. **Monitor Your Test Results**:
   - **CloudWatch Logs**: Check function logs at CloudWatch > Log groups > `/aws/lambda/aws-deep-dive-*`
   - **CloudWatch Metrics**: Go to CloudWatch > Metrics > Custom Namespaces > `FinancialProcessing`
   - **Step Functions History**: View execution details in Step Functions console
   - **CloudTrail Events**: Your console actions appear as API calls in CloudTrail

4. **Enable Failure Simulation** (during training):
   ```bash
   aws events enable-rule --name aws-deep-dive-failure-simulator
   ```

   💡 **Training Tips**:
   - Functions have built-in 15% failure rate for realistic scenarios
   - Run functions multiple times to see different failure patterns
   - Each execution populates different metrics in the dashboards
   - Web console method is perfect for hands-on training activities

## Training URLs You'll Need:

- **CloudWatch Dashboards**: `https://console.aws.amazon.com/cloudwatch/home#dashboards:`
- **CloudWatch Logs**: `https://console.aws.amazon.com/cloudwatch/home#logsV2:logs-insights`
- **CloudTrail Events**: `https://console.aws.amazon.com/cloudtrail/home#/events`
- **Step Functions**: `https://console.aws.amazon.com/states/home#/statemachines`

## Manual Cleanup After Training:

Delete stacks in this order:
1. `aws-deep-dive-monitoring-stack`
2. `aws-deep-dive-stepfunctions-stack`  
3. `aws-deep-dive-lambda-stack`

That's it! The manual deployment is actually simpler since you avoid the S3 upload complexity.
