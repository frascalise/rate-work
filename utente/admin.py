from django.contrib import admin
from .models import Utente, AnnuncioLavoro, Lavoro

# Mostra tutti i campi di utente
class UtenteAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'nome', 'tag', 'is_azienda', 'password')
    
class AnnuncioLavoroAdmin(admin.ModelAdmin):
    list_display = ('titolo', 'azienda', 'data_pubblicazione', 'is_distanza')

class LavoroAdmin(admin.ModelAdmin):
    list_display = ('annuncio', 'lavoratore', 'stato')

# Register your models here. 
admin.site.register(Utente, UtenteAdmin)
admin.site.register(AnnuncioLavoro, AnnuncioLavoroAdmin)
admin.site.register(Lavoro, LavoroAdmin)