from django.urls import path
from .views import Profilo, Registrazione, Login, Logout, CreaAnnuncio

urlpatterns = [
    path('', Profilo, name='profilo'),
    path('registrazione/', Registrazione, name='registrazione'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
    path('crea_annuncio/', CreaAnnuncio, name='crea_annuncio'),
]
