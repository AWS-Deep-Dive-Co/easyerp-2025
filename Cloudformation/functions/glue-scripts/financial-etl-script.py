"""
Financial Data ETL Script for SOX Auditor Training
This script simulates a financial data processing pipeline with realistic failure scenarios
"""

import sys
import random
import time
from datetime import datetime
from awsglue.transforms import *
from awsglue.utils import getResolvedOptions
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql import DataFrame
from pyspark.sql.functions import *
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
            Namespace='FinancialProcessing/GlueETL',
            MetricData=[metric_data]
        )
    except Exception as e:
        log_message('ERROR', f'Failed to send metric {metric_name}: {str(e)}')

def simulate_data_extraction():
    """Simulate extracting data from various financial systems"""
    log_message('INFO', 'Starting data extraction from financial systems...')
    
    # Simulate different data sources
    sources = [
        'General Ledger System',
        'Accounts Payable System', 
        'Accounts Receivable System',
        'Payroll System',
        'Fixed Assets System'
    ]
    
    extracted_records = 0
    failed_sources = []
    
    for source in sources:
        log_message('INFO', f'Extracting data from: {source}')
        
        # Simulate random extraction issues
        failure_chance = random.random()
        
        if failure_chance < 0.10:  # 10% chance of source failure
            error_msg = f'Connection timeout to {source}'
            log_message('ERROR', error_msg)
            failed_sources.append(source)
            send_custom_metric('SourceConnectionFailures', 1, dimensions=[
                {'Name': 'SourceSystem', 'Value': source}
            ])
            continue
            
        # Simulate successful extraction
        records = random.randint(10000, 50000)
        extracted_records += records
        log_message('INFO', f'Extracted {records:,} records from {source}')
        time.sleep(1)  # Simulate processing time
    
    if failed_sources:
        raise Exception(f'Data extraction failed for sources: {", ".join(failed_sources)}')
    
    log_message('INFO', f'Total records extracted: {extracted_records:,}')
    send_custom_metric('ExtractedRecords', extracted_records)
    return extracted_records

def simulate_data_transformation(record_count):
    """Simulate data transformation and validation"""
    log_message('INFO', 'Starting data transformation and validation...')
    
    # Simulate transformation processes
    transformations = [
        'Currency standardization',
        'Date format normalization', 
        'Account code mapping',
        'Duplicate detection',
        'Data type conversion',
        'Business rule validation'
    ]
    
    processed_records = 0
    validation_errors = 0
    
    for transformation in transformations:
        log_message('INFO', f'Applying transformation: {transformation}')
        
        # Simulate validation failures
        failure_chance = random.random()
        
        if failure_chance < 0.15:  # 15% chance of validation issues
            error_count = random.randint(100, 1000)
            validation_errors += error_count
            
            if transformation == 'Business rule validation':
                log_message('ERROR', f'CRITICAL: {error_count} records failed business rule validation')
                log_message('ERROR', 'Sample errors: Invalid GL account codes, missing required fields')
                send_custom_metric('BusinessRuleViolations', error_count)
                
                # Critical business rule failures should stop processing
                if error_count > 500:
                    raise Exception(f'Too many business rule violations ({error_count}). Processing halted.')
            else:
                log_message('WARNING', f'{error_count} records failed {transformation}')
                
        time.sleep(0.5)  # Simulate processing time
    
    # Calculate successful transformations
    processed_records = record_count - validation_errors
    
    if validation_errors > 0:
        log_message('WARNING', f'Transformation completed with {validation_errors:,} validation errors')
        log_message('WARNING', f'Successfully processed: {processed_records:,} records')
        
        # Send metrics
        send_custom_metric('ProcessedRecords', processed_records)
        send_custom_metric('ValidationErrors', validation_errors)
        send_custom_metric('SuccessRate', (processed_records / record_count) * 100, 'Percent')
    else:
        log_message('INFO', f'All {processed_records:,} records processed successfully')
        send_custom_metric('ProcessedRecords', processed_records)
        send_custom_metric('SuccessRate', 100.0, 'Percent')
    
    return processed_records, validation_errors

def simulate_data_loading(record_count):
    """Simulate loading data to data warehouse"""
    log_message('INFO', 'Starting data loading to financial data warehouse...')
    
    # Simulate different loading phases
    phases = [
        'Staging table insert',
        'Dimension table updates',
        'Fact table insert', 
        'Index rebuilding',
        'Statistics update'
    ]
    
    for phase in phases:
        log_message('INFO', f'Executing: {phase}')
        
        # Simulate potential loading issues
        failure_chance = random.random()
        
        if failure_chance < 0.05:  # 5% chance of loading failure
            error_msg = f'Loading failure during {phase}: Table lock timeout'
            log_message('ERROR', error_msg)
            send_custom_metric('LoadingFailures', 1, dimensions=[
                {'Name': 'Phase', 'Value': phase}
            ])
            raise Exception(error_msg)
            
        time.sleep(1)  # Simulate loading time
        log_message('INFO', f'✓ Completed: {phase}')
    
    log_message('INFO', f'Successfully loaded {record_count:,} records to data warehouse')
    send_custom_metric('LoadedRecords', record_count)

def main():
    """Main ETL process"""
    job_start_time = time.time()
    
    try:
        log_message('INFO', '=== FINANCIAL DATA ETL JOB STARTED ===')
        log_message('INFO', f'Job Name: {args["JOB_NAME"]}')
        log_message('INFO', f'Environment: {args["environment"]}')
        log_message('INFO', f'Start Time: {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}')
        
        # Phase 1: Data Extraction
        log_message('INFO', 'PHASE 1: Data Extraction')
        extracted_records = simulate_data_extraction()
        
        # Phase 2: Data Transformation
        log_message('INFO', 'PHASE 2: Data Transformation and Validation')
        processed_records, validation_errors = simulate_data_transformation(extracted_records)
        
        # Phase 3: Data Loading
        log_message('INFO', 'PHASE 3: Data Loading')
        simulate_data_loading(processed_records)
        
        # Calculate job metrics
        job_end_time = time.time()
        job_duration = job_end_time - job_start_time
        
        # Final success metrics
        send_custom_metric('JobDuration', job_duration, 'Seconds')
        send_custom_metric('JobSuccess', 1)
        
        log_message('INFO', f'Job completed successfully in {job_duration:.2f} seconds')
        log_message('INFO', f'Records processed: {processed_records:,}')
        
        if validation_errors > 0:
            log_message('WARNING', f'Job completed with {validation_errors:,} validation errors')
        
        log_message('INFO', '=== FINANCIAL DATA ETL JOB COMPLETED ===')
        
    except Exception as e:
        job_end_time = time.time()
        job_duration = job_end_time - job_start_time
        
        # Send failure metrics
        send_custom_metric('JobDuration', job_duration, 'Seconds')
        send_custom_metric('JobFailures', 1)
        
        log_message('ERROR', f'=== JOB FAILED AFTER {job_duration:.2f} SECONDS ===')
        log_message('ERROR', f'Error: {str(e)}')
        log_message('ERROR', 'Manual intervention required')
        
        raise e
    
    finally:
        job.commit()

if __name__ == '__main__':
    main()
