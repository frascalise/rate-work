from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm, AnnuncioLavoroForm, TagLavoratoreForm, RichiestaForm, RecensioneForm
from .models import Utente, AnnuncioLavoro, Lavoro, Recensione

# Utilizzo questa funzione per evitare che da loggati si possa accedere alla registrazione e al login
#def not_authenticated(user):
#    return not user.is_authenticated

@login_required(login_url='login')
def Profilo(request):
    utente = request.user
    if utente.is_azienda:
        richiesteLavoro = Lavoro.objects.filter(annuncio__azienda=utente, stato='In attesa')
        lavoriAccettati = Lavoro.objects.filter(annuncio__azienda=utente, stato='Accettato')
        annunci = AnnuncioLavoro.objects.filter(azienda=utente)
        if request.method == 'POST':
            form = AnnuncioLavoroForm(request.POST)
            if form.is_valid():
                annuncio = form.save(commit=False)
                annuncio.azienda = request.user
                annuncio.save()
                return redirect('profilo')
        else:
            form = AnnuncioLavoroForm()
        return render(request, 'utente/profilo/profilo.html', {'utente': utente, 'form': form, 'annunci': annunci, 'richiesteLavoro': richiesteLavoro, 'lavoriAccettati': lavoriAccettati})
    
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
        return render(request, 'utente/profilo/profilo.html', context={'utente': utente, 'form': form, 'lavoroUtente': lavoroUtente})
    

#@user_passes_test(not_authenticated, login_url='home')
def Registrazione(request):
    # Se l'utente è già loggato lo reindirizzo alla home
    if request.user.is_authenticated:
        return redirect('home')
        
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            utente = form.save()
            return redirect('login')
        else:
            for field in form:
                for error in field.errors:
                    messages.error(request, f"{field.label}: {error}")
            for error in form.non_field_errors():
                messages.error(request, error)
    else:
        form = RegistrationForm()

    return render(request, 'utente/registrazione/registrazione.html', {'form': form})


#@user_passes_test(not_authenticated, login_url='home')
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
            utente = authenticate(username=username, password=password)
            if utente is not None:
                login(request, utente)
                return redirect('home')
            else:
                message = 'Credenziali non valide'
        else:
            message = 'Errore nel login'
    return render(request, 'utente/login/login.html', {'form': form, 'message': message})


def Logout(request):
    logout(request)
    return redirect('home')


def ProfiloCercato(request, username):
    utenti = Utente.objects.filter(username=username)
    if utenti.exists():
        utente = utenti.first()
        Error404Msg = None
    else:
        utente = None
        Error404Msg = 'Error: 404 - Utente non trovato'
    
    return render(request, 'utente/profiloCercato/profilo.html', {'utente': utente, 'message': Error404Msg})


@login_required(login_url='login')
def Richieste(request):
    utente = request.user
    annunciUtente = AnnuncioLavoro.objects.filter(azienda=utente)
    richiesteLavoro = Lavoro.objects.filter(annuncio__in=annunciUtente, stato='In attesa')

    if request.method == 'POST':
        form = RichiestaForm(request.POST)
        lavoro_id = request.POST.get('lavoro_id')
        try:
            lavoro = Lavoro.objects.get(id=lavoro_id)
            if form.is_valid():
                scelta = form.cleaned_data['scelta']
                if scelta == 'Accetta':
                    lavoro.stato = 'Accettato'
                    lavoro.save()
                    lavoro.annuncio.is_available = False
                    # Elimina tutti gli altri lavori del lavoratore
                    Lavoro.objects.filter(lavoratore=lavoro.lavoratore).exclude(id=lavoro.id).delete()
                    
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


def RecensioneUtente(request, username):
    if request.method == 'POST':
        form = RecensioneForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = RecensioneForm()
    return render(request, 'utente/recensioneUtente/recensione.html', {'form': form})