from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.

from .models import Client, Room, Reservation, Bill

def hotel_home(request):
    return HttpResponse('<h1> Home </h1>')

def hotel_detail(request, id):
    instance = get_object_or_404(Room, id=id)
    context = {
        'title': 'Detail',
        'instance' : instance,
    }
    return render(request, 'hotel/room_detail.html', context)

def hotel_list(request):
    queryset = Room.objects.all()
    context = {
        'queryset' : queryset,
        'title': 'Room list'
    }
    return render(request, 'hotel/index.html', context)

def hotel_create(request):
    return HttpResponse('<h1> Create </h1>')

def hotel_update(request):
    return HttpResponse('<h1> Update </h1>')

def hotel_delete(request):
    return HttpResponse('<h1> Delete </h1>')