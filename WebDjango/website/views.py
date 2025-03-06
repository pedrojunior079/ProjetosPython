from django.shortcuts import render
from django.views.generic import ListView, CreateView
from django.views.generic.edit import UpdateView
from models import Funcionario
from  views import  FuncionarioListView 

def lista_funcionrios(request):
    # Primeiro, buscamos os funcionarios
    funcionarios = Funcionario.objetos.all()

    # Incluimos no contexto
    contexto = {'funcionarios': funcionarios}

    # Retornamos o template para listar os funcionarios
    return render(request, "templates/funcionarios.html", contexto)


def cria_funcionario(request, pk):
    # verifica se o método POST
    if request.method == 'POST':
        form = FormularioDeCriacao(request.POST)

        if form.is_valid():
          form.save()
          return HttpResponseRedirect(reverse('lista_funcionarios'))
        
    # Qualquer outro método: GET, OPTION, DELETE, etc...     
    else:
        return render(request, "templates/form.html", {"form", form})


class ListaFuncionarios(ListView):
    template_name = "template/funcionarios.html"
    model = Funcionario
    context_object_name = "funcionarios"


class IndexTemplateView(TemplateView):
    template_name = "index.html"


class FuncionarioListView(ListView):
    template_name = "template/funcionarios.html"
    model = Funcionario
    context_object_name = "funcionarios"

    def get_object(self, queryset=None):
        funcionario = None

        # Os campos {pk} e {slug} estao presentes em self.kwargs 
        id = self.kwargs.get(self.pk_kwargs)
        slug = self.kwargs.get(self.slug_url_kwarg)

        if id is not None:
          # Busca o funcionaro a partir do id
          funcionario = Funcionario.objects.filter(id=id).first()

        elif slug is not None:
          # Pega o campo slug do Model
          campo_slug = self.get_slug_field()

          # Busca o funcionario a partir do slug 
          funcionario = Funcionario.objects.filter(**{campo_slug: slug}).first()  
    
        # retorna o objeto encontrado
        return funcionario


class FuncionarioUpdateView(UpdateView):
    template_name = "atualiza.html"
    model = Funcionario
    fields = [
      'nome',
      'sobrenome',
      'cpf',
      'tempo_de_servico',
      'renumeracao'  
    ]

class FuncionarioDeleteView(DeleteView):
  template_name = "website/excluir.html"
  model = Funcionario
  context_object_name = 'funcionario'
  sucess_url = reverse_lazy("website:lista_funcionarios")

class FuncionarioCreateView(CreateView):
   template_name = "website/cria.html"
   model = Funcionario
   form_class = InsereFuncionarioForm
   success_url = reverse_lazy("website:lista_funcionarios")


class FiltraIPMiddleware:
   def __init__(self, get_response=None):
      self.get_response = get_response

   def __call__(self, request):
     response = self.get_response(request)
     return response

   def process_view(request, func, args, kwargs):
     # Lista de IPs autorizados
     ips_autorizados = ['127.0.0.1']

     # IP do usuario
     ip = request.META.get('REMOTE_ADDR')

     # verifica se o IP do está na Lista de IPs autorizados
     if ip not in ips_autorizados:
       # se usuario não autorizado > HTTP 403 (náo autorizado)
       return HttpResponseForbidden("IP não autorizado")
     

     # Se for autorizado, não fazemos nada
     return None
