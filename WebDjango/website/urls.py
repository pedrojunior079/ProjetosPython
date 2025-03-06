# Importamos a função index() definida no arquivo views.py
from django.urls import path
from django.views.generic import IndexTemplateView, FuncionarioListViews, FuncionarioUpdate, FuncionarioCreateView

from . import views 

app_name = 'website'

# urlpatterns contém a Lista de roteamentos de URLs
urlpatterns = [
    # GET
    path('', IndexTemplateView.as_view(), name='index'),
    path('funcionarios/', FuncionarioListViews.as_view(), name='lista_funcionarios'),
    
    # Utilizando o {id} para buscar o objeto
    path('funcionario/<id>', FuncionarioUpdateView.as_view(),
         name='atualiza_funcionario'),

    # Utilizando o {slug} para buscar o objeto
    path('funcionario/<slug>', FuncionarioUpdateView.as_view(), 
         name='atualiza_funcionario'),

    path('funcionario/excluir/<pk>', FuncionarioDeleteView.as_view(),
         name='deletar_funcionario'),

    path('funcionario/cadastrar/', FuncionarioCreateView.as_view(),
         name='cdastra_funcionario')               
]
