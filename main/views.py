from django.shortcuts import render
from django.contrib import messages
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, DeleteView
# from . forms import CreateUserForm, ProductPostForm, CategoryPostForm, ReviewPostForm
# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy


# Create your views here.



#Vista de Index - Defecto

class IndexView(generic.TemplateView):
        template_name = "main/index.html"

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            return context
        
        
class HomeView(generic.TemplateView):
        template_name = "main/home.html"

        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            return context
        