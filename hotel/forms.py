from django import forms 

from .models import Room, Reservation

class RoomForm(forms.ModelForm):
    class Meta:
        model = Room
        fields = ['name', 'description', 'room_number', 'type', 'category', 'cost_per_day']

class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['reservation_date', 'checkin_date', 'checkout_date', 'room', 'client']