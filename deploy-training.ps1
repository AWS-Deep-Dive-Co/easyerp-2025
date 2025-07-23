# SOX Auditor Training - Deployment Script
# Run this script to deploy the complete training environment

param(
    [Parameter(Mandatory=$false)]
    [string]$EnvironmentName = "sox-training",
    
    [Parameter(Mandatory=$false)]
    [string]$Region = "us-east-1",
    
    [Parameter(Mandatory=$false)]
    [switch]$SkipGlue = $false,
    
    [Parameter(Mandatory=$false)]
    [switch]$EnableFailureSimulation = $false
)

Write-Host "=== SOX Auditor Training Environment Deployment ===" -ForegroundColor Green
Write-Host "Environment: $EnvironmentName" -ForegroundColor Yellow
Write-Host "Region: $Region" -ForegroundColor Yellow
Write-Host ""

# Check if AWS CLI is installed and configured
try {
    $awsVersion = aws --version
    Write-Host "AWS CLI Version: $awsVersion" -ForegroundColor Green
} catch {
    Write-Error "AWS CLI not found. Please install AWS CLI first."
    exit 1
}

# Check AWS credentials
try {
    $identity = aws sts get-caller-identity --output text --query 'Account'
    Write-Host "AWS Account: $identity" -ForegroundColor Green
} catch {
    Write-Error "AWS credentials not configured. Please run 'aws configure' first."
    exit 1
}

Write-Host ""
Write-Host "=== Step 1: Uploading Glue Scripts to S3 ===" -ForegroundColor Blue

if (-not $SkipGlue) {
    # Create S3 bucket for Glue scripts
    $bucketName = "$EnvironmentName-glue-scripts-$identity"
    
    Write-Host "Creating S3 bucket: $bucketName"
    aws s3 mb s3://$bucketName --region $Region
    
    # Upload Glue scripts
    Write-Host "Uploading Glue ETL script..."
    aws s3 cp "./Cloudformation/functions/glue-scripts/financial-etl-script.py" "s3://$bucketName/financial-etl-script.py"
    
    Write-Host "Uploading Compliance validation script..."
    aws s3 cp "./Cloudformation/functions/glue-scripts/compliance-validation-script.py" "s3://$bucketName/compliance-validation-script.py"
    
    Write-Host "Glue scripts uploaded successfully!" -ForegroundColor Green
}

Write-Host ""
Write-Host "=== Step 2: Deploying CloudFormation Stacks ===" -ForegroundColor Blue

# Deploy Lambda stack
Write-Host "Deploying Lambda functions..."
aws cloudformation deploy `
    --template-file "./Cloudformation/functions/lambda.yaml" `
    --stack-name "$EnvironmentName-lambda-stack" `
    --parameter-overrides EnvironmentName=$EnvironmentName `
    --capabilities CAPABILITY_NAMED_IAM `
    --region $Region

if ($LASTEXITCODE -ne 0) {
    Write-Error "Failed to deploy Lambda stack"
    exit 1
}

# Deploy Step Functions stack
Write-Host "Deploying Step Functions workflow..."
aws cloudformation deploy `
    --template-file "./Cloudformation/functions/step-functions.yaml" `
    --stack-name "$EnvironmentName-stepfunctions-stack" `
    --parameter-overrides EnvironmentName=$EnvironmentName `
    --capabilities CAPABILITY_NAMED_IAM `
    --region $Region

if ($LASTEXITCODE -ne 0) {
    Write-Error "Failed to deploy Step Functions stack"
    exit 1
}

