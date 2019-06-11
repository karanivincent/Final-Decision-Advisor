from django.urls import path
from . import views

app_name='products'
urlpatterns = [
    path('new/', views.CreateProductView.as_view(), name='product_new'),
    path('detail/<int:pk>/', views.ProductDetailView.as_view(), name='product_detail'),
    path('', views.ProductListView.as_view(), name='product_list'),
    path('update/<int:pk>/', views.ProductUpdateView.as_view(), name='product_update'),
    path('delete/<int:pk>/', views.ProductDeleteView.as_view(), name='product_delete'),

]
