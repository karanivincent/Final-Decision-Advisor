from .forms import AssetsForm, LiabilitiesForm
from .models import Assets, Liabilities
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.
class CreateAssetsView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'assets/assets_detail.html'
    form_class = AssetsForm
    model = Assets

class AssetsUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'assets/assets_detail.html'
    template_name_suffix = '_update_form'
    form_class = AssetsForm
    model = Assets



class AssetsDetailView(DetailView):
    model = Assets

class AssetsListView(ListView):
    model = Assets

    def get_queryset(self):
        return Assets.objects.order_by('name')

class AssetsDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Assets
    success_url = reverse_lazy('assets:assets_list')



# Create your views here.
class CreateLiabilitiesView(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'assets/liabilities_detail.html'
    form_class = LiabilitiesForm
    model = Liabilities

class LiabilitiesUpdateView(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'assets/liabilities_detail.html'
    template_name_suffix = '_update_form'
    form_class = LiabilitiesForm
    model = Liabilities



class LiabilitiesDetailView(DetailView):
    model = Liabilities

class LiabilitiesListView(ListView):
    model = Liabilities

    def get_queryset(self):
        return Liabilities.objects.order_by('name')

class LiabilitiesDeleteView(LoginRequiredMixin, DeleteView):
    login_url = '/login/'
    model = Liabilities
    success_url = reverse_lazy('assets:liabilities_list')


