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
        "nome": ["Mario", "Luigi", "Peach", "Toad", "Yoshi"],
        "cognome": ["Rossi", "Verdi", "Bianchi", "Gialli", "Neri"]
    }

    for i in range(5):
        Utente.objects.create(nome=utentiDict["nome"][i], cognome=utentiDict["cognome"][i])
    
    print("==============================")
    print("Database inizializzato con \nsuccesso!")
    print("==============================\n")