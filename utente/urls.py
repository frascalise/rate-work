from django.urls import path
from .views import Profilo, Registrazione, Login, Logout, ProfiloCercato, Richieste, RecensioneUtente, ModificaProfilo, Licenzia, CancellaAnnuncio

urlpatterns = [
    path('', Profilo, name='profilo'),
    path('modifica/', ModificaProfilo, name='modifica'),
    path('registrazione/', Registrazione, name='registrazione'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('richieste/', Richieste, name='richieste'),
    path('licenzia/<str:username>/', Licenzia, name='licenzia'),
    path('recensione/<str:username>/', RecensioneUtente, name='recensione'),
    path('cancella_annuncio/<int:id>/', CancellaAnnuncio, name='cancella_annuncio'),
    path('<str:username>/', ProfiloCercato, name='profilo_cercato'),
]
