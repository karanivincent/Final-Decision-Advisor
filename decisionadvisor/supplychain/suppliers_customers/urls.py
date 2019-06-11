from django.urls import path
from . import views

app_name = 'supplier_customers'

urlpatterns = [
    ##############################################################################################################3
    path('suppliers/', views.SupplierListView.as_view(), name='supplier_list'),
    path('supplier/new/', views.SupplierCreateView.as_view(), name='supplier_new'),
    path('supplier/detail/<int:pk>/', views.SupplierDetailView.as_view(), name='supplier_detail'),
    path('supplier/update/<int:pk>/', views.SupplierUpdateView.as_view(), name='supplier_update'),
    path('supplier/delete/<int:pk>/', views.SupplierDeleteView.as_view(), name='supplier_delete'),
    
    ##########################################################################################################
    path('customers/', views.CustomerListView.as_view(), name='customer_list'),
    path('customer/new/', views.CustomerCreateView.as_view(), name='customer_new'),
    path('customer/detail/<int:pk>/', views.CustomerDetailView.as_view(), name='customer_detail'),
    path('customer/update/<int:pk>/', views.CustomerUpdateView.as_view(), name='customer_update'),
    path('customer/delete/<int:pk>/', views.CustomerDeleteView.as_view(), name='customer_delete'),
]