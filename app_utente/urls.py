from django.urls import include, path
from django.contrib import admin  # Import the admin module
from . import views

app_name = 'app_utente'

urlpatterns = [
    path('<int:pk>/', views.UtenteDetail.as_view(), name='utente_detail'),  # es. http://127.0.0.1:8000/utente/2/
    path('', views.UtenteList.as_view(), name='utente_list')
]