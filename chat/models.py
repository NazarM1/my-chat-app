from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from django.utils import timezone
from django.utils.timezone import localtime
from mimetypes import guess_type

# models.py
class CustomUser(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='customuser_groups', blank=True)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_permissions', blank=True)

class Room(models.Model):
    name = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    content = models.TextField(blank=True, null=True)  # يمكن أن تكون الرسالة نصية أو بدون نص
    media = models.FileField(upload_to='chat_media/', blank=True, null=True)  # لتخزين الملفات المرف
    # timestamp = models.DateTimeField(default=timezone.now)
    timestamp = models.DateTimeField(auto_now_add=True)


    @property
    def formatted_time(self):
        return localtime(self.timestamp).strftime('%I:%M %p')

    @property
    def is_image(self):
        if self.media:
            mime_type, _ = guess_type(self.media.url)
            return mime_type and mime_type.startswith('image')
        return False

    @property
    def is_video(self):
        if self.media:
            mime_type, _ = guess_type(self.media.url)
            return mime_type and mime_type.startswith('video')
        return False

    @property
    def is_other(self):
        if self.media and not (self.is_image or self.is_video):
            return self.media.name.split('/')[-1]  # اسم الملف
        return None

    
    def __str__(self):
        if self.content:
            return f'{self.user.username}: {self.content[:30]}'
        elif self.media:
            return f'{self.user.username}: [Media]'
        return f'{self.user.username}: [Empty]'