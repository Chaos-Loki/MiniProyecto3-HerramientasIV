from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path("cart/", views.cart_detail, name="cart_detail"),
    path("cart-remove/<int:cart_item_id>/", views.remove_from_cart, name="cart_remove"),
    path("cart-add/<int:pk>/", views.add_to_cart, name="cart-add"),
]