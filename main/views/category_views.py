from django.shortcuts import render
from django.contrib import messages
from django.views import generic
from django.views.generic import TemplateView
from main.forms import CategoryPostForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,
)
from django.views.decorators.cache import cache_control
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from main.models import (
        UserProfile,
        Product,
        Category,
        Review,
    )
from django.urls import reverse, reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView

#funcion de crear categoria
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='main:login')
def CategoryCreatePage(request):
    if request.method == 'POST':
        form = CategoryPostForm(request.POST, request.FILES)	
        if form.is_valid():
            entrada = form.save()
            messages.success(request, "Se añadio categoria satisfactoriamente!")
        else:
            messages.error(request, "Hubo un error... verifique e intentelo de nuevo.")
            form = CategoryPostForm()
    else:
        form = CategoryPostForm()
    return render(request, "main/Category/add-categories.html", {'form':form})

#-------------------------------------------------------------------------------------
#Vistas de Categorias

#Lista de categorias
class CategoryView(generic.ListView):
    model = Category
    template_name = "main/Category/ListCategories.html"
    paginate_by = 5
    
    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class CategoryDetailView(generic.DetailView):
    model = Category
    template_name = "main/Category/category.html"
    context_object_name = 'category'
    paginate_by = 10

#----Vista de Edicion de Categorias

class CategoryEditView (LoginRequiredMixin, UpdateView):
    model = Category
    fields = ['name', 'description', 'image']
    template_name = 'main/Category/edit-categories.html'
    success_message = 'Se edito categoria satisfactoriamente!'
    error_message = 'Hubo un error... verifique e intentelo de nuevo.'

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse('main:edit-categories', kwargs={'pk': self.object.pk})
    
    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return reverse('main:edit-categories', kwargs={'pk': self.object.pk})


#----Vista de Eliminacion de Categorias

class CategoryDeleteView (LoginRequiredMixin, DeleteView):
    model = Category
    template_name = 'main/Category/delete-categories.html'
    success_url= reverse_lazy('main:categories')