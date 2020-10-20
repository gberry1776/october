from django.shortcuts import render
from django.db import models
from django.views.generic import TemplateView

# Create your views here.

class start1(TemplateView):
    template_name = 'adventure/start1.html'

class A2(TemplateView):
    template_name= 'adventure/A2.html'
