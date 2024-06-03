from django.http import HttpResponseNotFound
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm, ModificaProfiloForm, AnnuncioLavoroForm, TagLavoratoreForm, RichiestaForm, RecensioneForm
from .models import Utente, AnnuncioLavoro, Lavoro, Recensione

# Vista per la pagina del profilo - Azienda e Lavoratore - OK
@login_required(login_url='login')
def Profilo(request):
    utente = request.user

    recensioni = Recensione.objects.filter(destinatario=utente)
    somma_recensioni = sum(recensione.valutazione for recensione in recensioni)

    # ----------- AZIENDA -----------
    if utente.is_azienda:
        richiesteLavoro = Lavoro.objects.filter(annuncio__azienda=utente, stato='In attesa')    # Per visualizzare le richieste di lavoro
        lavoriAccettati = Lavoro.objects.filter(annuncio__azienda=utente, stato='Accettato')    # Per visualizzare i dipendenti
        annunci = AnnuncioLavoro.objects.filter(azienda=utente, is_available=True)              # Per visualizzare gli annunci di lavoro in corso

        if request.method == 'POST':
            form = AnnuncioLavoroForm(request.POST)
            if form.is_valid():
                annuncio = form.save(commit=False)  # Non salvo immediatamente nel DB
                annuncio.azienda = request.user
                annuncio.save()                     # Ora salvo nel DB
                messages.success(request, 'Annuncio creato correttamente')
                return redirect('profilo')
        else:
            form = AnnuncioLavoroForm()
        return render(request, 'utente/profilo/profilo.html', 
                      {'utente': utente, 
                       'form': form, 
                       'annunci': annunci, 
                       'richiesteLavoro': richiesteLavoro, 
                       'lavoriAccettati': lavoriAccettati, 
                       'recensioni': recensioni, 
                       'somma_recensioni': somma_recensioni})
    
    # ----------- LAVORATORE -----------
    else:
        lavoroUtente = Lavoro.objects.filter(lavoratore=request.user, stato='Accettato').first()
        if request.method == 'POST':
            form = TagLavoratoreForm(request.POST, instance=utente)
            if form.is_valid():
                form.save()
                messages.success(request, 'Tag aggiornati con successo')
                return redirect('profilo')
        else:
                form = TagLavoratoreForm(instance=utente)
        return render(request, 'utente/profilo/profilo.html', {'utente': utente, 
                                                                'form': form, 
                                                                'lavoroUtente': lavoroUtente, 
                                                                'recensioni': recensioni, 
                                                                'somma_recensioni': somma_recensioni})
    
# Vista per la modifica del profilo - Azienda e Lavoratore - OK
@login_required(login_url='login')
def ModificaProfilo(request):
    if request.method == 'POST':
        form = ModificaProfiloForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profilo')
    else:
        form = ModificaProfiloForm(instance=request.user)
    return render(request, 'utente/modificaProfilo/modifica.html', {'form': form})

# Vista per la registrazione - OK
def Registrazione(request):
    # Se l'utente è già loggato lo reindirizzo alla home
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        else:
            # Controllo se ci sono dei messaggi di errore predefiniti di Django
            for field in form:
                for error in field.errors:
                    messages.error(request, f"{field.label}: {error}")
            for error in form.non_field_errors():
                messages.error(request, error)
    else:
        form = RegistrationForm()

    return render(request, 'utente/registrazione/registrazione.html', {'form': form})

# Vista per il login - OK
def Login(request):
    # Se l'utente è già loggato lo reindirizzo alla home
    if request.user.is_authenticated:
        return redirect('home')
    
    form = LoginForm(request.POST or None) 
    message = ''

    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            utente = authenticate(username=username, password=password) # Se l'utente viene autenticato viene restituito un oggetto Utente, altrimenti None
            if utente is not None:
                login(request, utente)  # Effettua il login
                return redirect('home')
            else:
                message = 'Credenziali non valide'
        else:
            message = 'Errore nel login'
    return render(request, 'utente/login/login.html', {'form': form, 'message': message})

# Vista per il logout - OK
def Logout(request):
    logout(request)
    return redirect('home')

