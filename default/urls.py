from django.urls import path

from . import views

urlpatterns = [
    path('', views.hello_world, name='index'),
    path('csrf-debug/', views.csrf_debug, name='csrf_debug'),
]