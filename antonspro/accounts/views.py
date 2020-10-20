from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView
from django.views import generic

from . import forms
# Create your views here.
class SignUp(CreateView, generic.RedirectView):

    form_class = forms.CustomUserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
