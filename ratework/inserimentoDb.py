from django.db import connection
from utente.models import Utente, AnnuncioLavoro, Lavoro, Recensione


def initDb():
    Utente.objects.all().delete()
    AnnuncioLavoro.objects.all().delete()
    Lavoro.objects.all().delete()
    Recensione.objects.all().delete()

    # RESET DEGLI ID
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='utente_utente';")
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='utente_annunciolavoro';")
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='utente_lavoro';")
        cursor.execute("DELETE FROM sqlite_sequence WHERE name='utente_recensione';")
        cursor.execute("DELETE FROM utente_utente;")
        cursor.execute("DELETE FROM utente_annunciolavoro;")
        cursor.execute("DELETE FROM utente_lavoro;")
        cursor.execute("DELETE FROM utente_recensione;")

    print('========================================')
    print("Database inizializzato con successo.")


def inserimentoUtenti():
    utenti = [                                                                                              # ID                                   
        ('mariorossi', 'progetto21', 'mariorossi@example.com', 'Mario Rossi', 'Reggio Emilia', False),      # 1
        ('giorgiobianchi', 'progetto21', 'giorgiobianchi@example.com', 'Giorgio Bianchi', 'Modena', False), # 2
        ('luciamarini', 'progetto21', 'luciamarini@example.com', 'Lucia Marini', 'Milano', False),          # 3
        ('andreabonolis', 'progetto21', 'andreabonolis@example.com', 'Andrea Bonolis', 'Parma', False),     # 4
        ('apple', 'progetto21', 'apple@example.com', 'Apple', 'Reggio Emilia', True),                       # 5
        ('microsoft', 'progetto21', 'microsoft@example.com', 'Microsoft', 'Piacenza', True),                # 6
        ('google', 'progetto21', 'google@example.com', 'Google', 'Bologna', True),                          # 7
        ('facebook', 'progetto21', 'facebook@example.com', 'Facebook', 'Reggio Emilia', True)               # 8
    ]

    for utente_data in utenti:
        Utente.objects.create_user(username=utente_data[0], password=utente_data[1], email=utente_data[2], nome=utente_data[3], citta=utente_data[4], is_azienda=utente_data[5])
    print("Utenti inseriti con successo.")


def inserimentoAnnunci():
    descrizione = 'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.'

    annunci = [
        # username,     titolo,                 descrizione, is_distanza,   range_stipendio,    tag                         # ID
        ('apple',       'Software Developer',   descrizione, False,         '1000-1200',        'html css javascript'),     # 1  
        ('apple',       'Web Developer',        descrizione, True,          '1200-1500',        'c++ python java'),         # 2 
        ('apple',       'Data Scientist',       descrizione, False,         '1500-2000',        'sql r ruby'),              # 3 
        ('microsoft',   'Software Developer',   descrizione, False,         '2000-2500',        'c# .net php'),             # 4
        ('microsoft',   'Web Developer',        descrizione, True,          '2500+',            'react angular vue'),       # 5
        ('microsoft',   'Data Scientist',       descrizione, False,         '1000-1200',        'scala go swift'),          # 6
        ('google',      'Software Developer',   descrizione, False,         '1200-1500',        'nodejs django flask'),     # 7
        ('google',      'Web Developer',        descrizione, True,          '1500-2000',        'html javascript jquery'),  # 8
        ('google',      'Data Scientist',       descrizione, False,         '2000-2500',        'python r sql'),            # 9
        ('facebook',    'Software Developer',   descrizione, False,         '2500+',            'java c++ c#'),             # 10
        ('facebook',    'Web Developer',        descrizione, True,          '1000-1200',        'java'),                    # 11
        ('facebook',    'Data Scientist',       descrizione, False,         '1200-1500',        'python sql')               # 12
    ]

    for annuncio_data in annunci:
        azienda = Utente.objects.get(username=annuncio_data[0])
        AnnuncioLavoro.objects.create(azienda=azienda, titolo=annuncio_data[1], descrizione=annuncio_data[2], is_distanza=annuncio_data[3], range_stipendio=annuncio_data[4], tag=annuncio_data[5])
    print("Annunci inseriti con successo.")

