from django.urls import path
from . import views

app_name = 'HR'

urlpatterns = [
    ######################################################################################################
    path('departments/', views.DepartmentsListView.as_view(), name='departments_list'),
    path('departments/new/', views.DepartmentsCreateView.as_view(), name='departments_new'),
    path('departments/detail/<int:pk>/', views.DepartmentsDetailView.as_view(), name='departments_detail'),
    path('departments/update/<int:pk>/', views.DepartmentsUpdateView.as_view(), name='departments_update'),
    path('departments/delete/<int:pk>/', views.DepartmentsDeleteView.as_view(), name='departments_delete'),
    ##############################################################################################################3
    path('employees/', views.EmployeeListView.as_view(), name='employee_list'),
    path('employee/new/', views.EmployeeCreateView.as_view(), name='employee_new'),
    path('employee/detail/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('employee/update/<int:pk>/', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('employee/delete/<int:pk>/', views.EmployeeDeleteView.as_view(), name='employee_delete'),
    ##########################################################################################################
    path('salaries/', views.SalariesListView.as_view(), name='salaries_list'),
    path('salaries/new/', views.SalariesCreateView.as_view(), name='salaries_new'),
    path('salaries/detail/<int:pk>/', views.SalariesDetailView.as_view(), name='salaries_detail'),
    path('salaries/update/<int:pk>/', views.SalariesUpdateView.as_view(), name='salaries_update'),
    path('salaries/delete/<int:pk>/', views.SalariesDeleteView.as_view(), name='salaries_delete'),
    ##########################################################################################################
    path('titles/', views.TitlesListView.as_view(), name='titles_list'),
    path('titles/new/', views.TitlesCreateView.as_view(), name='titles_new'),
    path('titles/detail/<int:pk>/', views.TitlesDetailView.as_view(), name='titles_detail'),
    path('titles/update/<int:pk>/', views.TitlesUpdateView.as_view(), name='titles_update'),
    path('titles/delete/<int:pk>/', views.TitlesDeleteView.as_view(), name='titles_delete'),
    ##########################################################################################################
    path('deptmanager/', views.DeptManagerListView.as_view(), name='dept_manager_list'),
    path('deptmanager/new/', views.DeptManagerCreateView.as_view(), name='dept_manager_new'),
    path('deptmanager/detail/<int:pk>/', views.DeptManagerDetailView.as_view(), name='dept_manager_detail'),
    path('deptmanager/update/<int:pk>/', views.DeptManagerUpdateView.as_view(), name='dept_manager_update'),
    path('deptmanager/delete/<int:pk>/', views.DeptManagerDeleteView.as_view(), name='dept_manager_delete'),
    ##########################################################################################################
    path('deptemployee/', views.DeptEmployeeListView.as_view(), name='dept_employee_list'),
    path('deptemployee/new/', views.DeptEmployeeCreateView.as_view(), name='dept_employee_new'),
    path('deptemployee/detail/<int:pk>/', views.DeptEmployeeDetailView.as_view(), name='dept_employee_detail'),
    path('deptemployee/update/<int:pk>/', views.DeptEmployeeUpdateView.as_view(), name='dept_employee_update'),
    path('deptemployee/delete/<int:pk>/', views.DeptEmployeeDeleteView.as_view(), name='dept_employee_delete'),
    ##########################################################################################################
    
]
