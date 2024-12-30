import json
from channels.generic.websocket import AsyncWebsocketConsumer
from asgiref.sync import sync_to_async
from django.core.files.base import ContentFile
import base64
from .models import Room, Message
from django.utils.text import slugify


class ChatConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        # self.room_group_name = f'chat_{self.room_name}'
        print(f'chat_{slugify(self.room_name)}')
        self.room_group_name = f'chat_{slugify(self.room_name)}'
        
        # Join room group
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )

    async def receive(self, text_data):
        data = json.loads(text_data)
        user = self.scope['user']
        username = self.scope['user'].username
        room = await sync_to_async(Room.objects.get)(name=self.room_name)

        # التحقق إذا كانت الرسالة تحتوي على نص أو وسائط
        message = data.get('message', None)
        media_data = data.get('media', None)
        media_name = data.get('media_name', None)

        if media_data:  # معالجة الوسائط إذا كانت موجودة
            format, file_str = media_data.split(';base64,')
            file_data = ContentFile(base64.b64decode(file_str), name=media_name)
            saved_message = await sync_to_async(Message.objects.create)(
                user=user,
                room=room,
                media=file_data
            )
        else:  # إذا كانت الرسالة نصية فقط
            saved_message = await sync_to_async(Message.objects.create)(
                user=user,
                room=room,
                content=message
            )

        # إرسال الرسالة إلى المجموعة
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'message': message,
                'username': username,
                'media': saved_message.media.url if saved_message.media else None,
                'media_name': media_name if media_data else None,
            }
        )

    async def chat_message(self, event):
        # إرسال الرسالة إلى WebSocket
        await self.send(text_data=json.dumps({
            'message': event['message'],
            'username': event['username'],
            'media': event['media'],
            'media_name': event['media_name'],
        }))