## STRUTTURA PROGETTO TECNOLOGIE WEB ##

# Modello DB
- [x] Fare modello ER
- [x] App per utente (lavoratore + azienda)
- [] App per recensioni (?)

# Home Page
- [x] Pulsanti per Login - Registrazione - Logout
- [] Ricerca di un utente (lavoratore o azienda) e visualizzarne il profilo (username, nome, recensioni)

# Profilo lavoratore
- [x] Visualizzare i propri dati, username, nome ecc...
- [x] Impostare i tag per gli annunci personalizzati
- [] Visualizzare annunci di lavoro personalizzati
- [] Visualizzare dove lavori (o inviare richiesta di lavoro se non lavori)
- [] Visualizzare le proprie recensioni
- [] Valutare l'azienda dove lavori
- [] Modificare il profilo (COME ULTIMA COSA)

# Profilo azienda
- [x] Visualizzare i propri dati, username, nome ecc...
- [x] Creare annunci di lavoro
- [] Visualizzare le proprie recensioni
- [] Visualizzare quali lavoratori sono assunti
- [] Valutare i lavoratori assunti
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