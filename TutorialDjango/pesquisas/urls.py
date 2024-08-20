from django.urls import path

from . import views

app_name = "pesquisas"

urlpatterns = [
    path("", views.index, name="index"),
    # ex: /pesquisas/5/
    path("<int:pergunta_id>/", views.detail, name="detail"),
    # ex: /pesquisas/5/resultados/
    path("<int:pergunta_id>/resultados/", views.resultados, name="resultados"),
    # ex: /pesquisas/5/voto/
    path("<int:pergunta_id>/voto/", views.voto, name="voto"),
    # added the word 'detalhes'
    path("detalhes/<int:pergunta_id>/", views.detail, name="detail"),
]

