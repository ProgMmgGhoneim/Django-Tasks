import string
import random

from django.db import models

from .utils import code_generator

# Create your models here.
class KirURLModel(models.Model):
    Url = models.CharField(max_length=100)
    Shortcode = models.CharField(max_length=200 , unique =True ,blank=True)
    Title = models.CharField(max_length=100,null= True ,blank =True)
    TimeCreate = models.DateTimeField(auto_now_add=True)
    Update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.Url
    def save (self,*args,**kwargs):
        self.Shortcode = code_generator()
        if 'https://' not in self.Url and '.com' not in self.Url:
            self.Url = 'https://'+self.Url+'.com'
        super(KirURLModel,self).save(*args,**kwargs)
