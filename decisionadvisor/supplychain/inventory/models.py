from django.db import models
from django.utils.text import slugify
from django.urls import reverse

# Create your models here.
import misaka

class Product(models.Model):
    #VSCode will see the objects declared
    objects = models.Manager()

    name = models.CharField(max_length=255, unique=True)
    price = models.PositiveIntegerField()	
    quantity = models.PositiveIntegerField()
    

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('products:product_detail', kwargs={'pk':self.pk})

    class Meta:
        ordering = ['name']