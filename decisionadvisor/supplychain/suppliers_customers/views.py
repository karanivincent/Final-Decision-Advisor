from django.shortcuts import render
from .models import Customers, Suppliers
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import (CreateView, DetailView,
                                    UpdateView, DeleteView,
                                    ListView )
from .forms import (CustomerForm, SupplierForm)


# Create your views here.

#Suppliers views
class SupplierCreateView(LoginRequiredMixin, CreateView):
    model = Suppliers
    form_class = SupplierForm

class SupplierDetailView(LoginRequiredMixin, DetailView):
    model = Suppliers

class SupplierUpdateView(LoginRequiredMixin, UpdateView):
    model = Suppliers
    form_class = SupplierForm
    template_name_suffix = '_update_form'


class SupplierDeleteView(LoginRequiredMixin, DeleteView):
    model = Suppliers
    success_url = reverse_lazy('suppliers_customers:employee_list')

class SupplierListView(LoginRequiredMixin, ListView):
    model = Suppliers

#######################################################################################
class CustomerCreateView(LoginRequiredMixin, CreateView):
    model = Customers
    form_class = CustomerForm

class CustomerDetailView(LoginRequiredMixin, DetailView):
    model = Customers

class CustomerUpdateView(LoginRequiredMixin, UpdateView):
    model = Customers
    form_class = CustomerForm
    template_name_suffix = '_update_form'


class CustomerDeleteView(LoginRequiredMixin, DeleteView):
    model = Customers
    success_url = reverse_lazy('suppliers_customers:employee_list')

class CustomerListView(LoginRequiredMixin, ListView):
    model = Customers

#######################################################################################

