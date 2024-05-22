## STRUTTURA PROGETTO TECNOLOGIE WEB ##

# Modello DB
- [x] Fare modello ER
- [] App per utente (lavoratore + azienda)
- [] App per recensioni (?)

# Home Page
- [] Pulsanti per Login - Registrazione - Logout

# Profilo lavoratore
- [] Visualizzare le proprie recensioni
- [] Visualizzare dove lavori (o inviare richiesta di lavoro se non lavori)
- [] Modificare il profilo
- [] Valutare l'azienda dove lavori

# Profilo azienda
- [] Visualizzare le proprie recensioni
- [] Visualizzare quali lavoratori sono assunti
- [] Modificare il profilo
- [] Valutare i lavoratori assunti


## COMANDI UTILI ##

# Avviare il progetto
- python manage.py runserver

# Creare una nuova app
- python manage.py startapp nome_app
- python manage.py makemigrations nome_app
- python manage.py migrate

# Creare un superuser
- python manage.py createsuperuser