from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),
    path('select-room/', views.select_room_view, name='select_room'),
    path('chat/<str:room_name>/', views.room_view, name='chat')
]
