from django.contrib import admin

# Register your models here.

from .models  import *

admin.site.register(Gasto)
admin.site.register(Presupuesto)
admin.site.register(Categoria)