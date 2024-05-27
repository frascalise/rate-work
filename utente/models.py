from django.db import models
from django.contrib.auth.models import AbstractUser

# Modello per l'utente
class Utente(AbstractUser):
    nome = models.CharField('nome', max_length=100)
    citta = models.CharField('citta', max_length=100)
    is_azienda = models.BooleanField('is_azienda', default=False)
    tag = models.CharField('tag', max_length=100, default=None, blank=True, null=True)

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
    tag = models.CharField('tag', max_length=200, default=None, null=True)

    RANGE_STIPENDIO_CHOICES = [("1000-1200", "1000-1200"),("1200-1500", "1200-1500"),("1500-2000", "1500-2000"),("2000-2500", "2000-2500"),("2500+", "2500+")]
    range_stipendio = models.CharField('range_stipendio', max_length=50, choices=RANGE_STIPENDIO_CHOICES)

    is_available = models.BooleanField('is_available', default=True)

    class Meta:
        verbose_name = 'Annuncio di Lavoro'
        verbose_name_plural = 'Annunci di Lavoro'

# Modello per il lavoro
class Lavoro(models.Model):
    annuncio = models.ForeignKey(AnnuncioLavoro, on_delete=models.CASCADE, related_name='lavori')
    lavoratore = models.ForeignKey(Utente, on_delete=models.CASCADE, related_name='lavori')
    stato = models.CharField('stato', max_length=200, choices=[('In attesa', 'In attesa'), ('Accettato', 'Accettato'), ('Rifiutato', 'Rifiutato')], default='In attesa')

    class Meta:
        verbose_name = 'Lavoro'
        verbose_name_plural = 'Lavori'

class Recensione(models.Model):
    azienda = models.ForeignKey(Utente, on_delete=models.CASCADE, related_name='recensioni_azienda', limit_choices_to={'is_azienda': True})
    lavoratore = models.ForeignKey(Utente, on_delete=models.CASCADE, related_name='recensioni_lavoratore', limit_choices_to={'is_azienda': False})
    lavoro = models.ForeignKey(Lavoro, on_delete=models.CASCADE, related_name='recensioni')
    valutazione = models.IntegerField('valutazione', choices=[(1, '★'), (2, '★★'), (3, '★★★'), (4, '★★★★'), (5, '★★★★★')])
    titolo = models.CharField('titolo', max_length=200)
    commento = models.TextField('commento')

    class Meta:
        verbose_name = 'Recensione'
        verbose_name_plural = 'Recensioni'