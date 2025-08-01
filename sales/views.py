# Sales Module Views
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.core.paginator import Paginator
from django.db.models import Q, Sum
from .models import Customer, SalesOrder, Invoice, SalesOrderLine
from inventory.models import Product

@login_required
def sales_dashboard(request):
    """Sales Module Dashboard"""
    context = {
        'page_title': 'Sales Dashboard',
        'total_customers': Customer.objects.filter(is_active=True).count(),
        'pending_orders': SalesOrder.objects.filter(status__in=['DRAFT', 'CONFIRMED']).count(),
        'recent_orders': SalesOrder.objects.order_by('-created_at')[:5],
        'recent_invoices': Invoice.objects.order_by('-created_at')[:5],
    }
    
    # Monthly sales stats
    try:
        from django.utils import timezone
        current_month = timezone.now().month
        context['monthly_revenue'] = Invoice.objects.filter(
            invoice_date__month=current_month,
            status='PAID'
        ).aggregate(total=Sum('total_amount'))['total'] or 0
    except:
        context['monthly_revenue'] = 0
    
    return render(request, 'sales/dashboard.html', context)

@login_required
def customer_list(request):
    """List all customers"""
    customers = Customer.objects.filter(is_active=True).order_by('company_name')
    
    # Search functionality
    search = request.GET.get('search', '')
    if search:
        customers = customers.filter(
            Q(company_name__icontains=search) |
            Q(contact_person__icontains=search) |
            Q(email__icontains=search)
        )
    
    # Pagination
    paginator = Paginator(customers, 20)
    page = request.GET.get('page')
    customers = paginator.get_page(page)
    
    context = {
        'customers': customers,
        'search': search,
        'page_title': 'Customers',
    }
    return render(request, 'sales/customer_list.html', context)

@login_required
def customer_create(request):
    """Create new customer"""
    if request.method == 'POST':
        # Handle form submission
        try:
            customer = Customer.objects.create(
                customer_id=request.POST.get('customer_id'),
                company_name=request.POST.get('company_name', ''),
                contact_person=request.POST.get('contact_person'),
                email=request.POST.get('email'),
                phone=request.POST.get('phone', ''),
                address=request.POST.get('address', ''),
                city=request.POST.get('city', ''),
                postal_code=request.POST.get('postal_code', ''),
                country=request.POST.get('country', ''),
                tax_id=request.POST.get('tax_id', ''),
                credit_limit=request.POST.get('credit_limit', 0),
                payment_terms=request.POST.get('payment_terms', 'Net 30'),
            )
            messages.success(request, f'Customer {customer.company_name} created successfully!')
            return redirect('sales:customer_list')
        except Exception as e:
            messages.error(request, f'Error creating customer: {str(e)}')
    
    context = {
        'page_title': 'Create Customer',
    }
    return render(request, 'sales/customer_form.html', context)

@login_required
def customer_detail(request, pk):
    """Customer detail view"""
    customer = get_object_or_404(Customer, pk=pk)
    orders = SalesOrder.objects.filter(customer=customer).order_by('-order_date')[:10]
    invoices = Invoice.objects.filter(customer=customer).order_by('-invoice_date')[:10]
    
    context = {
        'customer': customer,
        'orders': orders,
        'invoices': invoices,
        'page_title': f'Customer: {customer.company_name}',
    }
    return render(request, 'sales/customer_detail.html', context)

@login_required
def customer_edit(request, pk):
    """Edit customer"""
    customer = get_object_or_404(Customer, pk=pk)
    
    if request.method == 'POST':
        try:
            customer.customer_id = request.POST.get('customer_id')
            customer.company_name = request.POST.get('company_name', '')
            customer.contact_person = request.POST.get('contact_person')
            customer.email = request.POST.get('email')
            customer.phone = request.POST.get('phone', '')
            customer.address = request.POST.get('address', '')
            customer.city = request.POST.get('city', '')
            customer.postal_code = request.POST.get('postal_code', '')
            customer.country = request.POST.get('country', '')
            customer.tax_id = request.POST.get('tax_id', '')
            customer.credit_limit = request.POST.get('credit_limit', 0)
            customer.payment_terms = request.POST.get('payment_terms', 'Net 30')
            customer.save()
            
            messages.success(request, f'Customer {customer.company_name} updated successfully!')
            return redirect('sales:customer_detail', pk=pk)
        except Exception as e:
            messages.error(request, f'Error updating customer: {str(e)}')
    
    context = {
        'customer': customer,
        'page_title': f'Edit Customer: {customer.company_name}',
    }
    return render(request, 'sales/customer_form.html', context)

