# Enhanced General Ledger Models
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
import uuid

User = get_user_model()

class AccountType(models.Model):
    """Account Type master data"""
    CATEGORY_CHOICES = [
        ('ASSET', 'Assets'),
        ('LIABILITY', 'Liabilities'), 
        ('EQUITY', 'Equity'),
        ('REVENUE', 'Revenue'),
        ('EXPENSE', 'Expenses'),
    ]
    
    name = models.CharField(max_length=100, unique=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    normal_balance = models.CharField(max_length=10, choices=[('DEBIT', 'Debit'), ('CREDIT', 'Credit')])
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.name} ({self.category})"

class Account(models.Model):
    """Enhanced Chart of Accounts"""
    account_number = models.CharField(max_length=20, unique=True)
    account_name = models.CharField(max_length=250)
    account_type = models.ForeignKey(AccountType, on_delete=models.CASCADE)
    parent_account = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    balance = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    is_active = models.BooleanField(default=True)
    is_header = models.BooleanField(default=False)  # For grouping accounts
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.account_number} - {self.account_name}"

    class Meta:
        ordering = ['account_number']

class FiscalYear(models.Model):
    """Fiscal Year management"""
    name = models.CharField(max_length=50)
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=False)
    is_closed = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['-start_date']

class JournalEntryHeader(models.Model):
    """Journal Entry header with enhanced features"""
    ENTRY_TYPES = [
        ('MANUAL', 'Manual Entry'),
        ('AUTO', 'Automatic Entry'),
        ('CLOSING', 'Closing Entry'),
        ('ADJUSTMENT', 'Adjustment Entry'),
    ]

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    entry_number = models.CharField(max_length=50, unique=True)
    entry_type = models.CharField(max_length=20, choices=ENTRY_TYPES, default='MANUAL')
    entry_date = models.DateField(default=timezone.now)
    fiscal_year = models.ForeignKey(FiscalYear, on_delete=models.CASCADE)
    description = models.CharField(max_length=250)
    reference = models.CharField(max_length=100, blank=True)
    total_debit = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    total_credit = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    is_posted = models.BooleanField(default=False)
    posted_date = models.DateTimeField(null=True, blank=True)
    created_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    approved_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='approved_entries')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.entry_number} - {self.description}"

    @property
    def is_balanced(self):
        return self.total_debit == self.total_credit

    class Meta:
        ordering = ['-entry_date', '-created_at']
        verbose_name_plural = "Journal Entries"

class JournalEntryDetail(models.Model):
    """Journal Entry line items"""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    journal_entry = models.ForeignKey(JournalEntryHeader, on_delete=models.CASCADE, related_name='lines')
    account = models.ForeignKey(Account, on_delete=models.CASCADE)
    description = models.CharField(max_length=250, blank=True)
    debit_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    credit_amount = models.DecimalField(max_digits=15, decimal_places=2, default=0)
    
    def __str__(self):
        return f"{self.journal_entry.entry_number} - {self.account.account_name}"

    class Meta:
        ordering = ['id']

class FinancialPeriod(models.Model):
    """Monthly/Quarterly periods for financial reporting"""
    PERIOD_TYPES = [
        ('MONTHLY', 'Monthly'),
        ('QUARTERLY', 'Quarterly'),
        ('YEARLY', 'Yearly'),
    ]

    fiscal_year = models.ForeignKey(FiscalYear, on_delete=models.CASCADE)
    period_type = models.CharField(max_length=20, choices=PERIOD_TYPES)
    period_number = models.IntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    is_closed = models.BooleanField(default=False)
    closed_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.fiscal_year.name} - {self.period_type} {self.period_number}"

    class Meta:
        unique_together = ['fiscal_year', 'period_type', 'period_number']
        ordering = ['fiscal_year', 'period_number']