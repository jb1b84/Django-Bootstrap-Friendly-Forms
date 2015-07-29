from django.db import models

from myapp.fields import BSDateField

 # Create your models here.               
class Book(models.Model):    
    title = models.CharField(max_length=200)
    date_published = BSDateField(blank=True, null=True, verbose_name="Date Published")