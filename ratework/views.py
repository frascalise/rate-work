from django.shortcuts import render
from utente.models import Utente, AnnuncioLavoro


def home(request):
    if request.user.is_authenticated:
        utenti = Utente.objects.all()
        annunci = AnnuncioLavoro.objects.all()
        utente = request.user
        return render(request, 'home/homepage.html', {'utenti': utenti, 'annunci': annunci, 'utente': utente})
    else:
        return render(request, 'home/homepage.html')

