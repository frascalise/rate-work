from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from utente.models import Utente, AnnuncioLavoro, Lavoro
from django.contrib import messages
from .forms import CandidaturaForm

def home(request):
    utenti = Utente.objects.all()
    if request.user.is_authenticated:
        annunci = AnnuncioLavoro.objects.filter(is_available=True)
        utente = request.user
        hasAwork = False
        
        if not utente.is_azienda:
            user_tags = set(utente.tag.split()) if utente.tag else set() # Memorizzo i tag unici dell'utente
            annunci_list = list(annunci)
            for i in Lavoro.objects.all():
                if i.lavoratore == utente:
                    annunci_list = [annuncio for annuncio in annunci_list if annuncio.id != i.annuncio.id] # Rimuovo gli annunci per cui l'utente ha già inviato una candidatura
                    if i.stato == 'Accettato':
                        hasAwork = True

            if user_tags:
                # Calcola la pertinenza basata sui tag
                def calcola_pertinenza(annuncio):
                    annuncio_tags = set(annuncio.tag.split())
                    common_tags = user_tags.intersection(annuncio_tags)
                    return len(common_tags)

                # Ordina gli annunci in base alla pertinenza
                annunci_list.sort(key=calcola_pertinenza, reverse=True)

            return render(request, 'home/homepage.html', {'utenti': utenti, 'annunci': annunci_list, 'utente': utente, 'hasAwork': hasAwork})
        else:
            return render(request, 'home/homepage.html', {'utenti': utenti, 'annunci': annunci, 'utente': utente})
    else:
        annunci = AnnuncioLavoro.objects.filter(is_available=True).order_by('?')[:8] # Prendo 8 annunci a caso
        return render(request, 'home/homepage.html', {'utenti': utenti, 'annunci': annunci, 'hasAwork': True})


def Candidatura(request, id):
    if not request.user.is_authenticated:
        return redirect('home')
    
    form = CandidaturaForm()
    utente = request.user
    lavori = Lavoro.objects.filter(lavoratore=utente)
    annuncio = AnnuncioLavoro.objects.filter(id=id)

    if not annuncio.exists():
        ErrorMsg = 'Error: 404 - Annuncio non trovato'
        return HttpResponseNotFound(render(request, 'candidatura/candidatura.html', {'annuncio': annuncio, 'message': ErrorMsg, 'form': form}))
    
    for i in lavori:
        if i.stato == 'Accettato':
            messages.error(request, 'Hai già un lavoro in corso')
            return redirect('home')

    if annuncio.first().is_available and not utente.is_azienda:
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
        annuncio = None
        azienda = None
        ErrorMsg = 'Error: 404 - Annuncio non trovato'
        successMsg = None
    
    return render(request, 'candidatura/candidatura.html', {'annuncio': annuncio, 'azienda': azienda, 'message': ErrorMsg, 'form': form, 'successMsg': successMsg})


def errore_404(request):
    return HttpResponseNotFound(render(request, 'error/error.html', {'message': 'Error: 404 - Pagina non trovata'}))