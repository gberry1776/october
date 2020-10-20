from django import forms
from . import views


class GoldForm(forms.Form):
    amount = forms.DecimalField(label="",required=False,max_digits=6,decimal_places=2)
