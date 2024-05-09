from django.contrib import admin
from django.urls import path

from . import views

app_name = 'hotel'

urlpatterns = [
    path("", views.hotel_list),
    path("home/", views.hotel_home),
    path("detail/<int:id>/", views.hotel_detail, name='detail'),
    path("<int:id>/", views.hotel_detail, name='detail'),
    path("create/", views.hotel_create, name='create'),
    path("<int:id>/update/", views.hotel_update, name='update'),
    path("delete/", views.hotel_delete),
    path("reservation/", views.reservation_create)
]