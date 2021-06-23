from django import forms

class AgregarGasto(forms.Form):
    gasto = forms.CharField()
    # si le cambias el nombre a la variable se cambia el nombre en el html