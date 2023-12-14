from django.urls import path, include
from . import views

#from Chat import views as chat_views
app_name = "other-profile"

urlpatterns = [
    path("other-profile/<int:user_id>", views.OProfileView.as_view(), name="other-profile"),
]