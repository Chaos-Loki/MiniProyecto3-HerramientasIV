from django.shortcuts import render
from django.contrib import messages
from django.views import generic
from django.views.generic import TemplateView
from main.forms import ReviewPostForm
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

#Funciones de Review
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='main:login')
def ReviewCreatePage(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = ReviewPostForm(request.POST, request.FILES)	
        if form.is_valid():
            entrada = form.save(commit=False)  # Don't save the form yet
            entrada.user = request.user  # Associate the current user with the review
            entrada.product = product  # Associate the product with the review
            entrada = form.save()
            messages.success(request, "Se añadio una nueva review!")
        else:
            messages.error(request, "Hubo un error... verifique e intentelo de nuevo.")
            form = ReviewPostForm()
    else:
        form = ReviewPostForm()
    
    context = {'form': form, 'product': product}
    return render(request, "main/Reviews/add-reviews.html", context)

#Vistas de Reviews

class ReviewView(generic.ListView):
    model = Review
    #template_name = "main/categories.html"
    #paginate_by = 5
    context_object_name = 'review'

    def get_queryset(self):
        return super().get_queryset().filter(is_active=True)

class ReviewDetailView(generic.DetailView):
    model = Review
    #template_name = "main/category.html"
    context_object_name = 'review'

#----Vista de Edicion de Reviews

class ReviewEditView (LoginRequiredMixin, UpdateView):
    model = Review
    context_object_name = 'review'
    form_class = ReviewPostForm
    template_name = 'main/Reviews/edit-reviews.html'
    success_message = 'Se edito tu review satisfactoriamente!'
    error_message = 'Hubo un error... verifique e intentelo de nuevo.'

    def get_success_url(self):
        messages.success(self.request, self.success_message)
        return reverse('main:edit-reviews', kwargs={'pk': self.object.pk})
    
    def form_invalid(self, form):
        messages.error(self.request, self.error_message)
        return reverse('main:edit-reviews', kwargs={'pk': self.object.pk})

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = self.object.product
        return context

#----Vista de Eliminacion de Reviews

class ReviewDeleteView (LoginRequiredMixin, DeleteView):
    model = Review
    context_object_name = 'review'
    template_name = 'main/Reviews/delete-reviews.html'
    success_url= reverse_lazy('main:categories')
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['product'] = self.object.product
        return context
