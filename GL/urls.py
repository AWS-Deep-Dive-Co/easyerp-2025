# General Ledger URLs
from django.urls import path
from . import views

app_name = 'gl'

urlpatterns = [
    # Dashboard
    path('', views.gl_dashboard, name='dashboard'),
    
    # Chart of Accounts
    path('accounts/', views.account_list, name='account_list'),
    path('accounts/create/', views.account_create, name='account_create'),
    path('accounts/<int:pk>/', views.account_detail, name='account_detail'),
    path('accounts/<int:pk>/edit/', views.account_edit, name='account_edit'),
    
    # Journal Entries
    path('entries/', views.journal_entry_list, name='entry_list'),
    path('entries/create/', views.journal_entry_create, name='entry_create'),
    path('entries/<uuid:pk>/', views.journal_entry_detail, name='entry_detail'),
    path('entries/<uuid:pk>/edit/', views.journal_entry_edit, name='entry_edit'),
    path('entries/<uuid:pk>/post/', views.journal_entry_post, name='entry_post'),
    
    # Reports
    path('reports/', views.reports_dashboard, name='reports_dashboard'),
    path('reports/trial-balance/', views.trial_balance, name='trial_balance'),
    path('reports/income-statement/', views.income_statement, name='income_statement'),
    path('reports/balance-sheet/', views.balance_sheet, name='balance_sheet'),
    path('reports/cash-flow-statement/', views.cash_flow_statement, name='cash_flow_statement'),
    path('reports/general-ledger/', views.general_ledger_report, name='general_ledger_report'),
    
    # Chart of Accounts
    path('chart-of-accounts/', views.chart_of_accounts, name='chart_of_accounts'),
    
    # Fiscal Year
    path('fiscal-years/', views.fiscal_year_list, name='fiscal_year_list'),
    path('fiscal-years/create/', views.fiscal_year_create, name='fiscal_year_create'),
]
