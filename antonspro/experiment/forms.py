from django import forms
from . import views
from accounts.models import Account
from django.shortcuts import render
from django.db import models


class GoldForm(forms.Form):
    givegold= forms.DecimalField(max_value=None,min_value=0,max_digits=6,decimal_places=2)

class JudgeGold(forms.Form):
    jgold= forms.DecimalField(max_value=None,min_value=0,max_digits=6,decimal_places=2,initial=0,label='',required='False')
