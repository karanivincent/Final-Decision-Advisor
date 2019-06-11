from django.db import models
from django.urls import reverse
from django.utils.text import slugify



# Create your models here.
class Assets(models.Model):
   
    name = models.CharField(max_length=255, unique=True)
    value = models.PositiveIntegerField()	
    PurchaseDate = models.DateField(null=True)
    

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('assets:assets_detail', kwargs={'pk':self.pk})

    class Meta:
        ordering = ['name']

    #VSCode will see the objects declared
    objects = models.Manager()

class Liabilities(models.Model):

    name = models.CharField(max_length=255, unique=True)
    amount = models.PositiveIntegerField()	
    DueDate = models.DateField(null=True)
    StartDate = models.DateField(null=True)

    

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('assets_products:assets_products_detail', kwargs={'pk':self.pk})

    class Meta:
        ordering = ['name']
    
    #VSCode will see the objects declared
    objects = models.Manager()
