# Sales Module URLs
from django.urls import path
from . import views

app_name = 'sales'

urlpatterns = [
    # Dashboard
    path('', views.sales_dashboard, name='dashboard'),
    
    # Customers
    path('customers/', views.customer_list, name='customer_list'),
    path('customers/create/', views.customer_create, name='customer_create'),
    path('customers/<int:pk>/', views.customer_detail, name='customer_detail'),
    path('customers/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    
    # Sales Orders
    path('orders/', views.sales_order_list, name='order_list'),
    path('orders/create/', views.sales_order_create, name='order_create'),
    path('orders/<uuid:pk>/', views.sales_order_detail, name='order_detail'),
    path('orders/<uuid:pk>/edit/', views.sales_order_edit, name='order_edit'),
    
    # Invoices
    path('invoices/', views.invoice_list, name='invoice_list'),
    path('invoices/create/', views.invoice_create, name='invoice_create'),
    path('invoices/<uuid:pk>/', views.invoice_detail, name='invoice_detail'),
    path('invoices/<uuid:pk>/print/', views.invoice_print, name='invoice_print'),
]
