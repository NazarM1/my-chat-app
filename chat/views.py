# def index(request):
#     return render(request, "chat/index.html")
# def room(request, room_name):
#     return render(request, "chat/room.html", {"room_name": room_name})


from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import *

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('select_room')
        else:
            return render(request, 'login.html', {'error': 'Invalid credentials'})
    return render(request, 'login.html')

@login_required
def select_room_view(request):
    rooms = Room.objects.all()
    if request.method == 'POST':
        room_name = request.POST['room_name']
        return redirect('chat', room_name=room_name)
    return render(request, 'chat/select_room.html', {'rooms': rooms})

@login_required
def room_view(request, room_name):
    room, created = Room.objects.get_or_create(name=room_name)
    messages = Message.objects.filter(room=room).order_by('timestamp')
    return render(request, 'chat/room.html', {
        'room_name': room_name,
        'messages': messages
    })