from django import forms 
from dataclasses import field, fields
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class ProductFilterForm (forms.Form):
    name = forms.CharField()


