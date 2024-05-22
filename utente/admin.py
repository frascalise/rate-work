from django.contrib import admin
from .models import Utente

# Mostra tutti i campi di utente
class UtenteAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'nome', 'is_azienda')
    

# Register your models here. 
admin.site.register(Utente, UtenteAdmin)
