from django.shortcuts import render
from django.contrib import messages
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, DeleteView

from main.forms import CreateUserForm
from django.contrib.auth.forms import UserCreationForm

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
from main.models import (
        UserProfile,
    )
from django.views.decorators.cache import cache_control
#---VISTAS DE SESION DE USUARIO

#Funcion de Registro
def registerPage(request):
    if request.user.is_authenticated:
        return redirect("main:home")
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Se creo una cuenta para ' + user)
                return redirect('main:login')
        context = {'form':form}
        return render(request, 'main/register.html', context)
#Funcion de Login

def loginPage(request):
    if request.user.is_authenticated:
        return redirect("main:home")
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')
            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect("main:home")
            else:
                messages.info(request, 'Usuario O contraseña es incorrecto...')
        context = {}
        return render(request, 'main/login.html', context)

#Funcion de Logout
def logoutUser(request):
    logout(request)
    return redirect('main:login')

#Vista de Perfil - mixin es usado para protegerlo

class ProfileView(LoginRequiredMixin, TemplateView):
        template_name = "main/profiles.html"
        
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            user = self.request.user
            user_profile = UserProfile.objects.get(user=user)
            context['role'] = user_profile.role
            return context
        