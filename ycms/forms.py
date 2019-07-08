from django import forms

from .models import *

from django.contrib.auth.models import User





class details_form(forms.ModelForm):

    class Meta:
        model = event_details
        fields = ('eDate', 'duration', 'vAddress', 'eType', 'fname', 'lname', 'email', 'contact', 'address')


class accounts_form(forms.ModelForm):

    class Meta:
        model = accounts
        fields = ('username', 'email', 'password')


class login_Form(forms.ModelForm):
    class Meta():
        model = login
        fields = ('username','password')
