from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import LoginForm, RegistrationForm, AnnuncioLavoroForm, TagLavoratoreForm
from .models import Utente, AnnuncioLavoro

# Utilizzo questa funzione per evitare che da loggati si possa accedere alla registrazione e al login
#def not_authenticated(user):
#    return not user.is_authenticated

@login_required(login_url='login')
def Profilo(request):
    utente = request.user
    if utente.is_azienda:
        annunci = AnnuncioLavoro.objects.filter(azienda=utente)
        if request.method == 'POST':
            form = AnnuncioLavoroForm(request.POST)
            if form.is_valid():
                annuncio = form.save(commit=False)
                annuncio.azienda = request.user
                annuncio.save()
                return redirect('profilo')  # Definisci questa vista e rotta
        else:
            form = AnnuncioLavoroForm()
        return render(request, 'utente/profilo/profilo.html', {'utente': utente, 'form': form, 'annunci': annunci})
    else:
        if request.method == 'POST':
            form = form = TagLavoratoreForm(request.POST, instance=utente)
            if form.is_valid():
                form.save()
                return redirect('profilo')
        else:
                form = TagLavoratoreForm(instance=utente)
        return render(request, 'utente/profilo/profilo.html', context={'utente': utente, 'form': form})
    

#@user_passes_test(not_authenticated, login_url='home')
def Registrazione(request):
    # Se l'utente è già loggato lo reindirizzo alla home
    if request.user.is_authenticated:
        return redirect('home')
    message = ''
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            utente = form.save()
            message = 'Utente registrato con successo'
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