def inserimentoLavoro():
    lavoro = [
        # annuncio,    lavoratore,      stato           # ID
        (1,             1,              'Accettato'),   # 1
        (2,             2,              'In attesa'),   # 2
        (3,             3,              'Accettato'),   # 3
        (2,             4,              'In attesa'),   # 4
    ]

    annuncio1 = AnnuncioLavoro.objects.get(id=1)
    annuncio1.is_available = False
    annuncio1.save()

    annuncio3 = AnnuncioLavoro.objects.get(id=3)
    annuncio3.is_available = False
    annuncio3.save()

    for assunzione_data in lavoro:
        annuncio = AnnuncioLavoro.objects.get(id=assunzione_data[0])
        lavoratore = Utente.objects.get(id=assunzione_data[1])
        Lavoro.objects.create(annuncio=annuncio, lavoratore=lavoratore, stato=assunzione_data[2])
    print("Assunzioni inserite con successo.")

def inserimentoRecensioniAziendali():
    TitoloPositivo1 = 'Ottimo lavoro'
    TitoloPositivo2 = 'Lavoro eccellente'
    TitoloPositivo3 = 'Soddisfatto'
    TitoloPositivo4 = 'Consigliato'
    CommentoPositivo1 = 'Sono molto soddisfatto del lavoro svolto da Apple'
    CommentoPositivo2 = 'Ottimo lavoro svolto da Apple, consigliato'
    CommentoPositivo3 = 'Lavoro eccellente, sono molto soddisfatto'
    CommentoPositivo4 = 'Consigliato, lavoro eccellente'
    TitoloNegativo1 = 'Pessimo lavoro'
    TitoloNegativo2 = 'Non soddisfatto'
    CommentoNegativo1 = 'Non sono soddisfatto del lavoro svolto da Apple'
    CommentoNegativo2 = 'Pessimo lavoro svolto da Apple'
    TitoloNeutro1 = 'Lavoro sufficiente'
    TitoloNeutro2 = 'Niente di speciale'
    CommentoNeutro1 = 'Lavoro sufficiente, niente di speciale'
    CommentoNeutro2 = 'Niente di speciale, lavoro sufficiente'

    recensioni = [
    # mittente,     destinatario,   lavoro,     valutazione,   titolo,              commento
    (1,             5,              1,          1,              TitoloPositivo1,    CommentoPositivo1),
    (1,             5,              1,          1,              TitoloPositivo2,    CommentoPositivo2),
    (3,             5,              3,          1,              TitoloPositivo3,    CommentoPositivo3),
    (3,             5,              3,          1,              TitoloPositivo4,    CommentoPositivo4),
    (1,             5,              1,          -1,             TitoloNegativo1,    CommentoNegativo1),
    (1,             5,              1,          -1,             TitoloNegativo2,    CommentoNegativo2),
    (1,             5,              1,          0,              TitoloNeutro1,      CommentoNeutro1),
    (1,             5,              1,          0,              TitoloNeutro2,      CommentoNeutro2),
    ]

    for recensione in recensioni:
        mittente = Utente.objects.get(id=recensione[0])
        destinatario = Utente.objects.get(id=recensione[1])
        lavoro = Lavoro.objects.get(id=recensione[2])
        Recensione.objects.create(mittente=mittente, destinatario=destinatario, lavoro=lavoro, valutazione=recensione[3], titolo=recensione[4], commento=recensione[5])
    print("Recensioni per le aziende inserite con successo.")

def inserimentoRecensioniUtente():
    TitoloPositivo1 = 'Ottimo lavoro'
    TitoloPositivo2 = 'Lavoro eccellente'
    TitoloPositivo3 = 'Soddisfatto'
    TitoloPositivo4 = 'Consigliato'
    CommentoPositivo1 = 'Sono molto soddisfatto del lavoro svolto da Apple'
    CommentoPositivo2 = 'Ottimo lavoro svolto da Apple, consigliato'
    CommentoPositivo3 = 'Lavoro eccellente, sono molto soddisfatto'
    CommentoPositivo4 = 'Consigliato, lavoro eccellente'

    recensioni = [
    # mittente,     destinatario,   lavoro,     valutazione,   titolo,              commento
    (5,             1,              1,          1,              TitoloPositivo1,    CommentoPositivo1),
    (5,             1,              1,          1,              TitoloPositivo2,    CommentoPositivo2),
    (5,             3,              3,          1,              TitoloPositivo3,    CommentoPositivo3),
    (5,             3,              3,          1,              TitoloPositivo4,    CommentoPositivo4),
    ]

    for recensione in recensioni:
        mittente = Utente.objects.get(id=recensione[0])
        destinatario = Utente.objects.get(id=recensione[1])
        lavoro = Lavoro.objects.get(id=recensione[2])
        Recensione.objects.create(mittente=mittente, destinatario=destinatario, lavoro=lavoro, valutazione=recensione[3], titolo=recensione[4], commento=recensione[5])
    print("Recensioni per i lavoratori inserite con successo.")
    print('========================================\n')