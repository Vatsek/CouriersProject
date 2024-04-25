# Generated by Django 5.0.3 on 2024-04-25 17:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('couriers', '0002_courierсard_motivation_alter_courier_phone_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courier',
            name='courier_card',
        ),
        migrations.CreateModel(
            name='CourierCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='Дата карты')),
                ('count_deliveries', models.IntegerField(default=0, verbose_name='Количество доставок')),
                ('courier', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='courier', to='couriers.courier', verbose_name='Курьер')),
            ],
        ),
        migrations.DeleteModel(
            name='CourierСard',
        ),
    ]