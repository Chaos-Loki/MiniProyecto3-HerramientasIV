from django.urls import path, include
from . import chat_views
#from Chat import views as chat_views
app_name = "chat"

urlpatterns = [
    path("redact-chat/<int:user_id>", chat_views.redactChat, name="redact-chat"),
    path('inbox/', chat_views.inbox, name='inbox'),
    path('conversation-detail/<int:pk>/', chat_views.conversation_detail, name='conversation-detail'),
]