from django.shortcuts import render
from django.contrib import messages
from django.views import generic
from django.views.generic import TemplateView
from django.views.generic.edit import UpdateView, DeleteView
from .forms import CreateUserForm, ProductPostForm, CategoryPostForm, ReviewPostForm
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
from .models import (
        UserProfile,
        Product,
        Category,
        Review,
    )
from . forms import CreateUserForm, USER_ROLES
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
                role = form.cleaned_data.get('role', '')
                UserProfile.objects.update_or_create(user=user, defaults={'role': role})
                messages.success(request, 'Se creo la cuenta para ' + user)
                return redirect('main:login')
        context = {'form':form, 'roles': USER_ROLES}
        return render(request, 'main/register.html', context)

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

#------VISTAS DE PRODUCTOS

#funcion de crear producto
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='main:login')
def ProductCreatePage(request):
    if request.method == 'POST':
        form = ProductPostForm(request.POST, request.FILES)	
        if form.is_valid():
            entrada = form.save(commit=False)
            entrada.user = request.user
            entrada.save()
            messages.success(request, "Se añadio producto satisfactoriamente!")
        else:
            messages.error(request, "Hubo un error... verifique e intentelo de nuevo.")
            form = ProductPostForm()
    else:
        form = ProductPostForm()
    return render(request, "main/add-products.html", {'form':form})


class ProductView(generic.ListView):
    model = Product
    template_name = "main/store.html"

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "main/product-detail.html"
    context_object_name = 'product'

class ProductListView(generic.ListView):
    model = Product
    template_name = "product.html"
    context_object_name = 'products'
    
    def get_queryset(self):
        category_slug = self.kwargs['category_slug']
        category = Category.objects.get(slug=category_slug)
        return Product.objects.filter(category=category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        category_slug = self.kwargs['category_slug']
        context['category'] = Category.objects.get(slug=category_slug)
        return context

#----Vista de Edicion de Producto

class ProductEditView (LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['name', 'description', 'details', 'image', 'price', 'category']
    template_name = 'main/edit-products.html'
    success_message = 'Se edito producto satisfactoriamente!'
    error_message = 'Hubo un error... verifique e intentelo de nuevo.'

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse('main:edit-products', kwargs={'pk': self.object.pk})
    
    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return reverse('main:edit-products', kwargs={'pk': self.object.pk})

#----Vista de Eliminacion de Producto

class ProductDeleteView (LoginRequiredMixin, DeleteView):
    model = Product
    template_name = 'main/delete-products.html'
    success_url= reverse_lazy('main:categories')
    





















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
    
#Vista de Perfil - mixin es usado para protegerlo

class ProfileView(LoginRequiredMixin, TemplateView):
        template_name = "main/profiles.html"
        
        def get_context_data(self, **kwargs):
            context = super().get_context_data(**kwargs)
            user = self.request.user
            user_profile = UserProfile.objects.get(user=user)
            context['role'] = user_profile.role
            return context
        