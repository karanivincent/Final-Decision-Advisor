from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
import misaka

class Product(models.Model):
    
    name = models.CharField(max_length=255, unique=True)
    quantity = models.PositiveIntegerField()
    b_price = models.PositiveIntegerField()
    description = models.CharField(max_length=255, blank=True)
    s_price = models.PositiveIntegerField(null=True, blank=True)
    expenses = models.PositiveIntegerField(null=True, blank=True)	

    

    def __str__(self):
        return self.name

    def unit_bp(self):
        return (self.b_price + self.expenses)/self.quantity
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('products:product_detail', kwargs={'pk':self.pk})

    class Meta:
        ordering = ['name']

    #VSCode will see the objects declared
    objects = models.Manager()




# class Transaction(models.Model):



# statement of financial Position
class Accounts(models.Model):
    ACCOUNT_CHOICES = (
        ('AS','Asset'),
        ('LI','Liability'),
        ('CA','Capital'),
        ('EX', 'Expense'),
    )
    account_no = models.AutoField(primary_key=True,)
    name = models.CharField(max_length=20,)
    amount = models.IntegerField()
    account_type = models.CharField(max_length=4, null=True, choices=ACCOUNT_CHOICES)
    description = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('products:account_detail', kwargs={'pk':self.pk})

    class Meta:
        ordering = ['name']

    #VSCode will see the objects declared
    objects = models.Manager()

