from django.db import models
from django.core.validators import MinValueValidator

class Categoria(models.Model):
    nombre_categoria = models.CharField(max_length= 50,  null= True)

    def __str__(self):
        return self.nombre_categoria

class Gasto(models.Model):
    
    nombre_gasto = models.CharField(max_length=200, null=True)
    valor_gasto = models.DecimalField(max_digits=8, decimal_places=2,validators=[MinValueValidator(0.01)] ,null=True)
    fecha_gasto = models.DateField(auto_now_add=False, null= True)
    categoria = models.ForeignKey(Categoria,null=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.nombre_gasto

class Presupuesto(models.Model):
    
    valor_presupuesto = models.DecimalField(max_digits=10, decimal_places=2,null=True)
    fecha_presupuesto = models.DateField(auto_now_add=False, null= True)
    
        

