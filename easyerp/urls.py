"""easyerp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.contrib.auth import views as auth_views
from default import views as default_views

urlpatterns = [
    # Main ERP URLs
    path('', default_views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', default_views.user_profile, name='user_profile'),
    
    # Module URLs
    path('inventory/', include('inventory.urls')),
    path('sales/', include('sales.urls')),
    path('purchasing/', include('purchasing.urls')),
    path('gl/', include('GL.urls')),
    
    # Admin and health check
    path('admin/', admin.site.urls),
    path('health/', include('default.urls')),
    
    # Static files
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