@login_required
def sales_order_list(request):
    """List all sales orders"""
    orders = SalesOrder.objects.order_by('-order_date')
    
    # Filter by status
    status = request.GET.get('status', '')
    if status:
        orders = orders.filter(status=status)
    
    # Search functionality
    search = request.GET.get('search', '')
    if search:
        orders = orders.filter(
            Q(order_number__icontains=search) |
            Q(customer__company_name__icontains=search)
        )
    
    # Pagination
    paginator = Paginator(orders, 20)
    page = request.GET.get('page')
    orders = paginator.get_page(page)
    
    context = {
        'orders': orders,
        'search': search,
        'status': status,
        'status_choices': SalesOrder.STATUS_CHOICES,
        'page_title': 'Sales Orders',
    }
    return render(request, 'sales/order_list.html', context)

@login_required
def sales_order_create(request):
    """Create new sales order"""
    if request.method == 'POST':
        # This is a simplified version - in real implementation, 
        # you'd want to use Django forms for better validation
        messages.info(request, 'Sales order creation feature coming soon!')
        return redirect('sales:order_list')
    
    customers = Customer.objects.filter(is_active=True)
    products = Product.objects.filter(is_active=True)
    
    context = {
        'customers': customers,
        'products': products,
        'page_title': 'Create Sales Order',
    }
    return render(request, 'sales/order_form.html', context)

@login_required
def sales_order_detail(request, pk):
    """Sales order detail view"""
    order = get_object_or_404(SalesOrder, pk=pk)
    
    context = {
        'order': order,
        'page_title': f'Sales Order: {order.order_number}',
    }
    return render(request, 'sales/order_detail.html', context)

@login_required
def sales_order_edit(request, pk):
    """Edit sales order"""
    order = get_object_or_404(SalesOrder, pk=pk)
    
    if request.method == 'POST':
        messages.info(request, 'Sales order editing feature coming soon!')
        return redirect('sales:order_detail', pk=pk)
    
    context = {
        'order': order,
        'page_title': f'Edit Sales Order: {order.order_number}',
    }
    return render(request, 'sales/order_form.html', context)

@login_required
def invoice_list(request):
    """List all invoices"""
    invoices = Invoice.objects.order_by('-invoice_date')
    
    # Filter by status
    status = request.GET.get('status', '')
    if status:
        invoices = invoices.filter(status=status)
    
    # Pagination
    paginator = Paginator(invoices, 20)
    page = request.GET.get('page')
    invoices = paginator.get_page(page)
    
    context = {
        'invoices': invoices,
        'status': status,
        'status_choices': Invoice.STATUS_CHOICES,
        'page_title': 'Invoices',
    }
    return render(request, 'sales/invoice_list.html', context)

@login_required
def invoice_create(request):
    """Create new invoice"""
    if request.method == 'POST':
        messages.info(request, 'Invoice creation feature coming soon!')
        return redirect('sales:invoice_list')
    
    context = {
        'page_title': 'Create Invoice',
    }
    return render(request, 'sales/invoice_form.html', context)

@login_required
def invoice_detail(request, pk):
    """Invoice detail view"""
    invoice = get_object_or_404(Invoice, pk=pk)
    
    context = {
        'invoice': invoice,
        'page_title': f'Invoice: {invoice.invoice_number}',
    }
    return render(request, 'sales/invoice_detail.html', context)

@login_required
def invoice_print(request, pk):
    """Print invoice"""
    invoice = get_object_or_404(Invoice, pk=pk)
    
    context = {
        'invoice': invoice,
    }
    return render(request, 'sales/invoice_print.html', context)
