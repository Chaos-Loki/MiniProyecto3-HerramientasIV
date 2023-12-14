from django.urls import path, include
from . import chat_views
#from Chat import views as chat_views
app_name = "chat"

urlpatterns = [
    path("chat", chat_views.chatPage, name="chat-page"),
]