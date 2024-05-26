from django.shortcuts import render, redirect
from utente.models import Utente, AnnuncioLavoro, Lavoro
from django.contrib import messages
from .forms import CandidaturaForm

def home(request):
    if request.user.is_authenticated:
        utenti = Utente.objects.all()
        annunci = AnnuncioLavoro.objects.filter(is_available=True)
        utente = request.user
        hasAwork = False
        if not utente.is_azienda:
            for i in Lavoro.objects.all():
                if i.lavoratore == utente:
                    annunci = annunci.exclude(id=i.annuncio.id)
                    if i.stato == 'Accettato':
                        hasAwork = True
        return render(request, 'home/homepage.html', {'utenti': utenti, 'annunci': annunci, 'utente': utente, 'hasAwork': hasAwork})
    else:
        return render(request, 'home/homepage.html')


def Candidatura(request, id):
    if not request.user.is_authenticated:
        return redirect('home')

    utente = request.user
    lavori = Lavoro.objects.filter(lavoratore=utente)
    annuncio = AnnuncioLavoro.objects.filter(id=id)
    for i in lavori:
        if i.stato == 'Accettato':
            messages.error(request, 'Hai già un lavoro in corso')
            return redirect('home')

    if annuncio.exists() and annuncio.first().is_available and not utente.is_azienda:
        annuncio = annuncio.first()
        azienda = annuncio.azienda
        ErrorMsg = None
        successMsg = None
        
        if request.method == 'POST':
            form = CandidaturaForm(request.POST)
            if form.is_valid():
                Lavoro.objects.create(
                    annuncio=annuncio,
                    lavoratore=request.user,
                    stato='In attesa'
                )
                messages.success(request, 'Candidatura inviata con successo')
                return redirect('home')
        else:
            form = CandidaturaForm()
    else:
        annuncio = None
        azienda = None
        ErrorMsg = 'Error: 404 - Annuncio non trovato'
        successMsg = None
    
    return render(request, 'candidatura/candidatura.html', {'annuncio': annuncio, 'azienda': azienda, 'message': ErrorMsg, 'form': form, 'successMsg': successMsg})
