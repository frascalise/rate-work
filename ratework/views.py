from django.shortcuts import render
from django.http import HttpResponse
from app_utente.models import Utente
import logging


logger = logging.getLogger(__name__)

def home(request):
    ctx = {"utenti": Utente.objects.all()}
    return render(request, template_name = 'home/homepage.html', context = ctx)

def welcome(request, name, age):
    return HttpResponse(f'Hello, {name}, you are {age} years old!')
