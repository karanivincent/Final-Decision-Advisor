from django.db import models
from django.urls import reverse

# Create your models here.
class Suppliers(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    sup_no = models.AutoField(primary_key=True, null=False)
    name = models.CharField(max_length=100)
    balance = models.IntegerField(null=True,)
    email = models.EmailField(max_length=254,null=True)
    phone = models.PositiveIntegerField(null=True)


    class Meta:
        db_table = 'suppliers'
        ordering = ['name']

    def __str__(self):
        return self.name
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("suppliers_customers:supplier_detail", kwargs={"pk": self.pk})




    #VSCode will see the objects declared
    objects = models.Manager


class Customers(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    cus_no = models.AutoField(primary_key=True, null=False)
    first_name = models.CharField(max_length=14)
    last_name = models.CharField(max_length=16, null=True) 
    ID = models.PositiveIntegerField(null = True)
    gender = models.CharField(max_length=1, null=True, choices=GENDER_CHOICES)
    balance = models.IntegerField(null=True)
    email = models.EmailField(max_length=254,null=True)
    phone = models.PositiveIntegerField(null=True)

    class Meta:
        db_table = 'customers'
        ordering = ['hire_date']

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("suppliers_customers:customers_detail", kwargs={"pk": self.pk})

    def fullname(self):
        return self.first_name + ' ' + self.last_name


    #VSCode will see the objects declared
    objects = models.Manager()