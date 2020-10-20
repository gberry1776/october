from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class GenAbout(TemplateView):
    template_name= 'about/generalabout.html'

class SuAbout(TemplateView):
    template_name= 'about/aboutsudoku.html'

class PlanetAbout(TemplateView):
    template_name= 'about/planetabout.html'
