import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from chat.models import UserMessage
class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['conversation_id']
        self.room_group_name = f"chat_{self.room_name}"

        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        print(f"Received data: {text_data}")
        message = json.loads(text_data)
        content = message['content']

        await self.save_message(content)

        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat.message',
                'content': content
            }
        )

    async def chat_message(self, event):
        content = event['content']

        await self.send(text_data=json.dumps({
            'content': content
        }))

    @sync_to_async
    def save_message(self, content):
        # Save the message to your database
        UserMessage.objects.create(
            conversation_id=self.room_name,  
            from_user=self.scope['user'].userprofile,  # Assuming you store the user in the scope
            content=content
        )