from django.db import models
from django.forms import ModelForm, fields
from django.forms import widgets
from django.forms.widgets import DateInput
from .models import Gasto
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User


class GastoForm(ModelForm):
    class Meta:
        model = Gasto
        fields = ['nombre_gasto', 'valor_gasto', 'fecha_gasto', 'categoria']
        

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class DateInput(forms.DateInput):
    input_type =  'date'

class Fecha(forms.Form):
    inicio =  forms.DateField(required=True, label='FechaInicio', widget=DateInput)
    fin =  forms.DateField(required=True, label='FechaInicio', widget=DateInput)
    inicio2 =  forms.DateField(required=True, label='FechaInicio2', widget=DateInput)
    fin2 =  forms.DateField(required=True, label='FechaInicio2', widget=DateInput)
        
class FechaPrueba(forms.Form):
    inicio =  forms.DateField(required=True, label='FechaInicio', widget=DateInput)
    fin =  forms.DateField(required=True, label='FechaInicio', widget=DateInput)
