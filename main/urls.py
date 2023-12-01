from django.urls import path
from .views import (
    generic_views,
    users_views,
    products_views,
    category_views,
    review_views,
)

# Basicamente, cada vista estara separada para facilidad a la hora de leer codigo
# generic_views = vistas genericas para funciones genericas del sitio
# users_views = lista de vistas para el usuario
# y asi sucesivamente, basado en los nombres.
app_name = "main"

urlpatterns = [
    path('', generic_views.HomeView.as_view(), name="home"),
    path('register/', users_views.registerPage, name="register"),
    path('login/', users_views.loginPage, name="login"),
    path('logout/', users_views.logoutUser, name="logout"),
    #Profiles
    path('profiles/', users_views.ProfileView.as_view(), name="profiles"),
    #Categories
    path('categories/', category_views.CategoryView.as_view(), name="categories"),
    path('category/<int:pk>', category_views.CategoryDetailView.as_view(), name="category"),
    path('add-categories/', category_views.CategoryCreatePage, name="add-categories"),
    path('edit-categories/<int:pk>', category_views.CategoryEditView.as_view(), name="edit-categories"),
    path('delete-categories/<int:pk>', category_views.CategoryDeleteView.as_view(), name="delete-categories"),
    #Products
    path('add-products/', products_views.ProductCreatePage, name="add-products"),
    path('edit-products/<int:pk>', products_views.ProductEditView.as_view(), name="edit-products"),
    path('delete-products/<int:pk>', products_views.ProductDeleteView.as_view(), name="delete-products"),
    path('product-detail/<int:pk>', products_views.ProductDetailView.as_view(), name="product-detail"),
    #Reviews
    path('add-reviews/<int:pk>', review_views.ReviewCreatePage, name="add-reviews"),
    path('edit-reviews/<int:pk>', review_views.ReviewEditView.as_view(), name="edit-reviews"),
    path('delete-reviews/<int:pk>', review_views.ReviewDeleteView.as_view(), name="delete-reviews"),
    
    
]