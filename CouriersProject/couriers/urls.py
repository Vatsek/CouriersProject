from django.urls import path
from . import views


urlpatterns = [
    path('courier/add', views.courier_add, name='add_courier'),
    path('cards/add_card', views.courier_card_add, name='add_courier_card'),
    path('courier/<int:courier_id>', views.show_courier_statistics, name='show_courier_statistics'),
]
