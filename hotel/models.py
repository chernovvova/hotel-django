from django.db import models

# Create your models here.

class Client(models.Model):
    first_name = models.CharField(max_length=200, verbose_name='Имя')
    last_name = models.CharField(max_length=200, verbose_name='Фамилия')
    passport = models.CharField(max_length=15, verbose_name='Паспорт')

    def __unicode__(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'

class Room(models.Model):
    room_number = models.IntegerField(verbose_name='Нормер комнаты')
    type = models.CharField(max_length=50, verbose_name='Тип номера')
    category = models.CharField(max_length=50, verbose_name='Категория номера')
    cost_per_day = models.IntegerField(verbose_name='Стоимость за день')

    def __unicode__(self):
        return str(self.room_number)
    
    def __str__(self):
        return str(self.room_number)
    
    class Meta:
        verbose_name = 'Комната'
        verbose_name_plural = 'Комнаты'

class Reservation(models.Model):
    reservation_date = models.DateTimeField(verbose_name='Дата брони номера')
    checkin_date = models.DateTimeField(verbose_name='Дата заезда')
    checkout_date = models.DateTimeField(verbose_name='Дата выезда')
    room = models.ForeignKey(Room, on_delete=models.CASCADE, verbose_name='Комната')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Клиент')

    def __unicode__(self):
        return str(self.id)
    
    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Бронирование'
        verbose_name_plural = 'Бронирования'

class Bill(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete=models.CASCADE, verbose_name='Номер брони')
    total_price = models.IntegerField(verbose_name='Общая сумма')

    def __unicode__(self):
        return str(self.id)
    
    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Счёт'
        verbose_name_plural = 'Счета'


