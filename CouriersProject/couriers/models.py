from datetime import date
from django.db import models


class Courier(models.Model):
    first_name = models.CharField(max_length=30, verbose_name='Имя')
    last_name = models.CharField(max_length=30, verbose_name='Имя')
    phone = models.PositiveBigIntegerField(verbose_name='Номер телефона')
    motivation = models.ForeignKey('Motivation', on_delete=models.SET_NULL,
                                   null=True, default=None,
                                   related_name='courier',
                                   verbose_name=u'Мотивация')

    def __str__(self):
        return f'{self.last_name} {self.first_name}'

class Motivation(models.Model):
    title = models.CharField(max_length=30, verbose_name='Название')
    base_rate = models.PositiveIntegerField(default=0, verbose_name='Ставка за выход')
    included_deliveries = models.PositiveIntegerField(default=0, verbose_name='Кол-во включенных доставок')
    rate_for_delivery = models.PositiveIntegerField(default=0, verbose_name='Ставка за доставку')

    def __str__(self):
        return self.title


class CourierСard(models.Model):
    date = models.DateField(default=date.today(), verbose_name='Дата карты')
    count_deliveries = models.IntegerField(default=0, verbose_name='Количество доставок')
    courier = models.ForeignKey('Courier', on_delete=models.SET_NULL,
                                      null=True,
                                      related_name='courier',
                                      verbose_name='Курьер')
