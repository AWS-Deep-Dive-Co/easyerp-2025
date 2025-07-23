# Manual Deployment Guide for SOX Auditor Training

## Option 1: Using Master Template (Recommended)

Deploy `sox-training-master.yaml` with these parameters:
- **EnvironmentName**: `sox-training`
- **S3BucketName**: `your-github-sync-bucket-name`
- **DeployLambdaExamples**: `Yes`
- **DeployGlueExamples**: `Yes` (now works with your S3 bucket!)
- **DeployStepFunctionsExamples**: `Yes`
- **DeployMonitoringDashboards**: `Yes`

## Option 2: Individual Stack Deployment

### Deploy Individual Stacks in Order:

1. **Lambda Functions Stack**
   - Template: `Cloudformation/functions/lambda.yaml`
   - Parameters: EnvironmentName=`sox-training`
   - No dependencies

2. **Step Functions Stack**  
   - Template: `Cloudformation/functions/step-functions.yaml`
   - Parameters: EnvironmentName=`sox-training`
   - No dependencies

3. **Glue Jobs Stack**
   - Template: `Cloudformation/functions/glue-jobs.yaml`
   - Parameters: 
     - EnvironmentName=`sox-training`
     - S3BucketName=`your-github-sync-bucket-name`
   - **Requires**: Glue scripts already synced to S3 at:
     - `s3://your-bucket/Cloudformation/functions/glue-scripts/financial-etl-script.py`
     - `s3://your-bucket/Cloudformation/functions/glue-scripts/compliance-validation-script.py`

4. **Monitoring Stack**
   - Template: `Cloudformation/functions/monitoring-dashboards.yaml`
   - Parameters: EnvironmentName=`sox-training`
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
   ```bash
   aws lambda invoke --function-name sox-training-daily-transaction-processor --payload '{"test":true}' response.json
   aws lambda invoke --function-name sox-training-month-end-processor --payload '{"test":true}' response2.json
   ```

2. **Access Your Dashboards**:
   - SOX Compliance: CloudWatch > Dashboards > sox-training-sox-compliance-monitoring  
   - Operational: CloudWatch > Dashboards > sox-training-operational-monitoring

3. **Enable Failure Simulation** (during training):
   ```bash
   aws events enable-rule --name sox-training-failure-simulator
   ```

## Training URLs You'll Need:

- **CloudWatch Dashboards**: `https://console.aws.amazon.com/cloudwatch/home#dashboards:`
- **CloudWatch Logs**: `https://console.aws.amazon.com/cloudwatch/home#logsV2:logs-insights`
- **CloudTrail Events**: `https://console.aws.amazon.com/cloudtrail/home#/events`
- **Step Functions**: `https://console.aws.amazon.com/states/home#/statemachines`

## Manual Cleanup After Training:

Delete stacks in this order:
1. `sox-training-monitoring-stack`
2. `sox-training-stepfunctions-stack`  
3. `sox-training-lambda-stack`

That's it! The manual deployment is actually simpler since you avoid the S3 upload complexity.
