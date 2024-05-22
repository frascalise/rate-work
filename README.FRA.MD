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
- [] Visualizzare le proprie recensioni
- [] Visualizzare dove lavori (o inviare richiesta di lavoro se non lavori)
- [] Modificare il profilo
- [] Valutare l'azienda dove lavori
- [] Visualizzare annunci di lavoro personalizzati

# Profilo azienda
- [x] Visualizzare i propri dati, username, nome ecc...
- [] Visualizzare le proprie recensioni
- [] Visualizzare quali lavoratori sono assunti
- [] Modificare il profilo
- [] Valutare i lavoratori assunti
- [x] Creare annunci di lavoro



## COMANDI UTILI ##

# Avviare il progetto
- python manage.py runserver

# Creare una nuova app
- python manage.py startapp nome_app
- python manage.py makemigrations nome_app
- python manage.py migrate

# Creare un superuser
- python manage.py createsuperuser