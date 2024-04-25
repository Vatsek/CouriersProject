from datetime import datetime

from django import forms
from django.forms import DateField

from .models import Courier, CourierCard, Motivation


class CourierForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Введите имя'}))
    last_name = forms.CharField(max_length=30, widget=forms.TextInput(attrs={'placeholder': 'Введите фамилию'}))
    phone = forms.IntegerField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Введите номер телефона'}))

    class Meta:
        model = Courier
        exclude = []

    def __init__(self, *args, **kwargs):
        super(CourierForm, self).__init__(*args, **kwargs)
        self.fields['motivation'].required = True


class CourierCardForm(forms.ModelForm):
    class Meta:
        model = CourierCard
        exclude = []

    # widgets = {
    #     'date': forms.SelectDateWidget()}
