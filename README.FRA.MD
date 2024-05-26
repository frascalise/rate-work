## STRUTTURA PROGETTO TECNOLOGIE WEB ##

## OBBLIGATORI##
- [] Login e Registrazione
- [] Controlli sui vari input
- [] Utilizzo delle feature di Django
- [] Messaggi di conferma/errore dopo le operazioni
- [] Test
    - [] Testare registrazione con ogni tipo di input possibile
    - [] Testare una vista

# Modello DB
- [x] Fare modello ER
- [x] App per utente (lavoratore + azienda)
- [] App per recensioni (?)

# Home Page
- [x] Pulsanti per Login - Registrazione - Logout
- [x] Ricerca di un utente (lavoratore o azienda) e visualizzarne il profilo (username, nome, recensioni)

# Profilo lavoratore
- [x] Visualizzare i propri dati, username, nome ecc...
- [x] Impostare i tag per gli annunci personalizzati
- [x] Visualizzare dove lavori (o inviare richiesta di lavoro se non lavori)
- [] Visualizzare annunci di lavoro personalizzati
- [] Visualizzare le proprie recensioni
- [] Valutare l'azienda dove lavori
- [] Modificare il profilo (COME ULTIMA COSA)

# Profilo azienda
- [x] Visualizzare i propri dati, username, nome ecc...
- [x] Creare annunci di lavoro
- [x] Visualizzare quali lavoratori sono assunti
- [] Valutare i lavoratori assunti
- [] Visualizzare le proprie recensioni
- [] Modificare il profilo (COME ULTIMA COSA)



## COMANDI UTILI ##

# Avviare il progetto
- python manage.py runserver

# Creare una nuova app
- python manage.py startapp nome_app
- python manage.py makemigrations nome_app
- python manage.py migrate

# Creare un superuser
- python manage.py createsuperuser