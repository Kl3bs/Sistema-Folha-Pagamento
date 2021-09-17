from .imports import *
from .general import *

#* FOLHA DE PAGAMENTO


def folha_pagamento(request):

    data = pendulum.today()
    users = Funcionario.objects.filter(
        Q(is_active=True) & Q(data_pagamento=data))

    context = {
        "users": users,
    }
    return render(request, 'pagamento/pagamento.html', context)


def rodar_folha(request):

    today = pendulum.today()

    users = Funcionario.objects.filter(
        Q(is_active=True) & Q(data_pagamento=today))

    mes_atual = int(today.month)
    users.update(mes_pago=mes_atual)

    users.update(total_a_receber=0)
    users.update(data_pagamento=today.add(months=1))

    return render(request, 'pagamento/pagamento.html')


@csrf_exempt
@csrf_exempt
def agenda_pagamento(request, pk, dia):
    funcionario = filterById(Funcionario, pk)
    today = pendulum.today()

    if request.is_ajax() and request.POST:
        nova_data = pendulum.datetime(today.year, today.month, dia)
        funcionario.update(data_pagamento=nova_data)
        return render(request, 'index.html')
    else:
        raise
