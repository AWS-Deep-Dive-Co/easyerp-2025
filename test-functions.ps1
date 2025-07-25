#!/usr/bin/env powershell
# SOX Training - Manual Function Testing Script
# Use this script to test individual functions after deployment

param(
    [Parameter(Mandatory=$true)]
    [string]$EnvironmentName = "sox-training",
    
    [Parameter(Mandatory=$false)]
    [string]$Region = "us-east-1",
    
    [Parameter(Mandatory=$false)]
    [switch]$TestLambda,
    
    [Parameter(Mandatory=$false)]
    [switch]$TestStepFunctions,
    
    [Parameter(Mandatory=$false)]
    [switch]$TestAll
)

Write-Host "=== SOX Training Function Testing ===" -ForegroundColor Blue
Write-Host "Environment: $EnvironmentName" -ForegroundColor Green
Write-Host "Region: $Region" -ForegroundColor Green
Write-Host ""

# Create JSON payload file to avoid encoding issues
$payload = @'
{
  "test": true,
  "source": "manual-test",
  "timestamp": "2025-07-23T00:00:00Z"
}
'@
$payload | Out-File -FilePath "test-payload.json" -Encoding UTF8

if ($TestLambda -or $TestAll) {
    Write-Host "=== Testing Lambda Functions ===" -ForegroundColor Yellow
    
    Write-Host "Testing daily transaction processor..."
    try {
        aws lambda invoke `
            --function-name "$EnvironmentName-daily-transaction-processor" `
            --payload file://test-payload.json `
            --region $Region `
            lambda-response1.json
        
        if (Test-Path "lambda-response1.json") {
            $response = Get-Content "lambda-response1.json" | ConvertFrom-Json
            Write-Host "✅ Daily processor response: $($response.statusCode)" -ForegroundColor Green
        }
    }
    catch {
        Write-Host "❌ Daily processor failed: $($_.Exception.Message)" -ForegroundColor Red
    }
    
    Write-Host "Testing month-end processor..."
    try {
        aws lambda invoke `
            --function-name "$EnvironmentName-month-end-processor" `
            --payload file://test-payload.json `
            --region $Region `
            lambda-response2.json
            
        if (Test-Path "lambda-response2.json") {
            $response = Get-Content "lambda-response2.json" | ConvertFrom-Json
            Write-Host "✅ Month-end processor response: $($response.statusCode)" -ForegroundColor Green
        }
    }
    catch {
        Write-Host "❌ Month-end processor failed: $($_.Exception.Message)" -ForegroundColor Red
    }
    
    Write-Host ""
}

if ($TestStepFunctions -or $TestAll) {
    Write-Host "=== Testing Step Functions ===" -ForegroundColor Yellow
    
    try {
        # Get the state machine ARN
        $stateMachineArn = aws cloudformation describe-stacks `
            --stack-name "$EnvironmentName-stepfunctions-stack" `
            --query 'Stacks[0].Outputs[?OutputKey==`StateMachineArn`].OutputValue' `
            --output text `
            --region $Region
        
        if (-not $stateMachineArn -or $stateMachineArn -eq "None") {
            Write-Host "❌ Could not find Step Functions state machine ARN" -ForegroundColor Red
        } else {
            Write-Host "Found state machine: $stateMachineArn"
            
            # Create Step Functions input
            $stepFunctionsPayload = @'
{
  "source": "manual-test",
  "test_mode": true,
  "batch_size": 100
}
'@
            $stepFunctionsPayload | Out-File -FilePath "stepfunctions-test-payload.json" -Encoding UTF8
            
            $executionName = "manual-test-$(Get-Date -Format 'yyyyMMdd-HHmmss')"
            
            aws stepfunctions start-execution `
                --state-machine-arn $stateMachineArn `
                --name $executionName `
                --input file://stepfunctions-test-payload.json `
                --region $Region
                
            Write-Host "✅ Step Functions execution started: $executionName" -ForegroundColor Green
            Write-Host "Monitor execution in AWS Console > Step Functions" -ForegroundColor Cyan
        }
    }
    catch {
        Write-Host "❌ Step Functions test failed: $($_.Exception.Message)" -ForegroundColor Red
    }
    
    Write-Host ""
}

# Test EventBridge scheduled rules
if ($TestAll) {
    Write-Host "=== Testing EventBridge Rules ===" -ForegroundColor Yellow
    
    try {
        $rules = aws events list-rules --name-prefix $EnvironmentName --region $Region --output json | ConvertFrom-Json
        
        foreach ($rule in $rules.Rules) {
            $status = if ($rule.State -eq "ENABLED") { "✅ ENABLED" } else { "❌ DISABLED" }
            Write-Host "$status $($rule.Name)" -ForegroundColor $(if ($rule.State -eq "ENABLED") { "Green" } else { "Red" })
        }
    }
    catch {
        Write-Host "❌ Could not check EventBridge rules: $($_.Exception.Message)" -ForegroundColor Red
    }
    
    Write-Host ""
}

Write-Host "=== Test Results Summary ===" -ForegroundColor Blue

# Check for response files and show quick status
$testResults = @()

if (Test-Path "lambda-response1.json") {
    try {
        $resp1 = Get-Content "lambda-response1.json" | ConvertFrom-Json
        $testResults += "Daily Transaction Processor: $(if ($resp1.statusCode -eq 200) { 'PASS' } else { 'FAIL' })"
    } catch {
        $testResults += "Daily Transaction Processor: FAIL (invalid response)"
    }
}

if (Test-Path "lambda-response2.json") {
    try {
        $resp2 = Get-Content "lambda-response2.json" | ConvertFrom-Json
        $testResults += "Month-End Processor: $(if ($resp2.statusCode -eq 200) { 'PASS' } else { 'FAIL' })"
    } catch {
        $testResults += "Month-End Processor: FAIL (invalid response)"
    }
}

foreach ($result in $testResults) {
    if ($result.Contains("PASS")) {
        Write-Host "✅ $result" -ForegroundColor Green
    } else {
        Write-Host "❌ $result" -ForegroundColor Red
    }
}

Write-Host ""
Write-Host "🔍 Check CloudWatch Logs for detailed function output:" -ForegroundColor Cyan
Write-Host "   https://$Region.console.aws.amazon.com/cloudwatch/home?region=$Region#logsV2:log-groups"
Write-Host ""
Write-Host "📊 View CloudWatch Dashboards:" -ForegroundColor Cyan  
Write-Host "   https://$Region.console.aws.amazon.com/cloudwatch/home?region=$Region#dashboards:name=$EnvironmentName-sox-compliance-monitoring"

# Cleanup temporary files
Write-Host ""
Write-Host "Cleaning up temporary files..." -ForegroundColor Gray
if (Test-Path "test-payload.json") { Remove-Item "test-payload.json" }
if (Test-Path "stepfunctions-test-payload.json") { Remove-Item "stepfunctions-test-payload.json" }
if (Test-Path "lambda-response1.json") { Remove-Item "lambda-response1.json" }  
if (Test-Path "lambda-response2.json") { Remove-Item "lambda-response2.json" }

Write-Host "Testing complete!" -ForegroundColor Green
