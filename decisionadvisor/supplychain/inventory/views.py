from .forms import ProductForm, AccountForm
from .models import Product, Accounts
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
class CreateProductView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'inventory/product_detail.html'
    form_class = ProductForm
    model = Product

class ProductUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'inventory/product_detail.html'
    template_name_suffix = '_update_form'
    form_class = ProductForm
    model = Product


class ProductDetailView(DetailView):
    model = Product

class ProductListView(ListView):
    model = Product

    def get_queryset(self):
        return Product.objects.order_by('name')

class ProductDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Product
    success_url = reverse_lazy('products:product_list')

###############################################

class CreateAccountView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'inventory/account_detail.html'
    form_class = AccountForm
    model = Accounts

class AccountUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'inventory/account_detail.html'
    template_name_suffix = '_update_form'
    form_class = AccountForm
    model = Accounts


class AccountDetailView(DetailView):
    model = Accounts
    

class AccountListView(ListView):
    model = Accounts

    

class AccountDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Accounts
    success_url = reverse_lazy('products:account_list')





