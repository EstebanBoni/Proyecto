from django.core.validators import DecimalValidator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import FechaPrueba, GastoForm, CreateUserForm, Fecha
from .filters import GastoFilter
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
import datetime
from django.db.models import Sum

from django.contrib.auth.decorators import login_required

def loginPage(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')

    context = {}
    return render(request, 'accounts/login.html', context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def registro(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()

        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                usuario = form.cleaned_data.get('username')
                messages.success(request, 'La cuenta de '+ usuario + 'se creo correctamente')
                return redirect('login')

        context = {'form': form}
        return render(request, 'accounts/registro.html', context)

@login_required(login_url='login')
def home(request):
    actualMonth = datetime.date.today()
    gastos = Gasto.objects.filter(fecha_gasto__month=actualMonth.month, fecha_gasto__year=actualMonth.year).order_by('fecha_gasto')
    presupuesto = Presupuesto.objects.filter(fecha_presupuesto__month=actualMonth.month, fecha_presupuesto__year=actualMonth.year).order_by('fecha_presupuesto').reverse()[:1]
    #total = Gasto.objects.filter(fecha_gasto__month=actualMonth.month, fecha_gasto__year=actualMonth.year).aggregate(Sum('valor_gasto'))
    total = sum(gastos.values_list('valor_gasto', flat=True))
    restante = sum(presupuesto.values_list('valor_presupuesto', flat=True))
    restante = restante - total
    context = {'gastos':gastos, 'presupuesto':presupuesto, 'total':total, 'restante':restante}
    return render(request, 'accounts/dashboard.html',context)

@login_required(login_url='login')
def products(request):
    actualMonth = datetime.date.today()
    gastos = Gasto.objects.all().order_by('fecha_gasto')
    presupuesto = Presupuesto.objects.filter(fecha_presupuesto__month=actualMonth.month, fecha_presupuesto__year=actualMonth.year).order_by('fecha_presupuesto').reverse()[:1]
    myFilter = GastoFilter(request.GET, queryset=gastos)
    gastos = myFilter.qs
    total = sum(gastos.values_list('valor_gasto', flat=True))
    restante = sum(presupuesto.values_list('valor_presupuesto', flat=True))
    restante = restante - total
    context = {'gastos': gastos, 'myFilter':myFilter, 'total': total, 'presupuesto':presupuesto, 'restante':restante}

    return render(request, 'accounts/products.html',context)


@login_required(login_url='login')
def crearGasto(request):

    form = GastoForm()
    if request.method == 'POST':
        form = GastoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'accounts/gastos_form.html', context)

@login_required(login_url='login')
def actualizarGasto(request, pk):

    gasto = Gasto.objects.get(id=pk)
    form = GastoForm(instance=gasto)

    if request.method == 'POST':
        form = GastoForm(request.POST, instance=gasto)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form':form}
    return render(request, 'accounts/gastos_form.html', context)




@login_required(login_url='login')
def eliminarGasto(request, pk):
    gasto = Gasto.objects.get(id=pk)

    if request.method == "POST":
        gasto.delete()
        return redirect('/')

    context= {'item': gasto}
    return render (request, 'accounts/delete.html', context)

@login_required(login_url='login')
def comparar(request):
    form = Fecha()
    actualMonth = datetime.date.today()
    g = Gasto.objects.filter(fecha_gasto__month=actualMonth.month, fecha_gasto__year=actualMonth.year).order_by('fecha_gasto')
    total = sum(g.values_list('valor_gasto', flat=True))
    if request.method == "GET":
        gastos = Gasto.objects.all().order_by('fecha_gasto')
        context = {'form': form, 'gastos': gastos,'total':total}
        return render(request, 'accounts/comparar.html', context)
    if request.method == 'POST':
        form = Fecha(request.POST)
        if form.is_valid():
            fechaI = form.cleaned_data.get("inicio")
            fechaF = form.cleaned_data.get("fin")
            fechaI2 = form.cleaned_data.get("inicio2")
            fechaF2 = form.cleaned_data.get("fin2")
            if fechaI >= fechaF and fechaI2>= fechaF2:
                messages.warning(
                    request, 'La fecha inicial no puede ser igual o posterior a la final')
                #messages.info(request, 'La fecha inicial no puede ser igual o mayor a la final')
                return render(request, 'comparar.html', {'form': form})
            gastos = Gasto.objects.filter(fecha_gasto__range=[fechaI, fechaF]).order_by('fecha_gasto')
            gastos2 = Gasto.objects.filter(fecha_gasto__range=[fechaI2, fechaF2]).order_by('fecha_gasto')
            suma1 = sum(gastos.values_list('valor_gasto', flat=True))
            suma2 = sum(gastos2.values_list('valor_gasto', flat=True))

            if suma1 > suma2:
                mensaj = "Se gasto mas en el primer periodo"
            elif suma1 < suma2:
                mensaj = "Se gasto mas en el segundo periodo"
            else:
                mensaj = "Se gasto lo mismo en ambos periodos"
            diferencia = abs(suma1 - suma2)
            context = {'gastos': gastos, 'total': total, 'form': form, 'fechaF':fechaF, 
            'fechaI':fechaI, 'gastos2': gastos2, 'diferencia': diferencia, 'mensaj': mensaj,
            'suma1':suma1, 'suma2':suma2}
            
            return render(request, 'accounts/comparar.html',context)
    

@login_required(login_url='login')
def ahorros(request):
    actualMonth = datetime.date.today() + datetime.timedelta(days=10)
    gastos = Gasto.objects.filter(fecha_gasto__gt=actualMonth).order_by('fecha_gasto')
    gfecha = Gasto.objects.filter(fecha_gasto__gt=actualMonth).values_list('fecha_gasto', flat=True)
    myFilter = GastoFilter(request.GET, queryset=gastos)
    gastos = myFilter.qs
    total = sum(gastos.values_list('valor_gasto', flat=True))
    a = max(gfecha)
    delta = a - actualMonth
    ftotal = float(total)
    ftotal = round(ftotal, 2)
    ahorro = ftotal/(delta.days/30)
    ahorro = round(ahorro, 2)
    print(ahorro)

    context = {'gastos': gastos, 'myFilter':myFilter, 'ftotal': ftotal, 'ahorro': ahorro}

    return render(request, 'accounts/ahorros.html',context)


def bonos(request):
    form = FechaPrueba()
    bonos = Bono.objects.all()
    suma = 0 
    if request.method == "GET":
        context ={'bonos':bonos, 'suma':suma, 'form':form}
        return render(request, 'accounts/bonos.html', context)
    if request.method == 'POST':
        form = FechaPrueba(request.POST)
        if form.is_valid():
            fechaI = form.cleaned_data.get("inicio")
            fechaF = form.cleaned_data.get("fin")
            bonos = Bono.objects.filter(fechaBono__range=[fechaI, fechaF]).order_by('fechaBono')
            suma = sum(bonos.values_list('bono', flat=True))
            ftotal = float(suma)

            context = {'form':form, 'bonos':bonos, 'ftotal':ftotal}
            
            return render(request, 'accounts/bonos.html', context)
    

  

