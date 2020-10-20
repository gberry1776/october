
from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import Account

# class UserCreateForm(UserCreationForm):
#
#     class Meta:
#         fields = ('username','email','password1','password2')
#         model= get_user_model()
#
#
#
#     def __init__(self,*args,**kwargs):
#         super().__init__(*args,**kwargs)
#         self.fields['username'].label= 'Display Name'
#         self.fields['email'].label = 'Email Address'

class CustomUserCreationForm(UserCreationForm):

    class Meta:
        model = Account
        fields = ('username', 'email')

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = Account
        fields = ('username', 'email')
