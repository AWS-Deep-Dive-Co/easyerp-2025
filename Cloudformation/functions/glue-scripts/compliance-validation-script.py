"""
Compliance Data Validation Script for SOX Auditor Training
This script simulates data validation checks required for SOX compliance
"""

import sys
import random
import time
from datetime import datetime, timedelta
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
import boto3

# Initialize Glue context
args = getResolvedOptions(sys.argv, ['JOB_NAME', 'environment'])
sc = SparkContext()
glueContext = GlueContext(sc)
spark = glueContext.spark_session
job = Job(glueContext)
job.init(args['JOB_NAME'], args)

# Initialize CloudWatch client for custom metrics
cloudwatch = boto3.client('cloudwatch')

def log_message(level, message):
    """Enhanced logging with timestamps"""
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print(f"[{timestamp}] [{level}] {message}")

def send_custom_metric(metric_name, value, unit='Count', dimensions=None):
    """Send custom metrics to CloudWatch"""
    try:
        metric_data = {
            'MetricName': metric_name,
            'Value': value,
            'Unit': unit,
            'Timestamp': datetime.utcnow()
        }
        
        if dimensions:
            metric_data['Dimensions'] = dimensions
            
        cloudwatch.put_metric_data(
            Namespace='ComplianceValidation/SOX',
            MetricData=[metric_data]
        )
    except Exception as e:
        log_message('ERROR', f'Failed to send metric {metric_name}: {str(e)}')

def validate_data_completeness():
    """Validate that all required data is present"""
    log_message('INFO', 'Starting data completeness validation...')
    
    # Simulate checking various data completeness requirements
    validations = [
        ('General Ledger Transactions', 'All financial transactions recorded'),
        ('Journal Entry Documentation', 'Supporting documentation attached'),
        ('Account Reconciliations', 'All accounts reconciled monthly'),
        ('Approval Workflows', 'Required approvals documented'),
        ('Period-end Adjustments', 'All adjustments properly authorized')
    ]
    
    completeness_issues = []
    total_checks = len(validations)
    passed_checks = 0
    
    for check_name, description in validations:
        log_message('INFO', f'Validating: {check_name}')
        
        # Simulate completeness issues
        failure_chance = random.random()
        
        if failure_chance < 0.20:  # 20% chance of completeness issue
            issue_count = random.randint(5, 50)
            completeness_issues.append({
                'check': check_name,
                'description': description,
                'missing_count': issue_count
            })
            
            log_message('WARNING', f'COMPLETENESS ISSUE: {check_name}')
            log_message('WARNING', f'Missing/incomplete items: {issue_count}')
            
            send_custom_metric('CompletenessIssues', issue_count, dimensions=[
                {'Name': 'ValidationCheck', 'Value': check_name}
            ])
        else:
            passed_checks += 1
            log_message('INFO', f'✓ PASSED: {check_name}')
        
        time.sleep(0.5)
    
    completion_rate = (passed_checks / total_checks) * 100
    send_custom_metric('CompletenessRate', completion_rate, 'Percent')
    
    log_message('INFO', f'Data completeness validation finished: {passed_checks}/{total_checks} checks passed')
    return completeness_issues

