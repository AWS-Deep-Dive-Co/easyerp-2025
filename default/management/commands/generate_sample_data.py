from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.utils import timezone
from datetime import datetime, timedelta, date
from decimal import Decimal
import random

# Import all models
from default.models import User
from GL.models import AccountType, Account, FiscalYear, JournalEntryHeader, JournalEntryDetail
from inventory.models import Category, Product, Warehouse, StockMovement, Supplier
from sales.models import Customer, SalesOrder, SalesOrderLine, Invoice
from purchasing.models import PurchaseOrder, PurchaseOrderLine, GoodsReceipt, GoodsReceiptLine

User = get_user_model()

class Command(BaseCommand):
    help = 'Generate comprehensive sample data for all ERP modules'

    def add_arguments(self, parser):
        parser.add_argument(
            '--clear',
            action='store_true',
            help='Clear existing data before generating new data',
        )

    def handle(self, *args, **options):
        if options['clear']:
            self.stdout.write('Clearing existing data...')
            self.clear_data()

        self.stdout.write('Generating comprehensive sample data...')
        
        # Generate data in order of dependencies
        self.create_users()
        self.create_gl_data()
        self.create_inventory_data()
        self.create_customer_data()
        self.create_supplier_data()
        self.create_sales_data()
        self.create_purchasing_data()
        self.create_journal_entries()
        
        self.stdout.write(self.style.SUCCESS('Successfully generated comprehensive sample data'))

    def clear_data(self):
        """Clear existing data"""
        # Clear in reverse dependency order
        JournalEntryDetail.objects.all().delete()
        JournalEntryHeader.objects.all().delete()
        GoodsReceiptLine.objects.all().delete()
        GoodsReceipt.objects.all().delete()
        PurchaseOrderLine.objects.all().delete()
        PurchaseOrder.objects.all().delete()
        Invoice.objects.all().delete()
        SalesOrderLine.objects.all().delete()
        SalesOrder.objects.all().delete()
        StockMovement.objects.all().delete()
        Product.objects.all().delete()
        Category.objects.all().delete()
        Warehouse.objects.all().delete()
        Customer.objects.all().delete()
        Supplier.objects.all().delete()
        Account.objects.all().delete()
        AccountType.objects.all().delete()
        FiscalYear.objects.all().delete()
        
        # Keep admin user, delete others
        User.objects.filter(is_superuser=False).delete()

    def create_users(self):
        """Create sample users"""
        self.stdout.write('Creating users...')
        
        # Create admin user if doesn't exist
        if not User.objects.filter(username='admin').exists():
            User.objects.create_superuser(
                username='admin',
                email='admin@easyerp.com',
                password='admin123',
                first_name='System',
                last_name='Administrator'
            )
        
        # Create regular users
        users_data = [
            ('john.doe', 'john@easyerp.com', 'John', 'Doe', 'Accounting Manager'),
            ('jane.smith', 'jane@easyerp.com', 'Jane', 'Smith', 'Sales Manager'),
            ('mike.wilson', 'mike@easyerp.com', 'Mike', 'Wilson', 'Inventory Manager'),
            ('sarah.johnson', 'sarah@easyerp.com', 'Sarah', 'Johnson', 'Purchasing Manager'),
            ('david.brown', 'david@easyerp.com', 'David', 'Brown', 'Finance Director'),
        ]
        
        for username, email, first_name, last_name, position in users_data:
            if not User.objects.filter(username=username).exists():
                User.objects.create_user(
                    username=username,
                    email=email,
                    password='password123',
                    first_name=first_name,
                    last_name=last_name,
                    position=position
                )

    def create_gl_data(self):
        """Create GL accounts and fiscal year"""
        self.stdout.write('Creating GL data...')
        
        # Create account types
        account_types_data = [
            ('Current Assets', 'ASSET', 'DEBIT', 'Current assets - cash, receivables, inventory'),
            ('Fixed Assets', 'ASSET', 'DEBIT', 'Fixed assets - equipment, buildings'),
            ('Current Liabilities', 'LIABILITY', 'CREDIT', 'Current liabilities - accounts payable'),
            ('Long-term Liabilities', 'LIABILITY', 'CREDIT', 'Long-term debt and obligations'),
            ('Owner\'s Equity', 'EQUITY', 'CREDIT', 'Owner\'s equity and retained earnings'),
            ('Sales Revenue', 'REVENUE', 'CREDIT', 'Revenue from sales and services'),
            ('Cost of Sales', 'EXPENSE', 'DEBIT', 'Cost of goods sold'),
            ('Operating Expenses', 'EXPENSE', 'DEBIT', 'Operating and administrative expenses'),
        ]
        
        for name, category, normal_balance, description in account_types_data:
            AccountType.objects.get_or_create(
                name=name,
                defaults={
                    'category': category,
                    'normal_balance': normal_balance,
                    'description': description
                }
            )
        
        # Create detailed chart of accounts
        accounts_data = [
            # Assets
            ('1000', 'Cash - Operating', 'Current Assets', Decimal('25000.00')),
            ('1010', 'Cash - Savings', 'Current Assets', Decimal('50000.00')),
            ('1020', 'Petty Cash', 'Current Assets', Decimal('500.00')),
            ('1100', 'Accounts Receivable', 'Current Assets', Decimal('35000.00')),
            ('1200', 'Inventory - Raw Materials', 'Current Assets', Decimal('45000.00')),
            ('1210', 'Inventory - Finished Goods', 'Current Assets', Decimal('65000.00')),
            ('1300', 'Prepaid Expenses', 'Current Assets', Decimal('3200.00')),
            ('1500', 'Equipment', 'Fixed Assets', Decimal('120000.00')),
            ('1510', 'Accumulated Depreciation - Equipment', 'Fixed Assets', Decimal('-25000.00')),
            ('1600', 'Vehicles', 'Fixed Assets', Decimal('45000.00')),
            ('1610', 'Accumulated Depreciation - Vehicles', 'Fixed Assets', Decimal('-15000.00')),
            
            # Liabilities
            ('2000', 'Accounts Payable', 'Current Liabilities', Decimal('-18500.00')),
            ('2100', 'Accrued Liabilities', 'Current Liabilities', Decimal('-5200.00')),
            ('2200', 'Sales Tax Payable', 'Current Liabilities', Decimal('-2800.00')),
            ('2300', 'Notes Payable - Short Term', 'Current Liabilities', Decimal('-15000.00')),
            ('2500', 'Notes Payable - Long Term', 'Long-term Liabilities', Decimal('-75000.00')),
            
            # Equity
            ('3000', 'Owner\'s Capital', 'Owner\'s Equity', Decimal('-150000.00')),
            ('3100', 'Retained Earnings', 'Owner\'s Equity', Decimal('-45000.00')),
            ('3200', 'Current Year Earnings', 'Owner\'s Equity', Decimal('0.00')),
            
            # Revenue
            ('4000', 'Product Sales', 'Sales Revenue', Decimal('0.00')),
            ('4100', 'Service Revenue', 'Sales Revenue', Decimal('0.00')),
            ('4200', 'Other Income', 'Sales Revenue', Decimal('0.00')),
            
            # Expenses
            ('5000', 'Cost of Goods Sold', 'Cost of Sales', Decimal('0.00')),
            ('5100', 'Materials Cost', 'Cost of Sales', Decimal('0.00')),
            ('6000', 'Salaries and Wages', 'Operating Expenses', Decimal('0.00')),
            ('6100', 'Rent Expense', 'Operating Expenses', Decimal('0.00')),
            ('6200', 'Utilities', 'Operating Expenses', Decimal('0.00')),
            ('6300', 'Office Supplies', 'Operating Expenses', Decimal('0.00')),
            ('6400', 'Depreciation Expense', 'Operating Expenses', Decimal('0.00')),
            ('6500', 'Insurance', 'Operating Expenses', Decimal('0.00')),
            ('6600', 'Marketing and Advertising', 'Operating Expenses', Decimal('0.00')),
            ('6700', 'Professional Services', 'Operating Expenses', Decimal('0.00')),
        ]
        
        for account_number, account_name, account_type_name, balance in accounts_data:
            account_type = AccountType.objects.get(name=account_type_name)
            Account.objects.get_or_create(
                account_number=account_number,
                defaults={
                    'account_name': account_name,
                    'account_type': account_type,
                    'balance': balance,
                    'is_active': True,
                    'description': f'{account_name} account'
                }
            )
        
        # Create fiscal year
        current_year = datetime.now().year
        FiscalYear.objects.get_or_create(
            name=f"FY {current_year}",
            defaults={
                'start_date': f"{current_year}-01-01",
                'end_date': f"{current_year}-12-31",
                'is_current': True,
                'is_closed': False
            }
        )

    def create_inventory_data(self):
        """Create inventory data"""
        self.stdout.write('Creating inventory data...')
        
        # Create warehouses
        warehouses_data = [
            ('Main Warehouse', '123 Industrial Blvd, City, State 12345', True),
            ('Retail Store', '456 Main Street, Downtown, State 12345', True),
            ('Backup Warehouse', '789 Storage Lane, Suburb, State 12345', False),
        ]
        
        for name, location, is_active in warehouses_data:
            warehouse, created = Warehouse.objects.get_or_create(
                name=name,
                defaults={
                    'code': name.replace(' ', '_').upper()[:20],
                    'address': location,
                    'is_active': is_active
                }
            )
        
        # Create categories
        categories_data = [
            ('Electronics', 'Electronic devices and components'),
            ('Office Supplies', 'Office and administrative supplies'),
            ('Hardware', 'Tools and hardware items'),
            ('Software', 'Software products and licenses'),
            ('Services', 'Service-based products'),
        ]
        
        for name, description in categories_data:
            Category.objects.get_or_create(
                name=name,
                defaults={'description': description}
            )
        
        # Create products
        main_warehouse = Warehouse.objects.get(name='Main Warehouse')
        electronics = Category.objects.get(name='Electronics')
        office = Category.objects.get(name='Office Supplies')
        hardware = Category.objects.get(name='Hardware')
        software = Category.objects.get(name='Software')
        
        products_data = [
            ('LAPTOP001', 'Business Laptop - Dell Latitude', electronics, Decimal('899.99'), Decimal('1299.99'), 25, 10),
            ('MOUSE001', 'Wireless Mouse - Logitech', electronics, Decimal('29.99'), Decimal('49.99'), 50, 20),
            ('KEYBOARD001', 'Mechanical Keyboard', electronics, Decimal('79.99'), Decimal('129.99'), 30, 15),
            ('MONITOR001', '24" LCD Monitor', electronics, Decimal('149.99'), Decimal('249.99'), 15, 5),
            ('PAPER001', 'Copy Paper - 500 sheets', office, Decimal('4.99'), Decimal('8.99'), 100, 25),
            ('PEN001', 'Ballpoint Pen - Blue', office, Decimal('0.75'), Decimal('1.50'), 200, 50),
            ('FOLDER001', 'Manila Folders - Pack of 25', office, Decimal('5.99'), Decimal('9.99'), 40, 10),
            ('DRILL001', 'Cordless Drill', hardware, Decimal('89.99'), Decimal('149.99'), 12, 3),
            ('HAMMER001', 'Claw Hammer', hardware, Decimal('15.99'), Decimal('24.99'), 20, 5),
            ('SCREWS001', 'Wood Screws - Assorted', hardware, Decimal('8.99'), Decimal('14.99'), 35, 10),
            ('ANTIVIRUS001', 'Antivirus Software License', software, Decimal('39.99'), Decimal('79.99'), 50, 10),
            ('OFFICE365', 'Office 365 Subscription', software, Decimal('8.25'), Decimal('12.50'), 100, 20),
        ]
        
        for sku, name, category, cost, price, stock, reorder in products_data:
            product, created = Product.objects.get_or_create(
                sku=sku,
                defaults={
                    'name': name,
                    'category': category,
                    'cost_price': cost,
                    'selling_price': price,
                    'minimum_stock': reorder,
                    'maximum_stock': stock * 2,
                    'description': f'{name} - Quality product for business use',
                    'barcode': f"BC{sku}",  # Create unique barcode
                    'is_active': True
                }
            )
            
            # Create stock movements for each product
            if created:
                StockMovement.objects.create(
                    product=product,
                    movement_type='IN',
                    quantity_change=stock,
                    reference_number='INIT-STOCK',
                    notes='Initial stock entry',
                    created_by=None
                )

    def create_customer_data(self):
        """Create customer data"""
        self.stdout.write('Creating customer data...')
        
        customers_data = [
            ('CUST001', 'ABC Corporation', 'John', 'Smith', 'john.smith@abccorp.com', '555-0101', '123 Business Ave, City, State 12345'),
            ('CUST002', 'XYZ Enterprises', 'Sarah', 'Johnson', 'sarah@xyzent.com', '555-0102', '456 Commerce St, Town, State 12346'),
            ('CUST003', 'Tech Solutions Inc', 'Mike', 'Davis', 'mike.davis@techsol.com', '555-0103', '789 Technology Blvd, Metro, State 12347'),
            ('CUST004', 'Retail Plus', 'Lisa', 'Wilson', 'lisa@retailplus.com', '555-0104', '321 Retail Row, City, State 12348'),
            ('CUST005', 'Manufacturing Co', 'Robert', 'Brown', 'robert@mfgco.com', '555-0105', '654 Industrial Way, Factory Town, State 12349'),
            ('CUST006', 'Service First', 'Emily', 'Taylor', 'emily@servicefirst.com', '555-0106', '987 Service Lane, Downtown, State 12350'),
            ('CUST007', 'Global Imports', 'David', 'Miller', 'david@globalimports.com', '555-0107', '147 Import Plaza, Port City, State 12351'),
            ('CUST008', 'Local Store', 'Maria', 'Garcia', 'maria@localstore.com', '555-0108', '258 Main Street, Small Town, State 12352'),
        ]
        
        for code, company, first_name, last_name, email, phone, address in customers_data:
            Customer.objects.get_or_create(
                customer_id=code,
                defaults={
                    'company_name': company,
                    'contact_person': f'{first_name} {last_name}',
                    'email': email,
                    'phone': phone,
                    'address': address,
                    'city': 'Business City',
                    'postal_code': '12345',
                    'country': 'United States',
                    'is_active': True,
                    'credit_limit': Decimal('10000.00'),
                    'payment_terms': 'Net 30'
                }
            )

    def create_supplier_data(self):
        """Create supplier data"""
        self.stdout.write('Creating supplier data...')
        
        suppliers_data = [
            ('SUPP001', 'Tech Distributor Inc', 'James', 'Wilson', 'james@techdist.com', '555-1001', '100 Distribution Center, Supply City, State 12360'),
            ('SUPP002', 'Office Warehouse', 'Karen', 'Anderson', 'karen@officewarehouse.com', '555-1002', '200 Warehouse Blvd, Storage Town, State 12361'),
            ('SUPP003', 'Hardware Direct', 'Steve', 'Thompson', 'steve@hardwaredirect.com', '555-1003', '300 Hardware Ave, Tool City, State 12362'),
            ('SUPP004', 'Software Solutions', 'Nancy', 'White', 'nancy@softwaresol.com', '555-1004', '400 Software Park, Tech Valley, State 12363'),
            ('SUPP005', 'Electronics Wholesale', 'Mark', 'Lee', 'mark@electwholesale.com', '555-1005', '500 Electronics Way, Component City, State 12364'),
        ]
        
        for code, company, first_name, last_name, email, phone, address in suppliers_data:
            Supplier.objects.get_or_create(
                name=company,
                defaults={
                    'contact_person': f'{first_name} {last_name}',
                    'email': email,
                    'phone': phone,
                    'address': address,
                    'is_active': True,
                    'payment_terms': 'Net 30'
                }
            )

    def create_sales_data(self):
        """Create sales orders and invoices"""
        self.stdout.write('Creating sales data...')
        
        customers = list(Customer.objects.all())
        products = list(Product.objects.all())
        users = list(User.objects.all())
        
        # Create sales orders
        for i in range(10):
            customer = random.choice(customers)
            user = random.choice(users)
            order_date = timezone.now().date() - timedelta(days=random.randint(1, 60))
            
            order = SalesOrder.objects.create(
                order_number=f"SO-{2025:04d}-{(i+1):03d}",
                customer=customer,
                order_date=order_date,
                required_date=order_date + timedelta(days=random.randint(1, 14)),
                status=random.choice(['DRAFT', 'CONFIRMED', 'SHIPPED', 'DELIVERED']),
                created_by=user,
                notes=f"Sales order for {customer.company_name}"
            )
            
            # Add order lines
            num_lines = random.randint(1, 4)
            total_amount = Decimal('0.00')
            
            for j in range(num_lines):
                product = random.choice(products)
                quantity = random.randint(1, 10)
                unit_price = product.selling_price
                line_total = quantity * unit_price
                total_amount += line_total
                
                SalesOrderLine.objects.create(
                    sales_order=order,
                    product=product,
                    quantity=quantity,
                    unit_price=unit_price,
                    line_total=line_total
                )
            
            order.total_amount = total_amount
            order.save()
            
            # Create invoice for some orders
            if random.choice([True, False]) and order.status in ['SHIPPED', 'DELIVERED']:
                invoice_date = order.order_date + timedelta(days=random.randint(1, 7))
                due_date = invoice_date + timedelta(days=30)
                
                invoice = Invoice.objects.create(
                    invoice_number=f"INV-{2025:04d}-{(i+1):03d}",
                    sales_order=order,
                    customer=order.customer,
                    invoice_date=invoice_date,
                    due_date=due_date,
                    status=random.choice(['DRAFT', 'SENT', 'PAID']),
                    created_by=user,
                    notes=f"Invoice for sales order {order.order_number}",
                    subtotal=order.total_amount,
                    tax_amount=Decimal('0.00'),
                    total_amount=order.total_amount
                )

    def create_purchasing_data(self):
        """Create purchase orders and receipts"""
        self.stdout.write('Creating purchasing data...')
        
        suppliers = list(Supplier.objects.all())
        products = list(Product.objects.all())
        users = list(User.objects.all())
        warehouse = Warehouse.objects.get(name='Main Warehouse')
        
        # Create purchase orders
        for i in range(8):
            supplier = random.choice(suppliers)
            user = random.choice(users)
            order_date = timezone.now().date() - timedelta(days=random.randint(1, 45))
            
            po = PurchaseOrder.objects.create(
                po_number=f"PO-{2025:04d}-{(i+1):03d}",
                supplier=supplier,
                order_date=order_date,
                required_date=order_date + timedelta(days=random.randint(5, 21)),
                status=random.choice(['DRAFT', 'SENT', 'CONFIRMED', 'RECEIVED']),
                created_by=user,
                notes=f"Purchase order from {supplier.name}"
            )
            
            # Add order lines
            num_lines = random.randint(1, 3)
            total_amount = Decimal('0.00')
            
            for j in range(num_lines):
                product = random.choice(products)
                quantity = random.randint(5, 50)
                unit_cost = product.cost_price
                line_total = quantity * unit_cost
                total_amount += line_total
                
                PurchaseOrderLine.objects.create(
                    purchase_order=po,
                    product=product,
                    quantity_ordered=quantity,
                    unit_cost=unit_cost,
                    line_total=line_total
                )
            
            po.total_amount = total_amount
            po.save()
            
            # Create receipt for some orders
            if random.choice([True, False]) and po.status in ['RECEIVED']:
                receipt_date = po.order_date + timedelta(days=random.randint(3, 14))
                
                receipt = GoodsReceipt.objects.create(
                    receipt_number=f"REC-{2025:04d}-{(i+1):03d}",
                    purchase_order=po,
                    received_date=receipt_date,
                    received_by=user,
                    notes=f"Receipt for purchase order {po.po_number}"
                )
                
                # Copy order lines to receipt lines
                for po_line in po.lines.all():
                    received_qty = random.randint(int(po_line.quantity_ordered * 0.8), po_line.quantity_ordered)
                    
                    GoodsReceiptLine.objects.create(
                        goods_receipt=receipt,
                        purchase_order_line=po_line,
                        quantity_received=received_qty,
                        notes=f"Received {received_qty} of {po_line.quantity_ordered} ordered"
                    )
                    
                    # Create stock movement
                    StockMovement.objects.create(
                        product=po_line.product,
                        movement_type='IN',
                        quantity_change=received_qty,
                        reference_number=f"REC-{receipt.receipt_number}",
                        notes=f"Receipt from {po.supplier.name}",
                        created_by=user
                    )

    def create_journal_entries(self):
        """Create sample journal entries"""
        self.stdout.write('Creating journal entries...')
        
        fiscal_year = FiscalYear.objects.get(is_current=True)
        users = list(User.objects.all())
        
        # Get key accounts
        cash_account = Account.objects.get(account_number='1000')
        ar_account = Account.objects.get(account_number='1100')
        sales_account = Account.objects.get(account_number='4000')
        cogs_account = Account.objects.get(account_number='5000')
        inventory_account = Account.objects.get(account_number='1210')
        ap_account = Account.objects.get(account_number='2000')
        expense_account = Account.objects.get(account_number='6000')
        
        journal_entries_data = [
            # Sales entry
            {
                'description': 'Sales transaction - ABC Corporation',
                'reference': 'INV-2025-001',
                'lines': [
                    (ar_account, Decimal('1500.00'), Decimal('0.00'), 'Invoice to ABC Corporation'),
                    (sales_account, Decimal('0.00'), Decimal('1500.00'), 'Product sales revenue'),
                ]
            },
            # Cost of goods sold entry
            {
                'description': 'Cost of goods sold for sales',
                'reference': 'COGS-2025-001',
                'lines': [
                    (cogs_account, Decimal('900.00'), Decimal('0.00'), 'Cost of products sold'),
                    (inventory_account, Decimal('0.00'), Decimal('900.00'), 'Inventory reduction'),
                ]
            },
            # Cash receipt
            {
                'description': 'Payment received from customer',
                'reference': 'PAY-2025-001',
                'lines': [
                    (cash_account, Decimal('1500.00'), Decimal('0.00'), 'Customer payment received'),
                    (ar_account, Decimal('0.00'), Decimal('1500.00'), 'Accounts receivable payment'),
                ]
            },
            # Purchase entry
            {
                'description': 'Inventory purchase from supplier',
                'reference': 'PO-2025-001',
                'lines': [
                    (inventory_account, Decimal('2500.00'), Decimal('0.00'), 'Inventory purchase'),
                    (ap_account, Decimal('0.00'), Decimal('2500.00'), 'Amount owed to supplier'),
                ]
            },
            # Salary expense
            {
                'description': 'Monthly salary payment',
                'reference': 'PAY-2025-002',
                'lines': [
                    (expense_account, Decimal('8500.00'), Decimal('0.00'), 'Employee salaries'),
                    (cash_account, Decimal('0.00'), Decimal('8500.00'), 'Salary payment'),
                ]
            },
            # Supplier payment
            {
                'description': 'Payment to supplier for inventory',
                'reference': 'PAY-2025-003',
                'lines': [
                    (ap_account, Decimal('2500.00'), Decimal('0.00'), 'Supplier payment'),
                    (cash_account, Decimal('0.00'), Decimal('2500.00'), 'Cash payment to supplier'),
                ]
            },
        ]
        
        for i, entry_data in enumerate(journal_entries_data):
            entry_date = timezone.now().date() - timedelta(days=random.randint(1, 30))
            user = random.choice(users)
            
            # Calculate totals
            total_debit = sum(line[1] for line in entry_data['lines'])
            total_credit = sum(line[2] for line in entry_data['lines'])
            
            # Create journal entry header
            je = JournalEntryHeader.objects.create(
                entry_number=f"JE-{2025:04d}-{(i+1):03d}",
                entry_date=entry_date,
                fiscal_year=fiscal_year,
                description=entry_data['description'],
                reference=entry_data['reference'],
                total_debit=total_debit,
                total_credit=total_credit,
                is_posted=random.choice([True, False]),
                created_by=user
            )
            
            # Create journal entry lines
            for account, debit, credit, description in entry_data['lines']:
                JournalEntryDetail.objects.create(
                    journal_entry=je,
                    account=account,
                    description=description,
                    debit_amount=debit,
                    credit_amount=credit
                )
            
            # Update account balances if posted
            if je.is_posted:
                for account, debit, credit, description in entry_data['lines']:
                    if account.account_type.normal_balance == 'DEBIT':
                        account.balance += debit - credit
                    else:
                        account.balance += credit - debit
                    account.save()

        self.stdout.write(f'Created {len(journal_entries_data)} journal entries')
