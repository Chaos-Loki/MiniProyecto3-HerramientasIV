from django.shortcuts import redirect, render
from django.urls import reverse, reverse_lazy
from django.views.decorators.cache import cache_control
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required 
# Create your views here.
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='main:login')
def chatPage(request, *args, **kwargs):
    if not request.user.is_authenticated:
        return redirect("main:login")
    context = {}
    
    return render(request, "chat/chatPage.html", context)

