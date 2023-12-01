from django.urls import path
from .views import generic_views, users_views, products_views, category_views
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
    #
]