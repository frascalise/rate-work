from django.shortcuts import render
from django.views.generic.detail import DetailView
from .models import Utente

# Create your views here.
class UtenteDetail(DetailView):
    model = Utente
    template_name = 'app_utente/utente_detail.html'
    