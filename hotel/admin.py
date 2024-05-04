from django.contrib import admin

# Register your models here.

from .models import Client
from .models import Room
from .models import Reservation
from .models import Bill

class ClientModelAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'passport']
    list_display_links = ['first_name', 'last_name']
    search_fields = ['first_name', 'last_name', 'passport']
    list_editable = ['passport']
    class Meta:
        model = Client

admin.site.register(Client, ClientModelAdmin)


class RoomModelAdmin(admin.ModelAdmin):
    list_display = ['room_number', 'type', 'category', 'cost_per_day']
    list_display_links = ['room_number']
    list_filter = ['type', 'category', 'cost_per_day']
    search_fields = ['room_number', 'type', 'category', 'cost_per_day']
    list_editable = ['cost_per_day']
    class Meta:
        model = Room

admin.site.register(Room, RoomModelAdmin)


class ReservationModelAdmin(admin.ModelAdmin):
    list_display = ['reservation_date', 'checkin_date', 'checkout_date', 'room', 'client']
    list_display_links = ['reservation_date']
    list_filter = ['reservation_date', 'room', 'client']
    search_fields = ['reservation_date', 'checkin_date', 'checkout_date', 'room__room_number', 'client__first_name', 'client__last_name']
    class Meta:
        model = Reservation

admin.site.register(Reservation, ReservationModelAdmin)


class BillModelAdmin(admin.ModelAdmin):
    list_display = ['reservation', 'total_price']
    list_display_links = ['reservation', 'total_price']
    search_fields = ['reservation__id']
    class Meta:
        model = Bill

admin.site.register(Bill, BillModelAdmin)