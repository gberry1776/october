from django.db import models
from django.utils.text import slugify
from django.urls import reverse
import pickle

# Create your models here.

class Tournament(models.Model):
    name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    description = models.TextField(blank=True,default='')
    description_html= models.TextField(editable=False,default='',blank=True)
    players= []
    table=[]
    drop=[]
    tempplayers=[]
    clubmembers=[]
    round=0

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug= slugify(self.name)

        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('magicclub:swiss',kwargs={'slug':self.slug})

    class Meta:
        ordering= ['name']
