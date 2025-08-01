from django.core.management.base import BaseCommand
from GL.models import AccountType, Account, FiscalYear
from datetime import datetime

class Command(BaseCommand):
    help = 'Create initial GL accounts and fiscal year data'

    def handle(self, *args, **options):
        self.stdout.write('Setting up initial GL data...')
        
        # Create account types
        account_types = [
            ('Cash', 'ASSET', 'DEBIT'),
            ('Accounts Receivable', 'ASSET', 'DEBIT'),
            ('Inventory', 'ASSET', 'DEBIT'),
            ('Equipment', 'ASSET', 'DEBIT'),
            ('Accounts Payable', 'LIABILITY', 'CREDIT'),
            ('Notes Payable', 'LIABILITY', 'CREDIT'),
            ('Owner\'s Capital', 'EQUITY', 'CREDIT'),
            ('Sales Revenue', 'REVENUE', 'CREDIT'),
            ('Cost of Goods Sold', 'EXPENSE', 'DEBIT'),
            ('Operating Expenses', 'EXPENSE', 'DEBIT'),
        ]
        
        for name, category, normal_balance in account_types:
            account_type, created = AccountType.objects.get_or_create(
                name=name,
                defaults={
                    'category': category,
                    'normal_balance': normal_balance,
                    'description': f'{name} account type'
                }
            )
            if created:
                self.stdout.write(f'Created account type: {name}')
        
        # Create basic chart of accounts
        accounts = [
            ('1000', 'Cash - Operating', 'Cash'),
            ('1010', 'Cash - Savings', 'Cash'),
            ('1100', 'Accounts Receivable', 'Accounts Receivable'),
            ('1200', 'Inventory', 'Inventory'),
            ('1500', 'Equipment', 'Equipment'),
            ('2000', 'Accounts Payable', 'Accounts Payable'),
            ('2200', 'Notes Payable', 'Notes Payable'),
            ('3000', 'Owner\'s Capital', 'Owner\'s Capital'),
            ('4000', 'Sales Revenue', 'Sales Revenue'),
            ('5000', 'Cost of Goods Sold', 'Cost of Goods Sold'),
            ('6000', 'Operating Expenses', 'Operating Expenses'),
        ]
        
        for account_number, account_name, account_type_name in accounts:
            try:
                account_type = AccountType.objects.get(name=account_type_name)
                account, created = Account.objects.get_or_create(
                    account_number=account_number,
                    defaults={
                        'account_name': account_name,
                        'account_type': account_type,
                        'balance': 0,
                        'is_active': True,
                        'description': f'{account_name} account'
                    }
                )
                if created:
                    self.stdout.write(f'Created account: {account_number} - {account_name}')
            except AccountType.DoesNotExist:
                self.stdout.write(f'Account type {account_type_name} not found, skipping account {account_number}')
        
        # Create current fiscal year
        current_year = datetime.now().year
        fiscal_year, created = FiscalYear.objects.get_or_create(
            name=f"FY {current_year}",
            defaults={
                'start_date': f"{current_year}-01-01",
                'end_date': f"{current_year}-12-31",
                'is_current': True,
                'is_closed': False
            }
        )
        if created:
            self.stdout.write(f'Created fiscal year: FY {current_year}')
        
        self.stdout.write(self.style.SUCCESS('Successfully set up initial GL data'))