def validate_data_accuracy():
    """Validate data accuracy and integrity"""
    log_message('INFO', 'Starting data accuracy validation...')
    
    accuracy_checks = [
        ('Trial Balance Reconciliation', 'Debits equal credits'),
        ('Inter-company Eliminations', 'Eliminating entries balanced'),
        ('Currency Translation', 'Exchange rates applied correctly'),
        ('Depreciation Calculations', 'Asset depreciation accurate'),
        ('Accrual Calculations', 'Expense accruals properly calculated'),
        ('Revenue Recognition', 'Revenue recognized per policy')
    ]
    
    accuracy_issues = []
    total_amount_tested = random.randint(10000000, 50000000)  # $10M - $50M
    variance_total = 0
    
    for check_name, description in accuracy_checks:
        log_message('INFO', f'Testing accuracy: {check_name}')
        
        # Simulate accuracy issues
        failure_chance = random.random()
        
        if failure_chance < 0.15:  # 15% chance of accuracy issue
            variance_amount = random.randint(1000, 25000)
            variance_total += variance_amount
            
            accuracy_issues.append({
                'check': check_name,
                'description': description,
                'variance': variance_amount
            })
            
            log_message('ERROR', f'ACCURACY ISSUE: {check_name}')
            log_message('ERROR', f'Variance detected: ${variance_amount:,}')
            log_message('ERROR', f'Issue: {description}')
            
            # Critical threshold for individual variances
            if variance_amount > 20000:
                log_message('CRITICAL', f'MATERIAL VARIANCE: ${variance_amount:,} exceeds materiality threshold')
                send_custom_metric('MaterialVariances', 1)
            
            send_custom_metric('AccuracyVariances', variance_amount, 'None', dimensions=[
                {'Name': 'ValidationCheck', 'Value': check_name}
            ])
        else:
            log_message('INFO', f'✓ ACCURATE: {check_name}')
        
        time.sleep(0.8)
    
    # Calculate overall accuracy
    accuracy_rate = ((total_amount_tested - variance_total) / total_amount_tested) * 100
    send_custom_metric('AccuracyRate', accuracy_rate, 'Percent')
    send_custom_metric('TotalVariance', variance_total, 'None')
    
    log_message('INFO', f'Data accuracy validation finished')
    log_message('INFO', f'Total amount tested: ${total_amount_tested:,}')
    log_message('INFO', f'Total variance: ${variance_total:,}')
    log_message('INFO', f'Accuracy rate: {accuracy_rate:.2f}%')
    
    return accuracy_issues, variance_total

def validate_access_controls():
    """Validate that proper access controls are in place and functioning"""
    log_message('INFO', 'Starting access control validation...')
    
    control_tests = [
        ('Segregation of Duties', 'No single person can complete entire transaction'),
        ('User Access Reviews', 'Quarterly access reviews completed'),
        ('Privileged Access Controls', 'Admin access properly restricted'),
        ('System Access Logging', 'All access attempts logged'),
        ('Password Policy Compliance', 'Strong passwords enforced'),
        ('Failed Login Monitoring', 'Suspicious activity detected')
    ]
    
    control_failures = []
    
    for control_name, description in control_tests:
        log_message('INFO', f'Testing control: {control_name}')
        
        # Simulate control failures
        failure_chance = random.random()
        
        if failure_chance < 0.10:  # 10% chance of control failure
            violation_count = random.randint(1, 15)
            
            control_failures.append({
                'control': control_name,
                'description': description,
                'violations': violation_count
            })
            
            log_message('ERROR', f'CONTROL FAILURE: {control_name}')
            log_message('ERROR', f'Violations detected: {violation_count}')
            
            # Specific logging for different types of failures
            if control_name == 'Segregation of Duties':
                log_message('ERROR', 'CRITICAL: Same user initiated and approved transactions')
                send_custom_metric('SODViolations', violation_count)
            elif control_name == 'Privileged Access Controls':
                log_message('ERROR', 'CRITICAL: Unauthorized privileged access detected')
                send_custom_metric('PrivilegedAccessViolations', violation_count)
            
            send_custom_metric('AccessControlViolations', violation_count, dimensions=[
                {'Name': 'ControlType', 'Value': control_name}
            ])
        else:
            log_message('INFO', f'✓ EFFECTIVE: {control_name}')
        
        time.sleep(0.3)
    
    control_effectiveness = ((len(control_tests) - len(control_failures)) / len(control_tests)) * 100
    send_custom_metric('ControlEffectiveness', control_effectiveness, 'Percent')
    
    log_message('INFO', f'Access control validation finished: {len(control_failures)} control failures detected')
    return control_failures

