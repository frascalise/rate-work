import os
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser

# Per evitare che le immagini abbiano lo stesso nome - OK
def upload_to(instance, filename):
    username = instance.username
    timestamp = timezone.now().strftime('%Y%m%d_%H%M%S')
    filename_base, filename_ext = os.path.splitext(filename)
    new_filename = f'fotoProfilo_{username}_{timestamp}{filename_ext}'
    return os.path.join('profile_photos', new_filename)

# Modello per l'utente - OK
class Utente(AbstractUser):
    nome = models.CharField('nome', max_length=100)
    citta = models.CharField('citta', max_length=100)
    is_azienda = models.BooleanField('is_azienda', default=False)
    tag = models.CharField('tag', max_length=100, default=None, blank=True, null=True)
    immagine_profilo = models.ImageField(upload_to=upload_to, blank=True, null=True, default='profile_photos/default.jpg')

    class Meta:
        verbose_name = 'Utente'
        verbose_name_plural = 'Utenti'

# Modello per gli annunci di Lavoro - OK
class AnnuncioLavoro(models.Model):
    azienda = models.ForeignKey(Utente, on_delete=models.CASCADE)
    titolo = models.CharField('titolo', max_length=200)
    descrizione = models.TextField('descrizione')
    data_pubblicazione = models.DateTimeField('data di pubblicazione', auto_now_add=True)
    is_distanza = models.BooleanField('id_distanza', default=False)
    tag = models.CharField('tag', max_length=200, default=None, null=True)

    RANGE_STIPENDIO_CHOICES = [("1000-1200", "1000-1200"),("1200-1500", "1200-1500"),("1500-2000", "1500-2000"),("2000-2500", "2000-2500"),("2500+", "2500+")]
    range_stipendio = models.CharField('range_stipendio', max_length=50, choices=RANGE_STIPENDIO_CHOICES)

    is_available = models.BooleanField('is_available', default=True)

    class Meta:
        verbose_name = 'Annuncio di Lavoro'
        verbose_name_plural = 'Annunci di Lavoro'

# Modello per il lavoro - OK
class Lavoro(models.Model):
    annuncio = models.ForeignKey(AnnuncioLavoro, on_delete=models.CASCADE)
    lavoratore = models.ForeignKey(Utente, on_delete=models.CASCADE)
    stato = models.CharField('stato', max_length=200, choices=[('In attesa', 'In attesa'), ('Accettato', 'Accettato'), ('Rifiutato', 'Rifiutato'), ('Terminato', 'Terminato')], default='In attesa')

    class Meta:
        verbose_name = 'Lavoro'
        verbose_name_plural = 'Lavori'
    
    def getAzienda(self):
        return self.annuncio.azienda
    
    def getTitolo(self):
        return self.annuncio.titolo

# Modello per le recensioni - OK
class Recensione(models.Model):
    mittente = models.ForeignKey(Utente, on_delete=models.CASCADE, related_name='recensione_mittente')
    destinatario = models.ForeignKey(Utente, on_delete=models.CASCADE, related_name='recensione_destinatario')
    lavoro = models.ForeignKey(Lavoro, on_delete=models.CASCADE)
    data_pubblicazione = models.DateTimeField('data di pubblicazione', auto_now_add=True)
    
    POSITIVO = 1
    NEUTRO = 0
    NEGATIVO = -1
    VALUTAZIONE_CHOICES = [
        (POSITIVO, 'Positivo'),
        (NEUTRO, 'Neutro'),
        (NEGATIVO, 'Negativo'),
    ]
    valutazione = models.IntegerField('valutazione', choices=VALUTAZIONE_CHOICES)
    
    titolo = models.CharField('titolo', max_length=200)
    commento = models.TextField('commento')

    class Meta:
        verbose_name = 'Recensione'
        verbose_name_plural = 'Recensioni'
    
    def getValutazione(self):
        return dict(self.VALUTAZIONE_CHOICES)[int(self.valutazione)]