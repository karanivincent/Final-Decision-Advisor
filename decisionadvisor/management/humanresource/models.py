from django.db import models
from django.urls import reverse

# Create your models here.
class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    emp_no = models.AutoField(primary_key=True, null=False)
    birth_date = models.DateField(null=True)
    first_name = models.CharField(max_length=14)
    last_name = models.CharField(max_length=16) 
    gender = models.CharField(max_length=1, null=True, choices=GENDER_CHOICES)
    hire_date = models.DateField(null=True)

    class Meta:
        db_table = 'employees'
        ordering = ['hire_date']

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("management:employee_detail", kwargs={"pk": self.pk})

    def fullname(self):
        return self.first_name + ' ' + self.last_name


    #VSCode will see the objects declared
    objects = models.Manager()
    

class Departments(models.Model):
    dept_no = models.AutoField(primary_key=True, null=False)
    dept_name = models.CharField(unique=True, max_length=40)
 
    class Meta:
        db_table = 'departments'

    def __str__(self):
        return self.dept_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('management:departments_detail', kwargs={'pk': self.pk})

    #VSCode will see the objects declared
    objects = models.Manager()
    
class DeptEmployee(models.Model):
    emp_no = models.OneToOneField(Employee, on_delete=models.DO_NOTHING)
    dept_no = models.ForeignKey(Departments, on_delete=models.DO_NOTHING)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null = True)

    class Meta:
        unique_together = (('emp_no', 'dept_no'),)
    def __str__(self):
        return self.emp_no + ' ' +self.dept_no
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('management:dept_employee_detail', kwargs={'pk': self.pk})

    #VSCode will see the objects declared
    objects = models.Manager()


class DeptManager(models.Model):
    dept_no = models.OneToOneField(Departments, on_delete=models.DO_NOTHING, db_column='dept_no')
    emp_no = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, db_column='emp_no')
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)

    class Meta:
        db_table = 'dept_manager'
        unique_together = (('emp_no', 'dept_no'),)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('management:dept_manager_detail', kwargs={'pk': self.pk})

    #VSCode will see the objects declared
    objects = models.Manager()
        

class Salaries(models.Model):
    emp_no = models.ForeignKey(Employee, related_name='salary', on_delete=models.DO_NOTHING, db_column='emp_no')
    amount = models.PositiveIntegerField(null=True)
    advance = models.PositiveIntegerField(null=True)
    from_date = models.DateField(null=True)
    to_date = models.DateField(null=True)

    class Meta:
        db_table = 'salaries'
        unique_together = (('emp_no', 'from_date'),)

    def __str__(self):
        return str(self.emp_no) +"'s salary from " +  str(self.from_date) + ' to '+ str(self.to_date)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('management:salaries_detail', kwargs={'pk': self.pk})

    #VSCode will see the objects declared
    objects = models.Manager()


class Titles(models.Model):
    emp_no = models.ForeignKey(Employee, related_name='title', on_delete=models.DO_NOTHING, db_column='emp_no')
    title = models.CharField(max_length=50)
    from_date = models.DateField(null=True)
    to_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'titles'
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('management:titles_detail', kwargs={'pk': self.pk})

    #VSCode will see the objects declared
    objects = models.Manager()