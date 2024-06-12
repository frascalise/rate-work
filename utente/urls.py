<<<<<<< HEAD
from django.urls import path, re_path
from .views import Profilo, Registrazione, Login, Logout, ProfiloCercato, Richieste, RecensioneUtente, ModificaProfilo, Licenzia, CancellaAnnuncio, errore_404

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

=======
from django.urls import path, re_path
from .views import Profilo, Registrazione, Login, Logout, ProfiloCercato, Richieste, RecensioneUtente, ModificaProfilo, Licenzia, CancellaAnnuncio, errore_404

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

>>>>>>> 6922e3ef929380bfbd6f2c6b085c610217e22633
urlpatterns.append(re_path(r'^.*/$', errore_404))