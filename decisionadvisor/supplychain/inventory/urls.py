from django.urls import path
from . import views

app_name='products'
urlpatterns = [
    path('product/new/', views.CreateProductView.as_view(), name='product_new'),
    path('product/detail/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('product/', views.ProductListView.as_view(), name='product_list'),
    path('product/update/<int:pk>/', views.ProductUpdateView.as_view(), name='product_update'),
    path('product/delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),

    path('account/new/', views.CreateAccountView.as_view(), name='account_new'),
    path('account/detail/<int:pk>/', views.AccountDetailView.as_view(), name='account_detail'),
    path('account/', views.AccountListView.as_view(), name='account_list'),
    path('account/update/<int:pk>/', views.AccountUpdateView.as_view(), name='account_update'),
    path('account/delete/<int:pk>/', views.AccountDeleteView.as_view(), name='account_delete'),
]
