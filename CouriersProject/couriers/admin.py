from django.contrib import admin
from .models import Courier, Motivation, CourierСard


@admin.register(Courier)
class CourierAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'phone')
    search_fields = ['first_name', 'last_name']
    search_help_text = 'Поиск по имени или фамилии'


@admin.register(Motivation)
class MotivationAdmin(admin.ModelAdmin):
    list_display = ('title', 'base_rate', 'included_deliveries', 'rate_for_delivery')


@admin.register(CourierСard)
class CourierCardAdmin(admin.ModelAdmin):
    list_display = ('date', 'courier', 'count_deliveries')
    search_fields = ['date']
    search_help_text = 'Поиск по дате'