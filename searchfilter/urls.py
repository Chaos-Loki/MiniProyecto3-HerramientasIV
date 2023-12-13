from django.urls import path
from . import views

app_name = "searchfilter"

urlpatterns = [
        #path('search', views.SearchListView, name="search"),
        path('search', views.SearchListView.as_view(), name="search"),

]