from django import forms

class CandidaturaForm(forms.Form):
    conferma = forms.BooleanField(label='Conferma la tua candidatura')
