# General Ledger Module Views
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date
from .models import JournalEntryHeader, JournalEntryDetail, Account, AccountType, FiscalYear

@login_required
def gl_dashboard(request):
    """General Ledger Dashboard"""
    from django.db.models import Sum, Q
    from datetime import datetime, timedelta
    
    # Calculate total assets (ASSET accounts with debit balance)
    asset_accounts = Account.objects.filter(account_type__category='ASSET')
    total_assets = asset_accounts.aggregate(Sum('balance'))['balance__sum'] or 0
    
    # Calculate total liabilities (LIABILITY accounts with credit balance)
    liability_accounts = Account.objects.filter(account_type__category='LIABILITY')
    total_liabilities = abs(liability_accounts.aggregate(Sum('balance'))['balance__sum'] or 0)
    
    # Calculate net worth (Assets - Liabilities)
    net_worth = total_assets - total_liabilities
    
    # Count unposted journal entries
    unposted_entries = JournalEntryHeader.objects.filter(is_posted=False).count()
    
    # Get recent journal entries (last 5)
    recent_entries = JournalEntryHeader.objects.order_by('-created_at')[:5]
    
    # Format recent entries for display
    formatted_recent_entries = []
    for entry in recent_entries:
        # Calculate days ago
        days_ago = (datetime.now().date() - entry.entry_date).days
        if days_ago == 0:
            time_display = "Today"
        elif days_ago == 1:
            time_display = "Yesterday"
        elif days_ago < 7:
            time_display = f"{days_ago} days ago"
        else:
            time_display = entry.entry_date.strftime("%b %d")
        
        # Determine status color
        if entry.is_posted:
            status_color = "success"
        else:
            status_color = "warning"
        
        formatted_recent_entries.append({
            'entry': entry,
            'time_display': time_display,
            'status_color': status_color,
            'amount_display': f"${entry.total_debit:,.2f}" if entry.total_debit else f"${entry.total_credit:,.2f}"
        })
    
    context = {
        'page_title': 'General Ledger Dashboard',
        'module_name': 'General Ledger',
        'total_assets': total_assets,
        'total_liabilities': total_liabilities,
        'net_worth': net_worth,
        'unposted_entries': unposted_entries,
        'recent_entries': formatted_recent_entries,
    }
    return render(request, 'gl/dashboard.html', context)

@login_required
def chart_of_accounts(request):
    """Chart of Accounts"""
    context = {
        'page_title': 'Chart of Accounts',
        'today': date.today().isoformat(),
    }
    return render(request, 'gl/chart_of_accounts.html', context)

@login_required
def account_list(request):
    """List all accounts"""
    return render(request, 'gl/account_list.html', {'page_title': 'Account List'})

@login_required
def account_create(request):
    """Create new account"""
    return render(request, 'gl/account_form.html', {'page_title': 'Create Account'})

@login_required
def account_detail(request, pk):
    """Account detail view"""
    return render(request, 'gl/account_detail.html', {'page_title': 'Account Details'})

@login_required
def account_edit(request, pk):
    """Edit account"""
    return render(request, 'gl/account_form.html', {'page_title': 'Edit Account'})

@login_required
def journal_entry_list(request):
    """List journal entries"""
    from django.db import models
    
    # Get search parameters
    search = request.GET.get('search', '')
    status = request.GET.get('status', '')
    date_from = request.GET.get('date_from', '')
    
    # Base query
    entries = JournalEntryHeader.objects.all()
    
    # Apply filters
    if search:
        entries = entries.filter(
            models.Q(entry_number__icontains=search) |
            models.Q(description__icontains=search) |
            models.Q(reference__icontains=search)
        )
    
    if status:
        if status == 'POSTED':
            entries = entries.filter(is_posted=True)
        elif status == 'DRAFT':
            entries = entries.filter(is_posted=False)
    
    if date_from:
        entries = entries.filter(entry_date__gte=date_from)
    
    # Get statistics
    draft_count = JournalEntryHeader.objects.filter(is_posted=False).count()
    posted_count = JournalEntryHeader.objects.filter(is_posted=True).count()
    
    # Calculate monthly totals
    from django.db.models import Sum
    from datetime import datetime
    current_month = datetime.now().month
    current_year = datetime.now().year
    
    monthly_entries = JournalEntryHeader.objects.filter(
        entry_date__month=current_month,
        entry_date__year=current_year
    )
    monthly_debits = monthly_entries.aggregate(Sum('total_debit'))['total_debit__sum'] or 0
    monthly_credits = monthly_entries.aggregate(Sum('total_credit'))['total_credit__sum'] or 0
    
    context = {
        'page_title': 'Journal Entries',
        'entries': entries,
        'draft_count': draft_count,
        'posted_count': posted_count,
        'monthly_debits': monthly_debits,
        'monthly_credits': monthly_credits,
    }
    return render(request, 'gl/journal_entry_list.html', context)

