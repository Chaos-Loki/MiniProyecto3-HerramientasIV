from dataclasses import field, fields
from django import forms
# from .models import Product, Category, Review
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .choices import USER_ROLES
from .models import UserProfile

class CreateUserForm(UserCreationForm):
    
    role = forms.ChoiceField(choices=USER_ROLES, required=True)    
    
    class Meta:
        model = User
        fields = ['username','email','password1','password2', 'role']
        
    # def save(self, commit=True):
    #     user = super().save(commit=False)
    #     user_profile = UserProfile(user=user) 
    #     user_profile.role = self.cleaned_data['role']
    #     #role=self.cleaned_data['role'])
    #     if commit:             
    #         user.save()
    #         user_profile.save() 
    #     return user 