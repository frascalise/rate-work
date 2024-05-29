from django import forms
from .models import Utente, AnnuncioLavoro, Recensione
from django.contrib.auth.forms import UserCreationForm

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Username', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    
    password = forms.CharField(
        label='Password', 
        max_length=100,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

class RegistrationForm(UserCreationForm):
    username = forms.CharField(
        label='Username', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    email = forms.CharField(
        label='Email', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    nome = forms.CharField(
        label='Nome', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    password1 = forms.CharField(
        label='Password', 
        max_length=100,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    password2 = forms.CharField(
        label='Ripeti password', 
        max_length=100,
        widget=forms.PasswordInput(attrs={'class': 'form-control'})
    )

    citta = forms.CharField(
        label='Citta', 
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    is_azienda = forms.BooleanField(
        label='Seleziona se sei un azienda', 
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    class Meta:
        model = Utente
        fields = ('username', 'email', 'nome', 'password1', 'password2', 'citta', 'is_azienda')

class ModificaProfiloForm(forms.ModelForm):
    class Meta:
        model = Utente
        fields = ['nome', 'citta', 'immagine_profilo']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'citta': forms.TextInput(attrs={'class': 'form-control'}),
            'immagine_profilo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }

class AnnuncioLavoroForm(forms.ModelForm):
    titolo = forms.CharField(
        label='Titolo', 
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    descrizione = forms.CharField(
        label='Descrizione', 
        max_length=1000,
        widget=forms.Textarea(attrs={'class': 'form-control'})
    )

    is_distanza = forms.BooleanField(
        label='Seleziona se il lavoro è a distanza', 
        required=False,
        widget=forms.CheckboxInput(attrs={'class': 'form-check-input'})
    )

    range_stipendio = forms.ChoiceField(
        label='Range stipendio', 
        choices=AnnuncioLavoro.RANGE_STIPENDIO_CHOICES,
        widget=forms.Select(attrs={'class': 'form-control'})
    )

    tag = forms.CharField(
        label='tag', 
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = AnnuncioLavoro
        fields = ['titolo', 'descrizione', 'is_distanza', 'range_stipendio', 'tag']

class TagLavoratoreForm(forms.ModelForm):
    tag = forms.CharField(
        label='tag', 
        max_length=200,
        widget=forms.TextInput(attrs={'class': 'form-control'}),
        required=False,
    )

    class Meta:
        model = Utente
        fields = ['tag']

class RichiestaForm(forms.Form):
    SCELTE = [('Accetta', 'Accetta'),('Rifiuta', 'Rifiuta')]
    scelta = forms.ChoiceField(choices=SCELTE, widget=forms.RadioSelect)

class RecensioneForm(forms.ModelForm):
    valutazione = forms.ChoiceField(choices=[(1, 'Positivo'), (0, 'Neutro'), (-1, 'Negativo')], widget=forms.RadioSelect)
    
    class Meta:
        model = Recensione
        fields = ['valutazione', 'titolo', 'commento']
        widgets = {
            'titolo': forms.TextInput(attrs={'max_length': 200}),
            'commento': forms.Textarea(attrs={'max_length': 1000}),
        }