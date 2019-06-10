from django.shortcuts import render
from humanresource.models import (Departments, Employee,
                                Salaries, Titles,
                                DeptEmployee, DeptManager)
from django.views.generic import (CreateView, DetailView,
                                    UpdateView, DeleteView,
                                    ListView )
from django.contrib.auth.mixins import LoginRequiredMixin
from humanresource.forms import (DepartmentsForm, EmployeeForm,
                                SalariesForm, TitlesForm,
                                DeptEmployeeForm, DeptManagerForm)
from django.urls import reverse_lazy


# Create your views here.
###################################################################################

#Department Views

class DepartmentsCreateView(LoginRequiredMixin, CreateView):
    model = Departments
    login_url = '/login/'
    # redirect_field_name = 'management/department_detail.html'
    form_class = DepartmentsForm

class DepartmentsDetailView(LoginRequiredMixin, DetailView):
    model = Departments

class DepartmentsUpdateView(LoginRequiredMixin, UpdateView):
    model = Departments
    login_url = '/login/'
    form_class = DepartmentsForm
    template_name_suffix = '_update_form'


class DepartmentsDeleteView(LoginRequiredMixin, DeleteView):
    model = Departments
    success_url = reverse_lazy('management:departments_list')

class DepartmentsListView(ListView):
    model = Departments

#DeptManager views 

class DeptManagerCreateView(LoginRequiredMixin, CreateView):
    model = DeptManager
    form_class = DeptManagerForm

class DeptManagerDetailView(LoginRequiredMixin, DetailView):
    model = DeptManager

class DeptManagerUpdateView(LoginRequiredMixin, UpdateView):
    model = DeptManager
    form_class = DeptManagerForm
    template_name_suffix = '_update_form'

class DeptManagerDeleteView(LoginRequiredMixin, DeleteView):
    model = DeptManager
    success_url = reverse_lazy('management: deptmanager_list')

class DeptManagerListView(LoginRequiredMixin, ListView):
    model = DeptManager

#DeptEmployee views

class DeptEmployeeCreateView(LoginRequiredMixin, CreateView):
    model = DeptEmployee
    form_class = DeptEmployeeForm

class DeptEmployeeDetailView(LoginRequiredMixin, DetailView):
    model = DeptEmployee

class DeptEmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = DeptEmployee
    form_class = DeptEmployeeForm

class DeptEmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = DeptEmployee
    success_url = reverse_lazy('management: deptemployee_list')

class DeptEmployeeListView(LoginRequiredMixin, ListView):
    model = DeptEmployee


##############################################################################
#Employee views
class EmployeeCreateView(LoginRequiredMixin, CreateView):
    model = Employee
    form_class = EmployeeForm

class EmployeeDetailView(LoginRequiredMixin, DetailView):
    model = Employee

class EmployeeUpdateView(LoginRequiredMixin, UpdateView):
    model = Employee
    form_class = EmployeeForm
    template_name_suffix = '_update_form'


class EmployeeDeleteView(LoginRequiredMixin, DeleteView):
    model = Employee
    success_url = reverse_lazy('management:employee_list')

class EmployeeListView(LoginRequiredMixin, ListView):
    model = Employee

#######################################################################################

class SalariesCreateView(LoginRequiredMixin, CreateView):
    model = Salaries
    form_class = SalariesForm

class SalariesDetailView(LoginRequiredMixin, DetailView):
    model = Salaries

class SalariesUpdateView(LoginRequiredMixin, UpdateView):
    model = Salaries
    form_class = SalariesForm
    template_name_suffix = '_update_form'

class SalariesDeleteView(LoginRequiredMixin, DeleteView):
    model = Salaries
    success_url = reverse_lazy('management:salaries_list')

class SalariesListView(LoginRequiredMixin, ListView):
    model = Salaries

##########################################################################################

class TitlesCreateView(LoginRequiredMixin, CreateView):
    model = Titles
    form_class = TitlesForm

class TitlesDetailView(LoginRequiredMixin, DetailView):
    model = Titles

class TitlesUpdateView(LoginRequiredMixin, UpdateView):
    model = Titles
    form_class = TitlesForm
    template_name_suffix = '_update_form'

class TitlesDeleteView(LoginRequiredMixin, DeleteView):
    model = Titles
    success_url = reverse_lazy('management:titles_list')

class TitlesListView(LoginRequiredMixin, ListView):
    model = Titles