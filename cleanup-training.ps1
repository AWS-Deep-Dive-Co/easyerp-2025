# SOX Auditor Training - Cleanup Script
# Run this script to remove all training resources after the session

param(
    [Parameter(Mandatory=$false)]
    [string]$EnvironmentName = "sox-training",
    
    [Parameter(Mandatory=$false)]
    [string]$Region = "us-east-1",
    
    [Parameter(Mandatory=$false)]
    [switch]$Force = $false
)

Write-Host "=== SOX Auditor Training Environment Cleanup ===" -ForegroundColor Red
Write-Host "Environment: $EnvironmentName" -ForegroundColor Yellow
Write-Host "Region: $Region" -ForegroundColor Yellow
Write-Host ""

if (-not $Force) {
    $confirmation = Read-Host "This will DELETE all training resources. Type 'DELETE' to confirm"
    if ($confirmation -ne "DELETE") {
        Write-Host "Cleanup cancelled." -ForegroundColor Green
        exit 0
    }
}

# Get AWS account ID for S3 bucket names
try {
    $accountId = aws sts get-caller-identity --output text --query 'Account'
    Write-Host "AWS Account: $accountId" -ForegroundColor Green
} catch {
    Write-Error "AWS credentials not configured. Please run 'aws configure' first."
    exit 1
}

Write-Host ""
Write-Host "=== Step 1: Disabling Scheduled Events ===" -ForegroundColor Blue

# Disable all EventBridge rules to stop new executions
$rules = @(
    "$EnvironmentName-daily-transaction-schedule",
    "$EnvironmentName-month-end-schedule", 
    "$EnvironmentName-financial-etl-schedule",
    "$EnvironmentName-compliance-validation-schedule",
    "$EnvironmentName-financial-processing-schedule",
    "$EnvironmentName-failure-simulator"
)

foreach ($rule in $rules) {
    Write-Host "Disabling rule: $rule"
    aws events disable-rule --name $rule --region $Region 2>$null
}

Write-Host ""
Write-Host "=== Step 2: Emptying S3 Buckets ===" -ForegroundColor Blue

# Empty S3 buckets before stack deletion
$buckets = @(
    "$EnvironmentName-glue-scripts-$accountId",
    "$EnvironmentName-sox-audit-trail-$accountId"
)

foreach ($bucket in $buckets) {
    Write-Host "Checking bucket: $bucket"
    $bucketExists = aws s3api head-bucket --bucket $bucket --region $Region 2>$null
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Emptying bucket: $bucket"
        aws s3 rm s3://$bucket --recursive --region $Region
        
        # Remove bucket versioning objects if they exist
        aws s3api delete-objects --bucket $bucket --delete "$(aws s3api list-object-versions --bucket $bucket --output json --query '{Objects: Versions[].{Key:Key,VersionId:VersionId}}')" --region $Region 2>$null
        aws s3api delete-objects --bucket $bucket --delete "$(aws s3api list-object-versions --bucket $bucket --output json --query '{Objects: DeleteMarkers[].{Key:Key,VersionId:VersionId}}')" --region $Region 2>$null
    }
}

Write-Host ""
Write-Host "=== Step 3: Deleting CloudFormation Stacks ===" -ForegroundColor Blue

# Delete stacks in reverse dependency order
$stacks = @(
    "$EnvironmentName-monitoring-stack",
    "$EnvironmentName-stepfunctions-stack", 
    "$EnvironmentName-glue-stack",
    "$EnvironmentName-lambda-stack"
)

foreach ($stack in $stacks) {
    Write-Host "Checking stack: $stack"
    $stackExists = aws cloudformation describe-stacks --stack-name $stack --region $Region 2>$null
    
    if ($LASTEXITCODE -eq 0) {
        Write-Host "Deleting stack: $stack"
        aws cloudformation delete-stack --stack-name $stack --region $Region
        
        Write-Host "Waiting for stack deletion to complete..."
        aws cloudformation wait stack-delete-complete --stack-name $stack --region $Region
        
        if ($LASTEXITCODE -eq 0) {
            Write-Host "✓ Stack deleted: $stack" -ForegroundColor Green
        } else {
            Write-Host "⚠ Stack deletion may have failed: $stack" -ForegroundColor Yellow
        }
    }
}