# Vista per il profilo di un utente cercato - OK
def ProfiloCercato(request, username):
    utenti = Utente.objects.filter(username=username)
    if utenti.exists():
        utente = utenti.first()
        recensioni = Recensione.objects.filter(destinatario=utente)
        somma_recensioni = sum(recensione.valutazione for recensione in recensioni)
        Error404Msg = None
        
        if utente.is_azienda:   # Se l'utente è un'azienda allora prendo il numero di dipendenti
            dipendenti = Lavoro.objects.filter(annuncio__azienda=utente, stato='Accettato').count()
            lavoro = None
        else:                   # Se l'utente è un lavoratore allora prendo il lavoro in corso
            dipendenti = None
            if Lavoro.objects.filter(lavoratore=utente, stato='Accettato'):
                lavoro = Lavoro.objects.filter(lavoratore=utente, stato='Accettato').first()
            else:
                lavoro = None
        return render(request, 'utente/profiloCercato/profilo.html', {'utente': utente, 
                                                                      'message': Error404Msg, 
                                                                      'recensioni': recensioni, 
                                                                      'somma_recensioni': somma_recensioni, 
                                                                      'dipendenti': dipendenti, 
                                                                      'lavoro': lavoro})
    else:
        utente = None
        Error404Msg = 'Error: 404 - Utente non trovato'
        return HttpResponseNotFound(render(request, 'utente/profiloCercato/profilo.html', {'utente': utente, 'message': Error404Msg}))

# Vista per le richieste di lavoro che ha un'azienda - OK
@login_required(login_url='login')
def Richieste(request):
    utente = request.user
    annunciUtente = AnnuncioLavoro.objects.filter(azienda=utente)
    richiesteLavoro = Lavoro.objects.filter(annuncio__in=annunciUtente, stato='In attesa')  # Il campo annuncio di Lavoro deve essere uguale a uno degli annunciUtente

    if request.method == 'POST':
        form = RichiestaForm(request.POST)
        lavoro_id = request.POST.get('lavoro_id')   # Prendo l'id del lavoro dal campo hidden del form
        try:
            lavoro = Lavoro.objects.get(id=lavoro_id)

            if form.is_valid():
                scelta = form.cleaned_data['scelta']    # Prendo il dato pulito dal form
                if scelta == 'Accetta':
                    lavoro.stato = 'Accettato'
                    lavoro.annuncio.is_available = False
                    lavoro.annuncio.save()  # Salva le modifiche all'annuncio
                    lavoro.save()           # Salva le modifiche al lavoro

                    # Elimina tutte le altre richieste di lavoro del lavoratore tranne quelle con stato 'Terminato' e quella appena accettata
                    Lavoro.objects.filter(lavoratore=lavoro.lavoratore).exclude(id=lavoro.id).exclude(stato='Terminato').delete()

                    # Imposto su Rifiutato tutte le altre richieste di lavoro per quell'annuncio
                    Lavoro.objects.filter(annuncio=lavoro.annuncio).exclude(id=lavoro.id).update(stato='Rifiutato')
                    
                elif scelta == 'Rifiuta':
                    lavoro.stato = 'Rifiutato'
                    lavoro.save()

                messages.success(request, 'Richiesta accettata con successo')
                return redirect('profilo')
            
        except Lavoro.DoesNotExist:
            messages.error(request, 'ERRORE - LAVORO INESISTENTE')

    else:
        form = RichiestaForm()

    return render(request, 'utente/richiesteLavoro/richieste.html', {'richiesteLavoro': richiesteLavoro, 'form': form, 'message': messages})

# Vista per il licenziamento di un lavoratore - OK
@login_required(login_url='login')
def Licenzia(request, username):
    utente = request.user
    utenteLicenziamento = Utente.objects.filter(username=username).first()

    if not utenteLicenziamento:
        ErrorMsg = 'Error: 404 - Utente non trovato'
        return HttpResponseNotFound(render(request, 'utente/error/error.html', {'message': ErrorMsg}))

    # Se l'utente è un'azienda allora licenzio il lavoratore
    if utente.is_azienda:
        lavoro = Lavoro.objects.filter(lavoratore=utenteLicenziamento).filter(stato="Accettato").first() # Prendo il lavoro attualmente in corso
        if lavoro:
            lavoro.stato = 'Terminato'
            lavoro.save()
            messages.success(request, 'Hai licenziato ' + utenteLicenziamento.username)
        else:
            messages.error(request, 'Lavoro non trovato')

    # Se l'utente è un lavoratore allora mi licenzio
    else:
        lavoro = Lavoro.objects.filter(lavoratore=utente).filter(stato="Accettato").first() # Prendo il lavoro attualmente in corso
        if lavoro:
            lavoro.stato = 'Terminato'
            lavoro.save()
            messages.success(request, 'Ti sei licenziato')
        else:
            messages.error(request, 'Lavoro non trovato')

    return redirect('profilo')

