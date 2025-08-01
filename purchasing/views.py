# Purchasing Module Views
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def purchasing_dashboard(request):
    """Purchasing Module Dashboard"""
    context = {
        'page_title': 'Purchasing Dashboard',
        'module_name': 'Purchasing Management',
    }
    return render(request, 'purchasing/dashboard.html', context)

@login_required
def purchase_order_list(request):
    """List all purchase orders"""
    return render(request, 'purchasing/order_list.html', {'page_title': 'Purchase Orders'})

@login_required
def purchase_order_create(request):
    """Create new purchase order"""
    messages.info(request, 'Purchase order creation feature coming soon!')
    return render(request, 'purchasing/order_form.html', {'page_title': 'Create Purchase Order'})

@login_required
def purchase_order_detail(request, pk):
    """Purchase order detail view"""
    return render(request, 'purchasing/order_detail.html', {'page_title': 'Purchase Order Details'})

@login_required
def purchase_order_edit(request, pk):
    """Edit purchase order"""
    return render(request, 'purchasing/order_form.html', {'page_title': 'Edit Purchase Order'})

@login_required
def purchase_order_approve(request, pk):
    """Approve purchase order"""
    messages.success(request, 'Purchase order approved!')
    return render(request, 'purchasing/order_detail.html', {'page_title': 'Purchase Order Details'})

@login_required
def goods_receipt_list(request):
    """List goods receipts"""
    return render(request, 'purchasing/receipt_list.html', {'page_title': 'Goods Receipts'})

@login_required
def goods_receipt_create(request):
    """Create goods receipt"""
    return render(request, 'purchasing/receipt_form.html', {'page_title': 'Create Goods Receipt'})

@login_required
def goods_receipt_detail(request, pk):
    """Goods receipt detail"""
    return render(request, 'purchasing/receipt_detail.html', {'page_title': 'Goods Receipt Details'})

@login_required
def supplier_list(request):
    """List suppliers"""
    return render(request, 'purchasing/supplier_list.html', {'page_title': 'Suppliers'})

@login_required
def supplier_create(request):
    """Create supplier"""
    return render(request, 'purchasing/supplier_form.html', {'page_title': 'Create Supplier'})

@login_required
def supplier_detail(request, pk):
    """Supplier detail"""
    return render(request, 'purchasing/supplier_detail.html', {'page_title': 'Supplier Details'})
