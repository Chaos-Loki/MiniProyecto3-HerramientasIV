from django.shortcuts import render
from django.contrib import messages
from django.views import generic
from django.views.generic import TemplateView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,
)
from django.views.decorators.cache import cache_control
from django.urls import reverse
from main.models import (
        UserProfile,
        Product,
        Category,
        Review,
    )
from django.urls import reverse, reverse_lazy
from datetime import datetime
from searchfilter.filters import ProductFilter

# def SearchListView(request):
#     product_filter = ProductFilter(request.GET, queryset=Product.objects.all())
        
#     context = {
#         'form': product_filter.form,
#         'products': product_filter.qs
#     }
#     return render(request, 'searchf.html', context)

class SearchListView(generic.ListView):
    queryset=Product.objects.all()
    template_name = 'searchf.html'
    context_object_name = 'products'
    paginate_by = 7

    def get_queryset(self):
        queryset = super().get_queryset()
        self.filterset = ProductFilter(self.request.GET, queryset=queryset)
        return self.filterset.qs 
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = self.filterset.form  
        return context
    