# Vista per la recensione di un utente - OK
@login_required(login_url='login')
def RecensioneUtente(request, username):
    autoreRecensione = request.user

    # Controllo se l'utente recensito esiste
    if Utente.objects.filter(username=username).exists():
        utenteRecensito = Utente.objects.get(username=username)
    else:
        utenteRecensito = None

    # Se non esiste l'utente recensito - Se recensisco un'utente simile a me - Se recensisco me stesso
    if utenteRecensito is None:
        message = 'ERRORE - UTENTE NON TROVATO'
        return HttpResponseNotFound(render(request, 'utente/recensioneUtente/recensione.html', {'message': message}))
    elif autoreRecensione.is_azienda == utenteRecensito.is_azienda:
        message = 'ERRORE - NON PUOI RECENSIRE UN UTENTE SIMILE A TE'
        return HttpResponseNotFound(render(request, 'utente/recensioneUtente/recensione.html', {'message': message}))
    elif utenteRecensito == autoreRecensione:
        message = 'ERRORE - NON PUOI RECENSIRE TE STESSO'
        return HttpResponseNotFound(render(request, 'utente/recensioneUtente/recensione.html', {'message': message}))
    
    # Controllo se a scrivere la recensione e' un lavoratore o un'azienda e controllo che il lavoro esista
    if not autoreRecensione.is_azienda: # Lavoratore
        lavoro = Lavoro.objects.filter(annuncio__azienda=utenteRecensito, lavoratore=autoreRecensione, stato='Accettato').first()
    else: # Azienda
        lavoro = Lavoro.objects.filter(annuncio__azienda=autoreRecensione, lavoratore=utenteRecensito, stato='Accettato').first()
    
    # Controllo che l'utente recensito sia un utente con cui lavoro
    if not lavoro:
        message = 'ERRORE - NON PUOI RECENSIRE UN UTENTE CON CUI NON LAVORI'
        return HttpResponseNotFound(render(request, 'utente/recensioneUtente/recensione.html', {'message': message}))

    if request.method == 'POST':
        form = RecensioneForm(request.POST)

        if form.is_valid():
            recensione = form.save(commit = False)
            recensione.mittente = autoreRecensione
            recensione.destinatario = utenteRecensito
            
            # Prendo il lavoro in corso tra i due utenti
            if autoreRecensione.is_azienda:
                lavoro = Lavoro.objects.filter(annuncio__azienda=autoreRecensione, lavoratore=utenteRecensito, stato='Accettato').first()
            else:
                lavoro = Lavoro.objects.filter(annuncio__azienda=utenteRecensito, lavoratore=autoreRecensione, stato='Accettato').first()

            recensione.lavoro = lavoro
            recensione.save()
            return redirect('profilo')
        else:
            message = 'ERRORE - RECENSIONE NON VALIDA'
            return render(request, 'utente/recensioneUtente/recensione.html', {'message': message, 'form': form, 'utenteRecensito': utenteRecensito, 'autoreRecensione': autoreRecensione})
    else:
        form = RecensioneForm()
    return render(request, 'utente/recensioneUtente/recensione.html', {'form': form, 'message': None, 'utenteRecensito': utenteRecensito, 'autoreRecensione': autoreRecensione})

# Vista per la cancellazione di un annuncio - OK
@login_required(login_url='login')
def CancellaAnnuncio(request, id):
    annuncio = AnnuncioLavoro.objects.filter(id=id).first()
    utente = request.user
    if utente.is_azienda:
        if annuncio:
            if annuncio.azienda == utente:
                if annuncio.is_available:
                    annuncio.delete()
                    messages.success(request, 'Annuncio cancellato con successo')
            else:
                messages.error(request, "Non sei l'autore dell'annuncio")
        else:
            messages.error(request, 'Annuncio non trovato')
    else:
        messages.error(request, "Non sei un'azienda")
    return redirect('profilo')

# Vista per le pagine non trovate - OK
def errore_404(request):
    return HttpResponseNotFound(render(request, 'error/error.html', {'message': 'Error: 404 - Pagina non trovata'}))