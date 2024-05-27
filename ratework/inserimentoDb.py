from utente.models import Utente, AnnuncioLavoro, Lavoro, Recensione


def initDb():
    Utente.objects.all().delete()
    AnnuncioLavoro.objects.all().delete()
    Lavoro.objects.all().delete()
    Recensione.objects.all().delete()
    print('========================================')
    print("Database inizializzato con successo.")


def inserimentoUtenti():
    utenti = [
        ('mariorossi', 'progetto21', 'mariorossi@example.com', 'Mario Rossi', 'Reggio Emilia', False),
        ('giorgiobianchi', 'progetto21', 'giorgiobianchi@example.com', 'Giorgio Bianchi', 'Modena', False),
        ('luciamarini', 'progetto21', 'luciamarini@example.com', 'Lucia Marini', 'Milano', False),
        ('andreabonolis', 'progetto21', 'andreabonolis@example.com', 'Andrea Bonolis', 'Parma', False),
        ('apple', 'progetto21', 'apple@example.com', 'Apple', 'Reggio Emilia', True),
        ('microsoft', 'progetto21', 'microsoft@example.com', 'Microsoft', 'Piacenza', True),
        ('google', 'progetto21', 'google@example.com', 'Google', 'Bologna', True),
        ('facebook', 'progetto21', 'facebook@example.com', 'Facebook', 'Reggio Emilia', True)
    ]

    for utente_data in utenti:
        Utente.objects.create_user(username=utente_data[0], password=utente_data[1], email=utente_data[2], nome=utente_data[3], citta=utente_data[4], is_azienda=utente_data[5])
    print("Utenti inseriti con successo.")


def inserimentoAnnunci():
    descrizione = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

    annunci = [
        ('apple', 'Software Developer', descrizione, False, '1000-1200', 'html css javascript'),
        ('apple', 'Web Developer', descrizione, True, '1200-1500', 'c++ python java'),
        ('apple', 'Data Scientist', descrizione, False, '1500-2000', 'sql r ruby'),
        ('microsoft', 'Software Developer', descrizione, False, '2000-2500', 'c# .net php'),
        ('microsoft', 'Web Developer', descrizione, True, '2500+', 'react angular vue'),
        ('microsoft', 'Data Scientist', descrizione, False, '1000-1200', 'scala go swift'),
        ('google', 'Software Developer', descrizione, False, '1200-1500', 'nodejs django flask'),
        ('google', 'Web Developer', descrizione, True, '1500-2000', 'html javascript jquery'),
        ('google', 'Data Scientist', descrizione, False, '2000-2500', 'python r sql'),
        ('facebook', 'Software Developer', descrizione, False, '2500+', 'java c++ c#'),
        ('facebook', 'Web Developer', descrizione, True, '1000-1200', 'java'),
        ('facebook', 'Data Scientist', descrizione, False, '1200-1500', 'python sql')
    ]

    for annuncio_data in annunci:
        azienda = Utente.objects.get(username=annuncio_data[0])
        AnnuncioLavoro.objects.create(azienda=azienda, titolo=annuncio_data[1], descrizione=annuncio_data[2], is_distanza=annuncio_data[3], range_stipendio=annuncio_data[4], tag=annuncio_data[5])
    print("Annunci inseriti con successo.")
    print('========================================\n')