from django.shortcuts import render
from django.contrib import messages
from django.views import generic
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.decorators.cache import cache_control
from main.models import (
        UserProfile,
    )

# Create your views here.

class OProfileView(generic.DetailView):
    model = UserProfile 
    template_name = "other_profile/o-profile.html"
    
    def get_object(self):
        user_id = self.kwargs.get('user_id') 
        return get_object_or_404(UserProfile, user__id=user_id)
        