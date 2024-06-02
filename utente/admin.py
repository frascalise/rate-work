from django.contrib import admin
from .models import Utente, AnnuncioLavoro, Lavoro, Recensione

# Mostra tutti i campi di utente
class UtenteAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'nome', 'tag', 'is_azienda', 'password', 'citta', 'immagine_profilo')

# Mostra tutti i campi di annuncio di lavoro
class AnnuncioLavoroAdmin(admin.ModelAdmin):
    list_display = ('titolo', 'azienda', 'data_pubblicazione', 'is_distanza', 'is_available', 'tag', 'range_stipendio')

# Mostra tutti i campi di lavoro
class LavoroAdmin(admin.ModelAdmin):
    list_display = ('annuncio', 'lavoratore', 'stato')

# Mostra tutti i campi di recensione
class RecensioneAdmin(admin.ModelAdmin):
    list_display = ('mittente', 'destinatario', 'lavoro', 'valutazione', 'titolo', 'commento')

# Register your models here. 
admin.site.register(Utente, UtenteAdmin)
admin.site.register(AnnuncioLavoro, AnnuncioLavoroAdmin)
admin.site.register(Lavoro, LavoroAdmin)
admin.site.register(Recensione, RecensioneAdmin)