def generate_compliance_report(completeness_issues, accuracy_issues, variance_total, control_failures):
    """Generate summary compliance report"""
    log_message('INFO', 'Generating compliance validation report...')
    
    # Calculate overall compliance score
    total_issues = len(completeness_issues) + len(accuracy_issues) + len(control_failures)
    
    # Determine compliance status
    if total_issues == 0:
        compliance_status = 'COMPLIANT'
        compliance_score = 100.0
    elif total_issues <= 3 and variance_total < 10000:
        compliance_status = 'COMPLIANT WITH MINOR ISSUES'
        compliance_score = 85.0
    elif total_issues <= 8 and variance_total < 50000:
        compliance_status = 'NON-COMPLIANT - REMEDIATION REQUIRED'
        compliance_score = 60.0
    else:
        compliance_status = 'NON-COMPLIANT - MATERIAL WEAKNESSES'
        compliance_score = 30.0
    
    # Log detailed report
    log_message('INFO', '=' * 60)
    log_message('INFO', 'SOX COMPLIANCE VALIDATION REPORT')
    log_message('INFO', '=' * 60)
    log_message('INFO', f'Validation Date: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
    log_message('INFO', f'Overall Status: {compliance_status}')
    log_message('INFO', f'Compliance Score: {compliance_score:.1f}%')
    log_message('INFO', '')
    
    # Completeness findings
    log_message('INFO', f'DATA COMPLETENESS ISSUES: {len(completeness_issues)}')
    for issue in completeness_issues:
        log_message('WARNING', f'  • {issue["check"]}: {issue["missing_count"]} missing items')
    
    # Accuracy findings
    log_message('INFO', f'DATA ACCURACY ISSUES: {len(accuracy_issues)}')
    for issue in accuracy_issues:
        log_message('ERROR', f'  • {issue["check"]}: ${issue["variance"]:,} variance')
    log_message('INFO', f'Total Financial Variance: ${variance_total:,}')
    
    # Control findings
    log_message('INFO', f'ACCESS CONTROL FAILURES: {len(control_failures)}')
    for failure in control_failures:
        log_message('ERROR', f'  • {failure["control"]}: {failure["violations"]} violations')
    
    log_message('INFO', '=' * 60)
    
    # Send final compliance metrics
    send_custom_metric('ComplianceScore', compliance_score, 'Percent')
    send_custom_metric('TotalIssues', total_issues)
    
    # Determine if manual review is required
    if compliance_status in ['NON-COMPLIANT - REMEDIATION REQUIRED', 'NON-COMPLIANT - MATERIAL WEAKNESSES']:
        log_message('CRITICAL', 'MANUAL REVIEW REQUIRED: Compliance issues detected')
        log_message('CRITICAL', 'Contact SOX compliance team immediately')
        send_custom_metric('ManualReviewRequired', 1)
        
        if variance_total > 25000:
            log_message('CRITICAL', f'MATERIAL WEAKNESS: Total variance ${variance_total:,} exceeds materiality')
    
    return compliance_status, compliance_score

def main():
    """Main compliance validation process"""
    job_start_time = time.time()
    
    try:
        log_message('INFO', '=== SOX COMPLIANCE VALIDATION JOB STARTED ===')
        log_message('INFO', f'Job Name: {args["JOB_NAME"]}')
        log_message('INFO', f'Environment: {args["environment"]}')
        log_message('INFO', f'Validation Period: {datetime.now().strftime("%Y-%m")}')
        
        # Phase 1: Data Completeness Validation
        log_message('INFO', 'PHASE 1: Data Completeness Validation')
        completeness_issues = validate_data_completeness()
        
        # Phase 2: Data Accuracy Validation
        log_message('INFO', 'PHASE 2: Data Accuracy Validation')
        accuracy_issues, variance_total = validate_data_accuracy()
        
        # Phase 3: Access Control Validation
        log_message('INFO', 'PHASE 3: Access Control Validation')
        control_failures = validate_access_controls()
        
        # Phase 4: Generate Compliance Report
        log_message('INFO', 'PHASE 4: Compliance Report Generation')
        compliance_status, compliance_score = generate_compliance_report(
            completeness_issues, accuracy_issues, variance_total, control_failures
        )
        
        # Calculate job metrics
        job_end_time = time.time()
        job_duration = job_end_time - job_start_time
        
        # Final success metrics
        send_custom_metric('ValidationJobDuration', job_duration, 'Seconds')
        send_custom_metric('ValidationJobSuccess', 1)
        
        log_message('INFO', f'Validation completed in {job_duration:.2f} seconds')
        log_message('INFO', f'Final compliance status: {compliance_status}')
        log_message('INFO', '=== SOX COMPLIANCE VALIDATION JOB COMPLETED ===')
        
    except Exception as e:
        job_end_time = time.time()
        job_duration = job_end_time - job_start_time
        
        # Send failure metrics
        send_custom_metric('ValidationJobDuration', job_duration, 'Seconds')
        send_custom_metric('ValidationJobFailures', 1)
        
        log_message('ERROR', f'=== VALIDATION JOB FAILED AFTER {job_duration:.2f} SECONDS ===')
        log_message('ERROR', f'Error: {str(e)}')
        log_message('ERROR', 'Compliance validation could not be completed')
        log_message('CRITICAL', 'Manual validation required for this period')
        
        raise e
    
    finally:
        job.commit()

if __name__ == '__main__':
    main()