@login_required
def journal_entry_create(request):
    """Create journal entry"""
    if request.method == 'POST':
        # Handle form submission
        try:
            # Ensure we have a fiscal year
            fiscal_year = FiscalYear.objects.filter(is_current=True).first()
            if not fiscal_year:
                # Create a default fiscal year if none exists
                from datetime import datetime
                current_year = datetime.now().year
                fiscal_year = FiscalYear.objects.create(
                    name=f"FY {current_year}",
                    start_date=f"{current_year}-01-01",
                    end_date=f"{current_year}-12-31",
                    is_current=True,
                    is_closed=False
                )
            
            # Get next entry number
            last_entry = JournalEntryHeader.objects.order_by('-entry_number').first()
            if last_entry:
                last_num = int(last_entry.entry_number.split('-')[1]) if '-' in last_entry.entry_number else 0
                next_num = last_num + 1
            else:
                next_num = 1
            
            entry_number = f"JE-{next_num:04d}"
            
            # Create journal entry
            entry = JournalEntryHeader.objects.create(
                entry_number=entry_number,
                entry_date=request.POST.get('entry_date'),
                description=request.POST.get('description'),
                reference=request.POST.get('reference', ''),
                created_by=request.user,
                fiscal_year=fiscal_year
            )
            
            messages.success(request, f'Journal entry {entry_number} created successfully!')
            return redirect('gl:entry_detail', pk=entry.pk)
        except Exception as e:
            messages.error(request, f'Error creating journal entry: {str(e)}')
    
    # Get available accounts for the form
    accounts = Account.objects.filter(is_active=True).order_by('account_number')
    
    context = {
        'page_title': 'Create Journal Entry',
        'today': date.today().isoformat(),
        'accounts': accounts,
        'form': {
            'entry_number': {'value': None},
            'entry_date': {'value': None},
            'reference': {'value': None},
            'status': {'value': 'DRAFT'},
            'description': {'value': None},
        }
    }
    return render(request, 'gl/journal_entry_form.html', context)

@login_required
def journal_entry_detail(request, pk):
    """Journal entry detail"""
    try:
        entry = get_object_or_404(JournalEntryHeader, pk=pk)
        context = {
            'page_title': 'Journal Entry Details',
            'entry': entry,
        }
    except:
        # If no entry found, show message
        messages.error(request, 'Journal entry not found.')
        context = {
            'page_title': 'Journal Entry Details',
            'entry': None,
        }
    return render(request, 'gl/journal_entry_detail.html', context)

@login_required
def journal_entry_edit(request, pk):
    """Edit journal entry"""
    context = {
        'page_title': 'Edit Journal Entry',
        'today': date.today().isoformat(),
        'form': {
            'instance': {'pk': pk},
            'entry_number': {'value': 'JE-0001'},
            'entry_date': {'value': date.today()},
            'reference': {'value': 'INV-2025-001'},
            'status': {'value': 'DRAFT'},
            'description': {'value': 'Sample journal entry description'},
        }
    }
    return render(request, 'gl/journal_entry_form.html', context)

@login_required
def journal_entry_post(request, pk):
    """Post journal entry"""
    try:
        entry = get_object_or_404(JournalEntryHeader, pk=pk)
        
        # Post the journal entry
        entry.is_posted = True
        entry.save()
        
        messages.success(request, f'Journal entry {entry.entry_number} posted successfully!')
        
        context = {
            'page_title': 'Journal Entry Details',
            'entry': entry,
        }
        return render(request, 'gl/journal_entry_detail.html', context)
    except Exception as e:
        messages.error(request, f'Error posting journal entry: {str(e)}')
        return redirect('gl:entry_list')

@login_required
def trial_balance(request):
    """Trial Balance Report"""
    context = {
        'page_title': 'Trial Balance',
        'as_of_date': date.today(),
        'today': date.today().isoformat(),
        'balanced': True,
        'show_zero': False,
    }
    return render(request, 'gl/trial_balance.html', context)

@login_required
def income_statement(request):
    """Income Statement Report"""
    context = {
        'page_title': 'Income Statement',
        'today': date.today().isoformat(),
    }
    return render(request, 'gl/income_statement.html', context)

@login_required
def balance_sheet(request):
    """Balance Sheet Report"""
    context = {
        'page_title': 'Balance Sheet',
        'today': date.today().isoformat(),
    }
    return render(request, 'gl/balance_sheet.html', context)

@login_required
def cash_flow_statement(request):
    """Cash Flow Statement Report"""
    context = {
        'page_title': 'Cash Flow Statement',
        'today': date.today().isoformat(),
    }
    return render(request, 'gl/cash_flow_statement.html', context)

@login_required
def general_ledger_report(request):
    """General Ledger Report"""
    context = {
        'page_title': 'General Ledger Report',
        'today': date.today().isoformat(),
    }
    return render(request, 'gl/general_ledger_report.html', context)

@login_required
def reports_dashboard(request):
    """Reports Dashboard"""
    return render(request, 'gl/reports_dashboard.html', {'page_title': 'Financial Reports'})

@login_required
def fiscal_year_list(request):
    """List fiscal years"""
    return render(request, 'gl/fiscal_year_list.html', {'page_title': 'Fiscal Years'})

@login_required
def fiscal_year_create(request):
    """Create fiscal year"""
    return render(request, 'gl/fiscal_year_form.html', {'page_title': 'Create Fiscal Year'})
