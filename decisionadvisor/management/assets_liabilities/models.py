from django.db import models
from django.urls import reverse
from django.utils.text import slugify



# Create your models here.
class Assets(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    value = models.PositiveIntegerField()	
    purchase_date = models.DateField(null=True)
    description = models.CharField(max_length=255)
    

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
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, unique=True)
    amount = models.PositiveIntegerField()	
    due_date = models.DateField(null=True)
    description = models.CharField(max_length=255, null=True)


    

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('assets:assets_products_detail', kwargs={'pk':self.pk})

    class Meta:
        ordering = ['name']
    
    #VSCode will see the objects declared
    objects = models.Manager()
