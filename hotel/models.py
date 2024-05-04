from django.db import models

# Create your models here.

class Client(models.Model):
    first_name = models.CharField(max_length=200, verbose_name='Имя')
    last_name = models.CharField(max_length=200, verbose_name='Фамилия')
    passport = models.CharField(max_length=15, verbose_name='Паспорт')

class Room(models.Model):
    room_number = models.IntegerField(verbose_name='Нормер комнаты')
    type = models.CharField(max_length=50, verbose_name='Тип номера')
    category = models.CharField(max_length=50, verbose_name='Категория номера')
    cost_per_day = models.IntegerField(verbose_name='Стоимость за день')

class Reservation(models.Model):
    reservation_date = models.DateTimeField(verbose_name='Дата брони номера')
    checkin_date = models.DateTimeField(verbose_name='Дата заезда')
    checkout_date = models.DateTimeField(verbose_name='Дата выезда')
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

class Bill(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE)
    total_price = models.IntegerField(verbose_name='Общая сумма')


