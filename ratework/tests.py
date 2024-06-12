# Importa le librerie necessarie per i test
from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User
from utente.models import Utente, AnnuncioLavoro, Lavoro

class CandidaturaViewTest(TestCase):
    def setUp(self):
        # Crea un lavoratore
        self.utente = Utente.objects.create_user(username='luigi', password='testpassword', citta='reggio', is_azienda=False)
        # Crea un azienda
        self.azienda = Utente.objects.create_user(username='netflix', password='testpassword', citta='reggio', is_azienda=True)
        # Crea un annuncio di lavoro
        self.annuncio = AnnuncioLavoro.objects.create(
            azienda = self.azienda, 
            titolo="Annuncio di Test", 
            descrizione="Descrizione di test", 
            is_distanza = False, 
            is_available= True,
            range_stipendio = "1000-1200")
        # Crea un client di test
        self.client = Client()
        # Effettua il login dell'utente
        self.client.login(username='luigi', password='testpassword')

    def test_candidatura_view_get(self):
        url = reverse('candidatura', args=[self.annuncio.id])               # Ottieni l'URL della vista di candidatura
        response = self.client.get(url)                                     # Fai una richiesta GET alla vista di candidatura
        self.assertEqual(response.status_code, 200)                         # Verifica che la risposta sia 200 OK
        self.assertTemplateUsed(response, 'candidatura/candidatura.html')   # Verifica che il template corretto sia utilizzato
    
    def test_candidatura_view_post(self):
        url = reverse('candidatura', args=[self.annuncio.id])   # Ottieni l'URL della vista di candidatura
        form_data = {'conferma': True}                          # Crea un form di candidatura valido
        response = self.client.post(url, form_data)             # Fai una richiesta POST alla vista di candidatura con il form valido
        self.assertRedirects(response, reverse('home'))         # Verifica che la risposta reindirizzi alla home dopo il successo della candidatura
        self.assertTrue(Lavoro.objects.filter(annuncio=self.annuncio, lavoratore=self.utente).exists()) # Verifica che la candidatura sia stata creata nel database

    def test_candidatura_view_post_invalid_form(self):
        url = reverse('candidatura', args=[self.annuncio.id])               # Ottieni l'URL della vista di candidatura
        response = self.client.post(url, {})                                # Fai una richiesta POST alla vista di candidatura con un form vuoto (invalido)
        self.assertEqual(response.status_code, 200)                         # Verifica che la risposta sia 200 OK (form invalido -> pagina ricaricata)
        self.assertTemplateUsed(response, 'candidatura/candidatura.html')   # Verifica che il template corretto sia utilizzato
        self.assertTrue('form' in response.context)                         # Verifica che il form sia presente nel contesto della risposta (dati passati dalla view al template)
        self.assertFalse(Lavoro.objects.filter(annuncio=self.annuncio, lavoratore=self.utente).exists())  # Verifica che non sia stata creata alcuna candidatura nel database
    
    def test_annuncio_detail_view_with_invalid_id(self):
        url = reverse('candidatura', args=[self.annuncio.id + 100000000000000000000000000])  # Utilizza un ID non valido
        response = self.client.get(url)  
        self.assertEqual(response.status_code, 404)

