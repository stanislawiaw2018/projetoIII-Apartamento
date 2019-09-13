from django.contrib import admin
from .models import *
# Register your models here.
class ApartamentoAdmin(admin.ModelAdmin):
    list_display = ('numero', 'qtdQuartos', 'proprietario', 'valor_Condominio')


admin.site.register(Apartamento,ApartamentoAdmin)



