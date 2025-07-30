#!/usr/bin/env python3
"""
Sample data creation script for EasyTicket system
Run this to populate the system with realistic IT auditing scenarios
"""

import os
import sys
import django
from datetime import datetime, timedelta
from django.utils import timezone

# Setup Django
sys.path.append('/app')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'easyticket.settings')
django.setup()

from django.contrib.auth.models import User
from tickets.models import TicketType, Ticket, TicketApproval, TicketComment

def create_sample_data():
    print("Creating sample data for EasyTicket...")
    
    # Create admin user if it doesn't exist
    admin_user, created = User.objects.get_or_create(
        username='admin',
        defaults={
            'email': 'admin@example.com',
            'is_staff': True,
            'is_superuser': True,
        }
    )
    if created:
        admin_user.set_password('password')
        admin_user.save()
        print("✓ Created admin user")
    
    # Create ticket types
    ticket_types_data = [
        {
            'name': 'Standard Change Request',
            'description': 'Regular planned changes that follow standard procedures and have pre-approved risk assessments'
        },
        {
            'name': 'Emergency Change Request', 
            'description': 'Urgent changes requiring immediate action due to critical business impact or security issues'
        },
        {
            'name': 'Access Request',
            'description': 'Requests for system, application, or data access including new access, modifications, and removals'
        },
        {
            'name': 'Incident',
            'description': 'Service disruptions, system failures, or security incidents requiring investigation and resolution'
        },
        {
            'name': 'Security Exception',
            'description': 'Requests for temporary or permanent exceptions to security policies and controls'
        },
    ]
    
    for type_data in ticket_types_data:
        ticket_type, created = TicketType.objects.get_or_create(
            name=type_data['name'],
            defaults={'description': type_data['description']}
        )
        if created:
            print(f"✓ Created ticket type: {type_data['name']}")
    
    # Create sample tickets with realistic auditing scenarios
    sample_tickets = [
        {
            'title': 'Production Database Access for Financial Reporting',
            'description': 'Request read-only access to production financial database for monthly SOX compliance reporting. Access needed for tables: GL_ACCOUNTS, JOURNAL_ENTRIES, FINANCIAL_STATEMENTS.',
            'ticket_type': 'Access Request',
            'status': 'pending_approval',
            'priority': 'high',
            'requested_by': 'Sarah Johnson - Finance Manager',
            'business_justification': 'Required for SOX 404 compliance testing and monthly financial close process. Current manual process is inefficient and error-prone.',
            'technical_details': 'Read-only SELECT privileges on finance schema. Access through dedicated reporting user account with IP restrictions.',
            'risk_assessment': 'LOW RISK: Read-only access with proper logging and monitoring. No write permissions requested.',
            'approvers': [
                ('Michael Chen - IT Security Manager', 'IT Security'),
                ('David Wilson - Database Administrator', 'Database Team'),
                ('Jennifer Adams - CFO', 'Finance Leadership')
            ]
        },
        {
            'title': 'Emergency Patch Deployment - Critical Security Vulnerability',
            'description': 'Deploy critical security patches to address CVE-2024-1234 vulnerability in web application servers. Affects all production web servers.',
            'ticket_type': 'Emergency Change Request',
            'status': 'approved',
            'priority': 'critical',
            'requested_by': 'IT Security Team',
            'business_justification': 'Critical security vulnerability with active exploits in the wild. Immediate patching required to prevent potential data breach.',
            'technical_details': 'Deploy security patch v2.1.5 to all web servers. Requires 15-minute maintenance window per server with rolling deployment.',
            'risk_assessment': 'HIGH RISK: Emergency change with limited testing window. However, risk of not patching is significantly higher.',
            'approvers': [
                ('Robert Taylor - CISO', 'Information Security'),
                ('Lisa Brown - CTO', 'Technology Leadership')
            ]
        },
        {
            'title': 'Quarterly User Access Review - Privileged Accounts',
            'description': 'Systematic review of all privileged user accounts across systems as part of quarterly access governance process.',
            'ticket_type': 'Standard Change Request',
            'status': 'in_progress',
            'priority': 'medium',
            'requested_by': 'Compliance Team',
            'business_justification': 'Mandatory quarterly review per corporate access governance policy and SOX requirements.',
            'technical_details': 'Review all accounts with admin privileges across AD, databases, and applications. Generate access reports and obtain manager attestations.',
            'risk_assessment': 'LOW RISK: Standard governance process with established procedures.',
            'approvers': [
                ('Amanda Foster - Compliance Manager', 'Risk & Compliance'),
                ('Mark Rodriguez - IT Director', 'IT Management')
            ]
        },
        {
            'title': 'Server Outage - Customer Portal Down',
            'description': 'Customer portal is completely inaccessible. Error 500 on all pages. Started approximately 2:30 PM EST.',
            'ticket_type': 'Incident',
            'status': 'open',
            'priority': 'critical',
            'requested_by': 'NOC Team',
            'business_justification': 'Critical customer-facing service disruption affecting revenue and customer satisfaction.',
            'technical_details': 'Web servers responding with HTTP 500 errors. Database connectivity appears normal. Investigating application logs.',
            'risk_assessment': 'HIGH IMPACT: Customer-facing service disruption. Revenue loss and reputation damage if not resolved quickly.',
        },
        {
            'title': 'Temporary Firewall Exception for Vendor Integration',
            'description': 'Request temporary firewall rule to allow vendor XYZ to access internal API for data migration project.',
            'ticket_type': 'Security Exception',
            'status': 'rejected',
            'priority': 'medium',
            'requested_by': 'Project Manager - Data Migration',
            'business_justification': 'Vendor needs direct API access to migrate legacy data to new system. Project deadline is approaching.',
            'technical_details': 'Open port 8443 from vendor IP 203.45.67.89 to internal API server 10.1.2.15 for 30 days.',
            'risk_assessment': 'HIGH RISK: Direct external access to internal systems. Alternative secure methods should be explored.',
            'approvers': [
                ('Michael Chen - IT Security Manager', 'IT Security'),
            ]
        },
        {
            'title': 'New Employee Onboarding - System Access Setup',
            'description': 'Setup system access for new hire in Finance department. Standard access package required.',
            'ticket_type': 'Access Request',
            'status': 'closed',
            'priority': 'low',
            'requested_by': 'HR Department',
            'business_justification': 'New employee starting Monday. Requires standard finance user access to perform job duties.',
            'technical_details': 'Create AD account, assign to Finance security groups, provision ERP access with standard finance role.',
            'risk_assessment': 'LOW RISK: Standard onboarding process with appropriate approvals.',
            'approvers': [
                ('Jennifer Adams - CFO', 'Finance Leadership'),
                ('Amanda Foster - Compliance Manager', 'Risk & Compliance')
            ]
        }
    ]
    
    for ticket_data in sample_tickets:
        # Get ticket type
        ticket_type = TicketType.objects.get(name=ticket_data['ticket_type'])
        
        # Create ticket
        ticket = Ticket.objects.create(
            title=ticket_data['title'],
            description=ticket_data['description'],
            ticket_type=ticket_type,
            status=ticket_data['status'],
            priority=ticket_data['priority'],
            requested_by=ticket_data['requested_by'],
            business_justification=ticket_data['business_justification'],
            technical_details=ticket_data['technical_details'],
            risk_assessment=ticket_data['risk_assessment'],
            created_by=admin_user,
            created_at=timezone.now() - timedelta(days=random.randint(1, 30))
        )
        
        # Create approvals if specified
        if 'approvers' in ticket_data:
            for approver_name, approver_title in ticket_data['approvers']:
                approval_status = 'pending'
                if ticket_data['status'] == 'approved':
                    approval_status = 'approved'
                elif ticket_data['status'] == 'rejected':
                    approval_status = 'rejected'
                
                TicketApproval.objects.create(
                    ticket=ticket,
                    approver_name=approver_name,
                    approver_title=approver_title,
                    status=approval_status,
                    comments=f"Approval {'granted' if approval_status == 'approved' else 'pending review' if approval_status == 'pending' else 'denied'} per standard procedures."
                )
        
        # Add some comments for demonstration
        comments_data = [
            "Initial assessment completed. Moving to approval workflow.",
            "Security review in progress. Additional documentation may be required.",
            "Business stakeholder approval received. Technical review next.",
        ]
        
        if ticket_data['status'] in ['in_progress', 'approved', 'closed']:
            for i, comment_text in enumerate(comments_data[:2]):  # Add first 2 comments
                TicketComment.objects.create(
                    ticket=ticket,
                    author=admin_user,
                    comment=comment_text,
                    is_internal=False,
                    created_at=ticket.created_at + timedelta(days=i+1)
                )
        
        print(f"✓ Created ticket: {ticket.ticket_number} - {ticket.title[:50]}...")
    
    print(f"\n✅ Sample data creation complete!")
    print(f"   - {TicketType.objects.count()} ticket types")
    print(f"   - {Ticket.objects.count()} tickets")
    print(f"   - {TicketApproval.objects.count()} approvals")
    print(f"   - {TicketComment.objects.count()} comments")
    print(f"\nYou can now access the application and see realistic IT auditing scenarios!")

if __name__ == '__main__':
    import random
    create_sample_data()
