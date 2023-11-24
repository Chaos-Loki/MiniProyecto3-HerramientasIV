from django.urls import path
from . import views


app_name = "main"

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
]