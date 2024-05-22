from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class Utente(AbstractUser):
    nome = models.CharField('nome', max_length=100)
    is_azienda = models.BooleanField('is_azienda', default=False)