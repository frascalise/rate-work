from django.db import models


# Dopo ogni modifica:
# python manage.py makemigrations <nome_app>
# python manage.py migrate

# Create your models here.
class Utente(models.Model):
    nome = models.CharField(max_length=100)
    cognome = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Utente"
        verbose_name_plural = "Utenti"

    def getNomeCompleto(self):
        return self.nome + " " + self.cognome