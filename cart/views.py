from django.shortcuts import render

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from cart.models import Cart
from main.models import Product

@login_required
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

@login_required
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

@login_required
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