from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.

from .models import Client, Room, Reservation, Bill
from .forms import RoomForm, ReservationForm    
from django.template.context_processors import csrf

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
    form = RoomForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'form':form,
    }
    return render(request, 'hotel/room_create.html', context)

def hotel_update(request, id=None):
    instance = get_object_or_404(Room, id = id)
    form = RoomForm(request.POST or None, instance = instance)
    if form.is_valid():
        instance = form.save(commit = False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        'title' : "Update",
        'instance' : instance,
        'form' : form,
    }
    return render(request, 'hotel/room_create.html', context)

def hotel_delete(request):
    return HttpResponse('<h1> Delete </h1>')

def reservation_create(request):
    form = ReservationForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect('/hotel')
    context = {
        'form':form,
    }
    return render(request, 'hotel/reservation_create.html', context)