from app_utente.models import Utente

def erase_db():
    print("==============================")
    print("Cancello tutti gli utenti... ")
    print("==============================\n")
    Utente.objects.all().delete()


def init_db():
    if len(Utente.objects.all()) != 0:
        print("Database già inizializzato")
        return

    utentiDict = {
        "nome": ["Mario", "Luigi", "Peach", "Toad", "Yoshi", "Bowser", "Wario", "Waluigi", "Daisy", "Rosalina", "Donkey Kong", "Diddy Kong", "Koopa Troopa", "Shy Guy", "Birdo", "Toadette"],
        "cognome": ["Rossi", "Verdi", "Bianchi", "Gialli", "Neri", "Arancioni", "Viola", "Azzurri", "Rosa", "Celesti", "Marroni", "Grigi", "Verdi", "Bianchi", "Neri", "Arancioni"]
    }

    for i in range(len(utentiDict["nome"])):
        Utente.objects.create(nome=utentiDict["nome"][i], cognome=utentiDict["cognome"][i])
    
    print("==============================")
    print("Database inizializzato con \nsuccesso!")
    print("==============================\n")

def print_db():
    print("==============================")
    print("Stampo tutti gli utenti... ")
    print("==============================\n")
    for utente in Utente.objects.all():
        print(utente.id, ": ", utente.getNomeCompleto())
    print("\n==============================\n")