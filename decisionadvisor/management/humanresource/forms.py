from django import forms
from .models import (Titles, Departments,
                             Employee, Salaries,
                             DeptEmployee, DeptManager)
from bootstrap_datepicker_plus import DatePickerInput
from bootstrap4_datetime.widgets    import DateTimePicker

class DepartmentsForm(forms.ModelForm):

    class Meta():
        model = Departments
        fields = ['dept_name']

class EmployeeForm(forms.ModelForm):

    class Meta():
        model=Employee
        fields = ['first_name', 'last_name', 'gender', 'birth_date', 'hire_date']
        widgets = {
            'birth_date':forms.DateInput(attrs={'type': 'date'}),
            'hire_date':forms.DateInput(attrs={'type': 'date'})
        }

class SalariesForm(forms.ModelForm):

    class Meta():
        model = Salaries
        exclude = ['advance']      
        widgets = {
            'from_date':forms.DateInput(attrs={'type': 'date'}),
            'to_date': forms.DateInput(attrs={'type': 'date'})
        }

class TitlesForm(forms.ModelForm):

    class Meta():
        model = Titles
        fields = '__all__'
        widgets = {
            'from_date':forms.DateInput(attrs={'type': 'date'}),
            'to_date': forms.DateInput(attrs={'type': 'date'})
        }

class DeptEmployeeForm(forms.ModelForm):

    class Meta():
        model = DeptEmployee
        fields = '__all__'
        widgets = {
            'from_date':forms.DateInput(attrs={'type': 'date'}),
            'to_date': forms.DateInput(attrs={'type': 'date'})
        }


class DeptManagerForm(forms.ModelForm):
    
    class Meta():
        model = DeptManager
        fields = '__all__'
        widgets = {
            'from_date':forms.DateInput(attrs={'type': 'date'}),
            'to_date': forms.DateInput(attrs={'type': 'date'})
        }