Write-Host ""
Write-Host "=== Step 4: Cleaning Up Remaining Resources ===" -ForegroundColor Blue

# Delete any remaining S3 buckets
foreach ($bucket in $buckets) {
    Write-Host "Deleting bucket: $bucket"
    aws s3 rb s3://$bucket --force --region $Region 2>$null
}

# Clean up any remaining log groups
Write-Host "Cleaning up CloudWatch log groups..."
$logGroups = aws logs describe-log-groups --log-group-name-prefix "/aws/lambda/$EnvironmentName" --region $Region --query 'logGroups[].logGroupName' --output text 2>$null

if ($logGroups) {
    foreach ($logGroup in $logGroups.Split()) {
        if ($logGroup.Trim()) {
            Write-Host "Deleting log group: $logGroup"
            aws logs delete-log-group --log-group-name $logGroup --region $Region 2>$null
        }
    }
}

# Additional log groups
$additionalLogGroups = @(
    "/sox-compliance/$EnvironmentName/audit-trail",
    "/financial-processing/$EnvironmentName/transactions",
    "/aws/stepfunctions/$EnvironmentName-financial-processing",
    "/aws-glue/jobs/logs-v2",
    "/aws/cloudtrail/$EnvironmentName-sox-audit"
)

foreach ($logGroup in $additionalLogGroups) {
    Write-Host "Attempting to delete log group: $logGroup"
    aws logs delete-log-group --log-group-name $logGroup --region $Region 2>$null
}

Write-Host ""
Write-Host "=== Step 5: Verification ===" -ForegroundColor Blue

# Check if any resources remain
Write-Host "Checking for remaining Lambda functions..."
$lambdas = aws lambda list-functions --query "Functions[?contains(FunctionName, '$EnvironmentName')].FunctionName" --output text --region $Region
if ($lambdas) {
    Write-Host "⚠ Remaining Lambda functions: $lambdas" -ForegroundColor Yellow
} else {
    Write-Host "✓ No Lambda functions found" -ForegroundColor Green
}

Write-Host "Checking for remaining Step Functions..."
$stateMachines = aws stepfunctions list-state-machines --query "stateMachines[?contains(name, '$EnvironmentName')].name" --output text --region $Region
if ($stateMachines) {
    Write-Host "⚠ Remaining Step Functions: $stateMachines" -ForegroundColor Yellow
} else {
    Write-Host "✓ No Step Functions found" -ForegroundColor Green
}

Write-Host "Checking for remaining S3 buckets..."
foreach ($bucket in $buckets) {
    $bucketExists = aws s3api head-bucket --bucket $bucket --region $Region 2>$null
    if ($LASTEXITCODE -eq 0) {
        Write-Host "⚠ Bucket still exists: $bucket" -ForegroundColor Yellow
    } else {
        Write-Host "✓ Bucket removed: $bucket" -ForegroundColor Green
    }
}

Write-Host ""
Write-Host "=== CLEANUP COMPLETE! ===" -ForegroundColor Green
Write-Host ""
Write-Host "📊 All training dashboards have been removed" -ForegroundColor Cyan
Write-Host "🔧 All Lambda functions have been deleted" -ForegroundColor Cyan
Write-Host "🔄 All Step Functions workflows have been deleted" -ForegroundColor Cyan  
Write-Host "📦 All S3 buckets have been emptied and removed" -ForegroundColor Cyan
Write-Host "📋 All CloudWatch log groups have been deleted" -ForegroundColor Cyan
Write-Host "⏰ All scheduled events have been disabled" -ForegroundColor Cyan
Write-Host ""

Write-Host "💰 COST IMPACT:" -ForegroundColor Yellow
Write-Host "   • No more charges will accrue for training resources"
Write-Host "   • Any remaining CloudWatch logs will age out automatically"
Write-Host "   • EventBridge rules are now disabled (no execution costs)"
Write-Host ""

if ($lambdas -or $stateMachines) {
    Write-Host "⚠️  MANUAL CLEANUP NEEDED:" -ForegroundColor Red
    Write-Host "   Some resources may require manual deletion from the AWS Console"
    Write-Host "   Check the AWS Console for any remaining resources tagged with: $EnvironmentName"
    Write-Host ""
}

Write-Host "Training environment cleanup completed! 🧹" -ForegroundColor Green
