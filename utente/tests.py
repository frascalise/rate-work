from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from .forms import RegistrationForm

User = get_user_model()

class UserRegistrationTest(TestCase):
    # Pagina di registrazione ritorna status code 200
    def test_registration_page_status_code(self):
        response = self.client.get(reverse('registrazione'))
        self.assertEqual(response.status_code, 200)

    # Testa la registrazione con dati validi
    def test_registration_form_valid_data(self):
        form_data = {
            'username': 'testuser1',
            'email': 'testuser@example.com',
            'nome': 'Test Nome',
            'password1': 'TestPassword123!',
            'password2': 'TestPassword123!',
            'citta': 'Test City',
            'is_azienda': False
        }
        form = RegistrationForm(data=form_data)
        self.assertTrue(form.is_valid())    # Se l'interno e' vero allora il test passa

    # Testa la registrazione con dati non validi
    def test_registration_form_invalid_data(self):
        form_data = {
            'username': 'testuser2',
            'email': 'invalid-email',
            'nome': 'Test Nome',
            'password1': 'TestPassword123!',
            'password2': 'DifferentPassword123!',
            'citta': 'Test City',
            'is_azienda': False
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())   # Se l'interno e' falso allora il test passa

    # Testa la registrazione con username già esistente
    def test_registration_form_existing_username(self):
        User.objects.create_user(username='testuser1', password='password')
        form_data = {
            'username': 'testuser1',
            'email': 'testuser@example.com',
            'nome': 'Test Nome',
            'password1': 'TestPassword123!',
            'password2': 'TestPassword123!',
            'citta': 'Test City',
            'is_azienda': False
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())   # Se l'interno e' falso allora il test passa

    # Testa la registrazione con password diverse
    def test_registration_form_non_matching_passwords(self):
        form_data = {
            'username': 'testuser3',
            'email': 'newuser@example.com',
            'nome': 'Test Nome',
            'password1': 'TestPassword123!',
            'password2': 'DifferentPassword123!',
            'citta': 'Test City',
            'is_azienda': False
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())   # Se l'interno e' falso allora il test passa
    
    # Testa la registrazione con citta vuota
    def test_registration_form_empty_city(self):
        form_data = {
            'username': 'testuser1',
            'email': 'testuser@example.com',
            'nome': 'Test Nome',
            'password1': 'TestPassword123!',
            'password2': 'TestPassword123!',
            'citta': '',
            'is_azienda': False
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())    # Se l'interno e' falso allora il test passa

    # Testa la registrazione con username vuoto
    def test_registration_form_empty_username(self):
        form_data = {
            'username': '',
            'email': 'testuser@example.com',
            'nome': 'Test Nome',
            'password1': 'TestPassword123!',
            'password2': 'TestPassword123!',
            'citta': 'Test City',
            'is_azienda': False
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())    # Se l'interno e' falso allora il test passa

    # Testa la registrazione con mail vuota
    def test_registration_form_empty_mail(self):
        form_data = {
            'username': 'testuser1',
            'email': '',
            'nome': 'Test Nome',
            'password1': 'TestPassword123!',
            'password2': 'TestPassword123!',
            'citta': 'Test City',
            'is_azienda': False
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())    # Se l'interno e' falso allora il test passa

    # Testa la registrazione con nome vuoto
    def test_registration_form_empty_name(self):
        form_data = {
            'username': 'testuser1',
            'email': 'testuser@example.com',
            'nome': '',
            'password1': 'TestPassword123!',
            'password2': 'TestPassword123!',
            'citta': 'Test City',
            'is_azienda': False
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())    # Se l'interno e' falso allora il test passa