from django import forms
from . import views
from accounts.models import Account
from django.shortcuts import render
from django.db import models


class NameForm(forms.Form):
    playername= forms.CharField(max_length=20,min_length=1,required=False)

class DropForm(forms.Form):
    drop= forms.CharField(max_length=20,min_length=1,required=False)

class ClubForm(forms.Form):
    clubm= forms.CharField(max_length=20,min_length=1,required=False)

class PairNow(forms.Form):
    round= forms.DecimalField(max_value=None,min_value=0,max_digits=6,decimal_places=2,initial=0,label='',required=False)

class APoints(forms.Form):
    p1= forms.DecimalField(max_value=2,min_value=0,max_digits=1,decimal_places=0,initial=0,label='',required="False")
    p2= forms.DecimalField(max_value=2,min_value=0,max_digits=1,decimal_places=0,initial=0,label='',required="False")

class SaveForm(forms.Form):
    update1= forms.DecimalField(max_value=None,min_value=1,max_digits=6,decimal_places=2,initial=0,label='',required=False)

class LoadForm(forms.Form):
    load1= forms.DecimalField(max_value=None,min_value=1,max_digits=6,decimal_places=2,initial=0,label='',required=False)

class ClearForm(forms.Form):
    clearit= forms.DecimalField(max_value=None,min_value=1,max_digits=6,decimal_places=2,initial=0,label='',required=False)

class ClubMemberPoints(forms.Form):
    format= forms.CharField(max_length=20,min_length=1,required=False)
