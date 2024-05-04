from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path("", views.hotel_list),
    path("home/", views.hotel_home),
    path("detail/<int:id>/", views.hotel_detail),
    path("create/", views.hotel_create),
    path("update/", views.hotel_update),
    path("delete/", views.hotel_delete),
]