from django.db import models
from main.models import UserProfile

User = UserProfile()
# Create your models here.

class Conversation(models.Model):
    user1 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user1')
    user2 = models.ForeignKey(User, on_delete=models.CASCADE, related_name='user2')
    room_name = models.CharField(max_length=255, default='EMPTY') 
    last_updated = models.DateTimeField(auto_now_add=True)

class UserMessage(models.Model):
    conversation = models.ForeignKey(Conversation, related_name='messages', on_delete=models.CASCADE)
    content = models.TextField()
    from_user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True) 