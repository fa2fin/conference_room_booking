
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db import transaction
from django.shortcuts import get_object_or_404, redirect, render

from bookings.forms import BookingForm
from bookings.models import Booking
from rooms.models import Room

@login_required
def create_booking(request, room_id):
    room = get_object_or_404(Room, id=room_id, is_active=True)
    if request.method == 'POST':
        form = BookingForm(request.POST, initial={'room_id': room_id})
        if form.is_valid():
            try:
                with transaction.atomic():
                    booking = form.save(commit=False)
                    booking.user = request.user
                    booking.room = room
                    if booking.is_conflict():
                        messages.error(request, "Выбранное время занято.")
                        return redirect('rooms:detail', pk=room_id)
                    booking.save()
                    messages.success(request, "Бронирование создано!")
                    return redirect('bookings:list')
            except Exception as e:
                messages.error(request, f"Ошибка: {str(e)}")
        else:
            messages.error(request, "Исправьте ошибки в форме.")
    else:
        form = BookingForm(initial={'room_id': room_id})
    return render(request, 'bookings/create.html', {'form': form, 'room': room})

def booking_list(request):
    bookings = Booking.objects.filter(user=request.user)
    return render(request, 'bookings/list.html', {'bookings': bookings})

def booking_detail(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    return render(request, 'bookings/detail.html', {'booking': booking})

def cancel_booking(request, pk):
    booking = get_object_or_404(Booking, pk=pk)
    if request.user == booking.user:
        booking.delete()
    return redirect('bookings:list')