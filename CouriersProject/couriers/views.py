from django.shortcuts import render, redirect
from .forms import CourierForm, CourierCardForm
from .models import Courier, CourierCard


def courier_add(request):
    if request.method == 'POST':
        form = CourierForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('add_courier')
    else:
        form = CourierForm()
    return render(request, 'couriers/add_courier.html', {'form': form})


def courier_card_add(request):
    if request.method == 'POST':
        form = CourierCardForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('add_courier_card')
    else:
        form = CourierCardForm()
    return render(request, 'couriers/add_courier_card.html', {'form': form})

def show_courier_statistics(request, courier_id):
    courier = Courier.objects.get(pk=courier_id)
    cards = courier.cards.all()


    return render(request, 'couriers/statistics.html', {'courier': courier, 'cards': cards})




