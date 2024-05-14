from django.http import HttpResponse
from django.shortcuts import render


def page_with_static(request):
    return render(request, template_name="baseext.html",context={"title":"Pagina con elementi statici"})
