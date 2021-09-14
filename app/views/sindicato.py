from .imports import *
from .general import *

#* SINDICATO
def mostrar_funcionarios(request):
    funcionarios = Funcionario.objects.all()
    context = {"funcionarios": funcionarios}
    return render(request, 'sindicato/painel_sindicato.html', context)
 
@csrf_exempt
def aplicar_taxa(request, pk, value):
    funcionario = Funcionario.objects.filter(pk=pk)
    val = (Funcionario.objects.get(pk=pk).total_a_receber) - value
    if request.is_ajax() and request.POST:
        funcionario.update(taxa_sindicato=value)
        funcionario.update(total_a_receber=val)
        return render(request, 'sindicato/painel_sindicato.html')
    else:
        raise Http404

