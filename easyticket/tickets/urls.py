from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('tickets/', views.ticket_list, name='ticket_list'),
    path('tickets/create/', views.ticket_create, name='ticket_create'),
    path('tickets/<str:ticket_number>/', views.ticket_detail, name='ticket_detail'),
    path('tickets/<str:ticket_number>/edit/', views.ticket_edit, name='ticket_edit'),
    path('tickets/<str:ticket_number>/comment/', views.ticket_add_comment, name='ticket_add_comment'),
    path('approvals/<int:approval_id>/update/', views.approval_update, name='approval_update'),
]
