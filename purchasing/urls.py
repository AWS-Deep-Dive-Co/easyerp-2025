# Purchasing Module URLs
from django.urls import path
from . import views

app_name = 'purchasing'

urlpatterns = [
    # Dashboard
    path('', views.purchasing_dashboard, name='dashboard'),
    
    # Purchase Orders
    path('orders/', views.purchase_order_list, name='order_list'),
    path('orders/create/', views.purchase_order_create, name='order_create'),
    path('orders/<uuid:pk>/', views.purchase_order_detail, name='order_detail'),
    path('orders/<uuid:pk>/edit/', views.purchase_order_edit, name='order_edit'),
    path('orders/<uuid:pk>/approve/', views.purchase_order_approve, name='order_approve'),
    
    # Goods Receipt
    path('receipts/', views.goods_receipt_list, name='receipt_list'),
    path('receipts/create/', views.goods_receipt_create, name='receipt_create'),
    path('receipts/<uuid:pk>/', views.goods_receipt_detail, name='receipt_detail'),
    
    # Suppliers (if not handled in inventory)
    path('suppliers/', views.supplier_list, name='supplier_list'),
    path('suppliers/create/', views.supplier_create, name='supplier_create'),
    path('suppliers/<int:pk>/', views.supplier_detail, name='supplier_detail'),
]
