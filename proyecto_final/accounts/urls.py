from django.contrib.auth import logout
from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.home, name='home'),
    path('products/', views.products, name='product'),
    path('comparar/', views.comparar, name='comparar'),
    path('gastos_form/', views.crearGasto, name='gastos_form'),
    path('actualizar_gasto/<str:pk>/',views.actualizarGasto, name='actualizar_gasto'),
    path('eliminar_gasto/<str:pk>', views.eliminarGasto, name='eliminar_gasto'),
    path('registro/', views.registro, name='registro'),
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('ahorros/', views.ahorros,  name='ahorros'),
]