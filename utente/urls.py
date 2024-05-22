from django.urls import path
from .views import Registrazione, Login, Logout

urlpatterns = [
    path('registrazione/', Registrazione, name='registrazione'),
    path('login/', Login, name='login'),
    path('logout/', Logout, name='logout'),
]
