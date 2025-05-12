# Логика бронирования
from django.shortcuts import render, redirect, get_object_or_404
from .forms import BookingForm
from .models import Booking

def create_booking(request, room_id):
    if request.method == 'POST':
        form = BookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.user = request.user
            booking.room_id = room_id
            if not booking.is_conflict():
                booking.save()
                return redirect('bookings:list')
    else:
        form = BookingForm()
    return render(request, 'bookings/create.html', {'form': form})

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