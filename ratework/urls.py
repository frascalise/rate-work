<<<<<<< HEAD
"""
URL configuration for ratework project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from .views import home, Candidatura, errore_404 
from .inserimentoDb import initDb, inserimentoUtenti, inserimentoAnnunci, inserimentoLavoro, inserimentoRecensioniAziendali, inserimentoRecensioniUtente
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('utente/', include('utente.urls')),
    path('candidatura/<int:id>/', Candidatura, name='candidatura'),
]

# Cosi posso usare i file multimediali
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Se aggiunta in urlpatterns non carica le risorse statiche e multimediali?
urlpatterns.append(re_path(r'^.*/$', errore_404))

'''Popolamento del database
initDb()
inserimentoUtenti()
inserimentoAnnunci()
inserimentoLavoro()
inserimentoRecensioniAziendali()
inserimentoRecensioniUtente()
=======
"""
URL configuration for ratework project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from .views import home, Candidatura, errore_404 
from .inserimentoDb import initDb, inserimentoUtenti, inserimentoAnnunci, inserimentoLavoro, inserimentoRecensioniAziendali, inserimentoRecensioniUtente
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('utente/', include('utente.urls')),
    path('candidatura/<int:id>/', Candidatura, name='candidatura'),
]

# Cosi posso usare i file multimediali
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Se aggiunta in urlpatterns non carica le risorse statiche e multimediali?
urlpatterns.append(re_path(r'^.*/$', errore_404))

'''Popolamento del database
initDb()
inserimentoUtenti()
inserimentoAnnunci()
inserimentoLavoro()
inserimentoRecensioniAziendali()
inserimentoRecensioniUtente()
>>>>>>> 6922e3ef929380bfbd6f2c6b085c610217e22633
''' 