from django.urls import path
from .views import Profilo, Registrazione, Login, Logout, ProfiloCercato, Richieste, RecensioneUtente

urlpatterns = [
    path('', Profilo, name='profilo'),
    path('registrazione/', Registrazione, name='registrazione'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('richieste/', Richieste, name='richieste'),
    path('recensione/<str:username>/', RecensioneUtente, name='recensione'),
    path('<str:username>/', ProfiloCercato, name='profilo_cercato'),
]
