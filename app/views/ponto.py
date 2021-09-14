from .imports import *
from .general import *

 
def ponto(request, pk):
    data = {}
    data['db'] = Funcionario.objects.get(pk=pk)
    data['ponto_form'] = PontoForm(request.POST or None, instance=data['db'])

    return render(request, 'ponto/ponto_horario.html', data)


def bater_ponto(request, pk):

    today = pendulum.today()
    form = PontoForm(request.POST or None)  #DADOS QUE VÊM DO FORMULARIO
    if form.is_valid():  #VERIFICA SE TUDO É VÁLIDO
        instance = form.save()
        instance.is_active = True
        instance.funcionario_id = pk

        #!CASTING DAS HORAS
        hora_entrada = int((instance.hora_entrada).strftime("%H"))
        hora_saida = int((instance.hora_saida).strftime("%H"))
        instance.horas_trabalhadas = (hora_saida - hora_entrada)
        instance.mes_ponto = int(today.month)
        instance.is_paid = False

        inserir_pagamento_hora(instance, pk)

        instance.save()

        return redirect('home')  #*REDIRECIONA PARA A HOME


def ponto_info(request, pk):
    user = Funcionario.objects.get(pk=pk)
    #Proximo mes que o funcionario vai receber o pagamento
    proximo_mes= int(user.data_pagamento.month)
    #Atualiza os que já foram pagos
    query = (Q(funcionario_id=pk) & Q(mes_ponto__lte=proximo_mes))

    if user.mes_pago:
        PontoFuncionario.objects.filter(query).update(is_paid=True)

    queryset = PontoFuncionario.objects.all()

    context = {
        "user": user,
        "object_list": queryset,
    }

    return render(request, 'ponto/ponto_info.html', context)


def inserir_pagamento_hora(instance, pk):
    user = Funcionario.objects.get(pk=pk)

    #CALCULA O VALOR A RECEBER ()
    if instance.horas_trabalhadas > 8:
        #CALCULA O BONUS DE 1.5x
        excedente = (instance.horas_trabalhadas - 8)
        bonus = (excedente * 1.5) * 10
        user.total_a_receber += (user.salario * 8) + bonus
    else:
        user.total_a_receber += (user.salario * instance.horas_trabalhadas)

    Funcionario.objects.filter(pk=pk).update(
        total_a_receber=user.total_a_receber)


def remover_pagamento_hora(funcionario_id, pk):
    instance = PontoFuncionario.objects.get(pk=pk)
    user = Funcionario.objects.get(pk=funcionario_id)

    if instance.horas_trabalhadas > 8:
        #CALCULA O BONUS DE 1.5x
        excedente = (instance.horas_trabalhadas - 8)
        bonus = (excedente * 1.5) * 10
        calc = (user.salario * 8) + bonus
        if user.total_a_receber >= calc:
            user.total_a_receber -= calc
        else:
            user.total_a_receber = 0
    else:
        user.total_a_receber -= (user.salario * instance.horas_trabalhadas)

    result = user.total_a_receber
    Funcionario.objects.filter(pk=funcionario_id).update(
        total_a_receber=result)


def desativar_ponto(request, funcionario_id, pk):
    remover_pagamento_hora(funcionario_id, pk)
    PontoFuncionario.objects.filter(pk=pk).update(is_active=False)
    return ponto_info(request, funcionario_id)


def reativar_ponto(request, funcionario_id, pk):
    instance = PontoFuncionario.objects.get(pk=pk)
    funcionario = Funcionario.objects.get(pk=funcionario_id)
    inserir_pagamento_hora(instance, funcionario_id)
    PontoFuncionario.objects.filter(pk=pk).update(is_active=True)
        
    return ponto_info(request, funcionario_id)


def deletar_ponto(request, funcionario_id, pk):
    ponto = PontoFuncionario.objects.get(pk=pk)
    ponto.delete()
    return ponto_info(request, funcionario_id)