# Deploy Glue stack (if not skipped)
if (-not $SkipGlue) {
    Write-Host "Deploying Glue jobs..."
    aws cloudformation deploy `
        --template-file "./Cloudformation/functions/glue-jobs.yaml" `
        --stack-name "$EnvironmentName-glue-stack" `
        --parameter-overrides EnvironmentName=$EnvironmentName `
        --capabilities CAPABILITY_NAMED_IAM `
        --region $Region

    if ($LASTEXITCODE -ne 0) {
        Write-Error "Failed to deploy Glue stack"
        exit 1
    }
}

# Deploy Monitoring stack
Write-Host "Deploying monitoring dashboards..."
aws cloudformation deploy `
    --template-file "./Cloudformation/functions/monitoring-dashboards.yaml" `
    --stack-name "$EnvironmentName-monitoring-stack" `
    --parameter-overrides EnvironmentName=$EnvironmentName `
    --capabilities CAPABILITY_NAMED_IAM `
    --region $Region

if ($LASTEXITCODE -ne 0) {
    Write-Error "Failed to deploy Monitoring stack"
    exit 1
}

Write-Host ""
Write-Host "=== Step 3: Initial Test Runs ===" -ForegroundColor Blue

# Trigger initial Lambda function runs to populate logs
Write-Host "Running initial test of daily transaction processor..."
aws lambda invoke `
    --function-name "$EnvironmentName-daily-transaction-processor" `
    --payload '{"test": true}' `
    --region $Region `
    response.json

Write-Host "Running initial test of month-end processor..."
aws lambda invoke `
    --function-name "$EnvironmentName-month-end-processor" `
    --payload '{"test": true}' `
    --region $Region `
    response2.json

# Start Step Functions execution
Write-Host "Starting Step Functions workflow..."
$stateMachineArn = aws cloudformation describe-stacks `
    --stack-name "$EnvironmentName-stepfunctions-stack" `
    --query 'Stacks[0].Outputs[?OutputKey==`StateMachineArn`].OutputValue' `
    --output text `
    --region $Region

aws stepfunctions start-execution `
    --state-machine-arn $stateMachineArn `
    --name "initial-test-$(Get-Date -Format 'yyyyMMdd-HHmmss')" `
    --input '{"source": "deployment-test"}' `
    --region $Region

Write-Host ""
Write-Host "=== Step 4: Getting Access URLs ===" -ForegroundColor Blue

# Get dashboard URLs
$dashboardUrl = "https://$Region.console.aws.amazon.com/cloudwatch/home?region=$Region#dashboards:name=$EnvironmentName-sox-compliance-monitoring"
$logsUrl = "https://$Region.console.aws.amazon.com/cloudwatch/home?region=$Region#logsV2:logs-insights"
$cloudtrailUrl = "https://$Region.console.aws.amazon.com/cloudtrail/home?region=$Region#/events"

Write-Host ""
Write-Host "=== DEPLOYMENT COMPLETE! ===" -ForegroundColor Green
Write-Host ""
Write-Host "🎯 TRAINING ENVIRONMENT READY" -ForegroundColor Yellow
Write-Host ""
Write-Host "📊 SOX Compliance Dashboard:" -ForegroundColor Cyan
Write-Host "   $dashboardUrl" -ForegroundColor White
Write-Host ""
Write-Host "📋 CloudWatch Logs:" -ForegroundColor Cyan  
Write-Host "   $logsUrl" -ForegroundColor White
Write-Host ""
Write-Host "🔍 CloudTrail Events:" -ForegroundColor Cyan
Write-Host "   $cloudtrailUrl" -ForegroundColor White
Write-Host ""

if (-not $SkipGlue) {
    $glueUrl = "https://$Region.console.aws.amazon.com/glue/home?region=$Region#etl:tab=jobs"
    Write-Host "🔧 Glue Jobs Console:" -ForegroundColor Cyan
    Write-Host "   $glueUrl" -ForegroundColor White
    Write-Host ""
}

$stepFunctionsUrl = "https://$Region.console.aws.amazon.com/states/home?region=$Region#/statemachines"
Write-Host "🔄 Step Functions Console:" -ForegroundColor Cyan
Write-Host "   $stepFunctionsUrl" -ForegroundColor White
Write-Host ""

Write-Host "⏰ SCHEDULED PROCESSES:" -ForegroundColor Yellow
Write-Host "   • Daily Transaction Processing: 2 AM UTC daily"
Write-Host "   • Month-End Close: Last day of month, 1 AM UTC"
Write-Host "   • Financial ETL: 3 AM UTC daily (if Glue deployed)"
Write-Host "   • Compliance Validation: Mondays 6 AM UTC (if Glue deployed)"
Write-Host "   • Step Functions Workflow: 8 AM and 8 PM UTC"
Write-Host ""

Write-Host "🎓 TRAINING TIPS:" -ForegroundColor Yellow
Write-Host "   1. Wait 5-10 minutes for initial metrics to appear"
Write-Host "   2. Check CloudWatch Logs for sample error messages"  
Write-Host "   3. Review CloudTrail for deployment API calls"
Write-Host "   4. Use the Training Guide for hands-on activities"
Write-Host ""

if ($EnableFailureSimulation) {
    Write-Host "⚠️  ENABLING FAILURE SIMULATION..." -ForegroundColor Red
    
    # Enable the failure simulator EventBridge rule
    aws events enable-rule --name "$EnvironmentName-failure-simulator" --region $Region
    
    Write-Host "   Failure simulation enabled - processes will randomly fail for training"
    Write-Host "   To disable: aws events disable-rule --name $EnvironmentName-failure-simulator --region $Region"
    Write-Host ""
}

Write-Host "🗑️  TO CLEAN UP AFTER TRAINING:" -ForegroundColor Red
Write-Host "   Run: ./cleanup-training.ps1 -EnvironmentName $EnvironmentName -Region $Region"
Write-Host ""

# Clean up temporary files
Remove-Item -Path "response.json" -ErrorAction SilentlyContinue
Remove-Item -Path "response2.json" -ErrorAction SilentlyContinue

Write-Host "Deployment completed successfully! 🎉" -ForegroundColor Green
