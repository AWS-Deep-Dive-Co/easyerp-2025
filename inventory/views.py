# Inventory Module Views
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

@login_required
def inventory_dashboard(request):
    """Inventory Module Dashboard"""
    context = {
        'page_title': 'Inventory Dashboard',
        'module_name': 'Inventory Management',
    }
    return render(request, 'inventory/dashboard.html', context)

@login_required
def product_list(request):
    """List all products"""
    context = {
        'page_title': 'Products',
    }
    return render(request, 'inventory/product_list.html', context)

@login_required
def product_create(request):
    """Create new product"""
    messages.info(request, 'Product creation feature coming soon!')
    return render(request, 'inventory/product_form.html', {'page_title': 'Create Product'})

@login_required
def product_detail(request, pk):
    """Product detail view"""
    return render(request, 'inventory/product_detail.html', {'page_title': f'Product Details'})

@login_required
def product_edit(request, pk):
    """Edit product"""
    return render(request, 'inventory/product_form.html', {'page_title': 'Edit Product'})

@login_required
def stock_overview(request):
    """Stock overview"""
    return render(request, 'inventory/stock_overview.html', {'page_title': 'Stock Overview'})

@login_required
def stock_movement_create(request):
    """Create stock movement"""
    return render(request, 'inventory/stock_movement_form.html', {'page_title': 'Stock Movement'})

@login_required
def stock_movement_list(request):
    """List stock movements"""
    return render(request, 'inventory/stock_movement_list.html', {'page_title': 'Stock Movements'})

@login_required
def category_list(request):
    """List categories"""
    return render(request, 'inventory/category_list.html', {'page_title': 'Categories'})

@login_required
def category_create(request):
    """Create category"""
    return render(request, 'inventory/category_form.html', {'page_title': 'Create Category'})

@login_required
def supplier_list(request):
    """List suppliers"""
    return render(request, 'inventory/supplier_list.html', {'page_title': 'Suppliers'})

@login_required
def supplier_create(request):
    """Create supplier"""
    return render(request, 'inventory/supplier_form.html', {'page_title': 'Create Supplier'})

@login_required
def supplier_detail(request, pk):
    """Supplier detail"""
    return render(request, 'inventory/supplier_detail.html', {'page_title': 'Supplier Details'})

@login_required
def warehouse_list(request):
    """List warehouses"""
    return render(request, 'inventory/warehouse_list.html', {'page_title': 'Warehouses'})

@login_required
def warehouse_create(request):
    """Create warehouse"""
    return render(request, 'inventory/warehouse_form.html', {'page_title': 'Create Warehouse'})
