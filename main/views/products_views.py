from django.shortcuts import render
from django.contrib import messages
from django.views import generic
from django.views.generic import TemplateView
from main.forms import ProductPostForm
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
    return render(request, "main/Products/add-products.html", {'form':form})

#-------------------------------------------------------------------------------------
#Vistas de Productos

class ProductDetailView(generic.DetailView):
    model = Product
    template_name = "main/Products/product-detail.html"
    context_object_name = 'product'

class ProductListView(generic.ListView):
    model = Category
    template_name = "main/Category/category.html"
    context_object_name = 'products'
    paginate_by = 5
    

    def get_queryset(self):
        category_id = self.kwargs['category_id']
        self.category = Category.objects.get(id=category_id)
        products = Product.objects.filter(category_id=category_id)
        
        return products
        # # Paginate the queryset
        # paginator = Paginator(products, self.paginate_by)  
        # page_number = self.request.GET.get('page')
        # page_obj = paginator.get_page(page_number)
        
        # return page_obj

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category'] = self.category
        
        products = self.get_queryset()
        
        paginator = Paginator(products, self.paginate_by)  
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context['page_obj'] = page_obj
        return context
        
        # context = super().get_context_data(**kwargs)
        # context['category'] = self.category
        # page_obj = self.get_queryset()
        
        # context['page_obj'] = page_obj
        # return context

    
#----Vista de Edicion de Producto

class ProductEditView (LoginRequiredMixin, UpdateView):
    model = Product
    fields = ['name', 'description', 'details', 'image', 'price', 'category']
    template_name = 'main/Products/edit-products.html'
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
    template_name = 'main/Products/delete-products.html'
    success_url= reverse_lazy('main:categories')
    
