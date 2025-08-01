# EasyERP Main Views
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.http import JsonResponse, HttpResponse
from django.db.models import Sum, Count, F
from django.utils import timezone
from datetime import datetime, timedelta

# Health check view (keep existing)
def hello_world(request):
    html = "<html><body>Hello {}!</body></html>".format('EasyERP System')
    return HttpResponse(html)

def health_check(request):
    return HttpResponse("OK")

@login_required
def dashboard(request):
    """Main ERP Dashboard"""
    context = {
        'user': request.user,
        'current_date': timezone.now().date(),
        'page_title': 'EasyERP Dashboard',
        'modules_available': True,
    }
    
    # Add basic statistics if modules are available
    try:
        from sales.models import SalesOrder, Customer, Invoice
        from purchasing.models import PurchaseOrder
        from inventory.models import Product, StockMovement
        from GL.models import JournalEntryHeader
        
        # Sales statistics
        context['sales_stats'] = {
            'total_customers': Customer.objects.filter(is_active=True).count(),
            'pending_orders': SalesOrder.objects.filter(status__in=['DRAFT', 'CONFIRMED']).count(),
            'monthly_revenue': Invoice.objects.filter(
                invoice_date__month=timezone.now().month,
                status='PAID'
            ).aggregate(total=Sum('total_amount'))['total'] or 0,
        }
        
        # Purchasing statistics
        context['purchasing_stats'] = {
            'pending_pos': PurchaseOrder.objects.filter(status__in=['DRAFT', 'SENT', 'CONFIRMED']).count(),
        }
        
        # Inventory statistics
        context['inventory_stats'] = {
            'total_products': Product.objects.filter(is_active=True).count(),
            'low_stock_items': 0,  # Simplified for now
        }
        
        # GL statistics
        context['gl_stats'] = {
            'unposted_entries': JournalEntryHeader.objects.filter(is_posted=False).count(),
        }
        
    except ImportError:
        # Modules not yet created, show basic dashboard
        context['modules_available'] = False
    
    return render(request, 'dashboard.html', context)

@login_required
def user_profile(request):
    """User profile management"""
    if request.method == 'POST':
        # Handle profile updates
        user = request.user
        user.first_name = request.POST.get('first_name', '')
        user.last_name = request.POST.get('last_name', '')
        user.email = request.POST.get('email', '')
        user.save()
        messages.success(request, 'Profile updated successfully!')
        return redirect('user_profile')
    
    return render(request, 'user_profile.html', {'user': request.user})

@login_required
def quick_stats_api(request):
    """API endpoint for dashboard quick stats"""
    try:
        from sales.models import SalesOrder
        from purchasing.models import PurchaseOrder
        from inventory.models import Product
        
        stats = {
            'sales_orders_today': SalesOrder.objects.filter(
                order_date=timezone.now().date()
            ).count(),
            'purchase_orders_pending': PurchaseOrder.objects.filter(
                status__in=['DRAFT', 'SENT']
            ).count(),
            'total_products': Product.objects.filter(is_active=True).count(),
        }
        
        return JsonResponse(stats)
    except ImportError:
        return JsonResponse({'error': 'Modules not available'})

# Module navigation helper
@login_required
def module_navigator(request):
    """Returns available modules for navigation"""
    modules = [
        {
            'name': 'General Ledger',
            'url': '/gl/',
            'icon': 'fas fa-calculator',
            'description': 'Chart of Accounts, Journal Entries, Financial Reports'
        },
        {
            'name': 'Sales',
            'url': '/sales/',
            'icon': 'fas fa-chart-line',
            'description': 'Customers, Sales Orders, Invoices'
        },
        {
            'name': 'Purchasing',
            'url': '/purchasing/',
            'icon': 'fas fa-shopping-cart',
            'description': 'Suppliers, Purchase Orders, Receipts'
        },
        {
            'name': 'Inventory',
            'url': '/inventory/',
            'icon': 'fas fa-boxes',
            'description': 'Products, Stock Management, Warehouses'
        },
    ]
    
    return render(request, 'modules.html', {'modules': modules})