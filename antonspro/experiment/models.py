from django.db import models
from django.utils.text import slugify
from django.urls import reverse
from django import template
register = template.Library()

# groups models.py file
# Create your models here.
from django.contrib.auth import get_user_model
User= get_user_model()

# Create your models here.

class EGroup(models.Model):
    name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(allow_unicode=True,unique=True)
    description = models.TextField(blank=True,default='')
    description_html= models.TextField(editable=False,default='',blank=True)
    members1= models.ManyToManyField(User,through='InGroup')
    judge=models.ManyToManyField(User,through='IsJudge',related_name='judges')
    goldinroom= models.DecimalField(verbose_name='goldinroom',default=0,max_digits=6,decimal_places=2,)

    def __str__(self):
        return self.name

    def save(self,*args,**kwargs):
        self.slug= slugify(self.name)

        super().save(*args,**kwargs)

    def get_absolute_url(self):
        return reverse('experiment:single1',kwargs={'slug':self.slug,'elnamo':self.slug})

    class Meta:
        ordering= ['name']

class InGroup(models.Model):
    group= models.ForeignKey(EGroup,related_name='membership',on_delete=models.CASCADE)
    user= models.ForeignKey(User,related_name='user_group',on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('group','user')

class IsJudge(models.Model):
    courtroom= models.ForeignKey(EGroup,related_name='courtroomjudge',on_delete=models.CASCADE)
    judge1= models.ForeignKey(User,related_name='judge_group',on_delete=models.CASCADE)

    def __str__(self):
        return self.judge1.username

    class Meta:
        unique_together = ('courtroom','judge1')
