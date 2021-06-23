from django.shortcuts import render
from django.http import HttpResponse
from .forms import AgregarGasto

# Create your views here.

gastos = ['aprender django', 'estudiar', 'clases online']

def home(request):
    context = {'gastos': gastos}
    return render(request, "home/index.html", context)

def add(request):
    if request.method == 'POST':
        form = AgregarGasto(request.POST)
        #aqui lee lo que esta en el input
        if form.is_valid():
            gasto = form.cleaned_data["gasto"]
            gastos.append(gasto)
    else:
        form = AgregarGasto()
    context = {"form": form}
    return render(request, "home/add.html", context)