from django.db import models
from django.contrib.auth.models import AbstractUser

# Modello per l'utente
class Utente(AbstractUser):
    nome = models.CharField('nome', max_length=100)
    citta = models.CharField('citta', max_length=100)
    is_azienda = models.BooleanField('is_azienda', default=False)

    class Meta:
        verbose_name = 'Utente'
        verbose_name_plural = 'Utenti'

# Modello per gli annunci di Lavoro
class AnnuncioLavoro(models.Model):
    azienda = models.ForeignKey(Utente, on_delete=models.CASCADE, related_name='annunci', limit_choices_to={'is_azienda': True})
    titolo = models.CharField('titolo', max_length=200)
    descrizione = models.TextField('descrizione')
    data_pubblicazione = models.DateTimeField('data di pubblicazione', auto_now_add=True)
    is_distanza = models.BooleanField('id_distanza', default=False)

    RANGE_STIPENDIO_CHOICES = [("1000-1200", "1000-1200"),("1200-1500", "1200-1500"),("1500-2000", "1500-2000"),("2000-2500", "2000-2500"),("2500+", "2500+")]
    range_stipendio = models.CharField('range_stipendio', max_length=50, choices=RANGE_STIPENDIO_CHOICES)

    class Meta:
        verbose_name = 'Annuncio di Lavoro'
        verbose_name_plural = 'Annunci di Lavoro'

