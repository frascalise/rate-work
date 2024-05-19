from django.shortcuts import render
from django.http import HttpResponse
import logging


logger = logging.getLogger(__name__)

def home(request):
    ctx = {"lista": [1, 2, 3, 4, 5]}
    return render(request, template_name = 'home/homepage.html', context = ctx)

def welcome(request, name, age):
    return HttpResponse(f'Hello, {name}, you are {age} years old!')
