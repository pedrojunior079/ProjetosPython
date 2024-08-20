from django.http import HttpResponse
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from .models import Pergunta

def index(request):
    latest_pergunta_list= Pergunta.objects.order_by("-pub_date")[:5]
    context = {"latest_pergunta_list": latest_pergunta_list}
    return render(request, "pesquisas/index.html",context)

def detail(request, pergunta_id):
    pergunta = get_object_or_404(pergunta, pk=pergunta_id)    
    return render(request, "pesquisas/detail.html", {"pergunta": pergunta})

def resultados(request, pergunta_id):
    response = "Voce esta olhando os resultados da pergunta %s."
    return HttpResponse(response % pergunta_id)

def voto(request, pergunta_id):
    return HttpResponse("Voce está votando na questão %s." % pergunta_id)

