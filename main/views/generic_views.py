from django.shortcuts import render
from django.contrib import messages
from django.views import generic

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse, reverse_lazy

from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,
)

from django.views.decorators.cache import cache_control

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
    