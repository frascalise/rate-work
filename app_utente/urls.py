from django.urls import include, path
from . import views

app_name = 'app_utente'

urlpatterns = [
    path('', views.home, name='home'),
    path('app_utente/', include('app_utente.urls')),
    path('admin/', admin.site.urls)   
]