from django.shortcuts import render, redirect, get_object_or_404

from bookings.forms import BookingForm
from .models import Room
from .forms import RoomForm

Room.objects.filter(capacity__isnull=True).delete()

def room_list(request):
    rooms = Room.objects.filter(is_active=True)
    return render(request, 'rooms/list.html', {'rooms': rooms})

def room_detail(request, pk):
    room = get_object_or_404(Room, pk=pk)
    form = BookingForm()  # Передаем форму в контекст
    return render(request, 'rooms/detail.html', {'room': room, 'form': form})

def room_create(request):
    if request.method == 'POST':
        form = RoomForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('rooms:list')
    else:
        form = RoomForm()
    return render(request, 'rooms/create.html', {'form': form})