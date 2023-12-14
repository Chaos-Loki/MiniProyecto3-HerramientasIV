from django.shortcuts import render
from django.views.decorators.cache import cache_control
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cart.models import Cart
from main.models import Product
from django.views.decorators.cache import cache_control

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='main:login')
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    
    cart_item, created = Cart.objects.get_or_create(
        user=request.user, 
        product=product  
    )

    if not created:
        cart_item.quantity += 1
        cart_item.save()

    messages.success(request, "Item added to cart")

    return redirect("cart:cart_detail")
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='main:login')
def cart_detail(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = 0
    for item in cart_items:
        total_price += item.quantity * item.product.price
    for item in cart_items:
        item.total_price = item.quantity * item.product.price 

    context = {
        "cart_items": cart_items,
        "total_price": total_price,
    }

    return render(request, "cart_detail.html", context)

@cache_control(no_cache=True, must_revalidate=True, no_store=True)
@login_required(login_url='main:login')
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, id=cart_item_id, user=request.user)

    if cart_item.user == request.user:
        if cart_item.quantity > 1: 
            cart_item.quantity -= 1
            cart_item.save()
            messages.success(request, "Reduced item quantity")
        else: 
            cart_item.delete()
            messages.success(request, "Item removed from cart")
            
    return redirect("cart:cart_detail")