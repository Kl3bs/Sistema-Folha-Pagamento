from django.shortcuts import redirect, render
from django.http import HttpResponse
from app.forms import FuncionarioForm, PontoForm, VendaForm
from app.models import Funcionario, PontoFuncionario, Venda
from django.db.models import Sum
from django.db.models import F
from datetime import datetime


# Create your views here.
def home(request):
    data = {}
    data['db'] = Funcionario.objects.all(
    )  #DATA RECEBE OS VALORES TRAZIDOS DO BANCO EM FORMA DE ARRAY DE OBJETOS

    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = FuncionarioForm()
    return render(request, 'user/form.html', data)


def create(request):
    form = FuncionarioForm(request.POST or None)  #DADOS QUE VÊM DO FORMULARIO
    if form.is_valid():  #VERIFICA SE TUDO É VÁLIDO
        instance = form.save()
        instance.is_active = True

        if instance.tipo == "MENSALISTA":
            instance.total_a_receber = instance.salario
        else:
            instance.total_a_receber = 0

        instance.save()  #!SALVA NO BANCO

        return redirect('home')  #*REDIRECIONA PARA A HOME


def view(requiest, pk):
    data = {}
    data['db'] = Funcionario.objects.get(pk=pk)

    return render(requiest, 'user/view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Funcionario.objects.get(pk=pk)
    data['form'] = FuncionarioForm(instance=data['db'])

    return render(request, 'user/form.html', data)


def update(request, pk):
    data = {}
    data['db'] = Funcionario.objects.get(pk=pk)
    form = FuncionarioForm(
        request.POST or None, instance=data['db']
    )  #Pega os dados do form e atualiza na instância 'db' (Banco de dados)
    if form.is_valid:
        form.save()

        return redirect('home')


def delete(request, pk):
    db = Funcionario.objects.get(pk=pk)
    db.delete()

    return redirect('home')


def desativar(request, pk):
    Funcionario.objects.filter(pk=pk).update(is_active=False)
    return redirect('home')


def reativar(request, pk):
    Funcionario.objects.filter(pk=pk).update(is_active=True)
    return redirect('home')


def ponto(request, pk):
    data = {}
    data['db'] = Funcionario.objects.get(pk=pk)
    data['ponto_form'] = PontoForm(request.POST or None, instance=data['db'])

    return render(request, 'ponto/ponto_horario.html', data)


def bater_ponto(request, pk):

    user = Funcionario.objects.get(pk=pk)
    form = PontoForm(request.POST or None)  #DADOS QUE VÊM DO FORMULARIO
    if form.is_valid():  #VERIFICA SE TUDO É VÁLIDO
        instance = form.save()
        instance.is_active = True
        instance.funcionario_id = pk

        hora_entrada = int((instance.hora_entrada).strftime("%H"))
        hora_saida = int((instance.hora_saida).strftime("%H"))
        instance.horas_trabalhadas = (hora_saida - hora_entrada)

        #CALCULA O VALOR A RECEBER ()
        if instance.horas_trabalhadas > 8:
            #CALCULA O BONUS DE 1.5x
            excedente =  (instance.horas_trabalhadas - 8)
            bonus = (excedente * 1.5) * 10 
            user.total_a_receber = (user.salario * 8) + bonus
        else:
            user.total_a_receber += (user.salario * instance.horas_trabalhadas)

        Funcionario.objects.filter(pk=pk).update(
            total_a_receber=user.total_a_receber)

        instance.save()

        return redirect('home')  #*REDIRECIONA PARA A HOME


def ponto_info(request, pk):
    user = Funcionario.objects.get(pk=pk)
    queryset = PontoFuncionario.objects.all()
    time1 = PontoFuncionario.objects.values('hora_entrada')

    horas_trabalhadas = PontoFuncionario.objects.filter(
        funcionario_id__exact=pk).values_list()

    context = {
        "user": user,
        "object_list": queryset,
        "time1": time1,
        "horas_trabalhadas": horas_trabalhadas
    }

    return render(request, 'ponto/ponto_info.html', context)


def vendas(request, pk):
    data = {}
    data['db'] = Funcionario.objects.get(pk=pk)
    data['venda_form'] = VendaForm()
    return render(request, 'vendas/nova_venda.html', data)


def nova_venda(request, pk):
    form = VendaForm(request.POST or None)  #DADOS QUE VÊM DO FORMULARIO
    if form.is_valid():  #VERIFICA SE TUDO É VÁLIDO
        instance = form.save()
        instance.funcionario_id = pk
        instance.save()

        return redirect('home')  #*REDIRECIONA PARA A HOME


def listar_vendas(request, pk):
    user = Funcionario.objects.get(pk=pk)
    queryset = Venda.objects.all()

    #* SOMA TODOS AS VENDAS DO FUNCIONARIO, MULTIPLICA PELA TAXA DE COMISSAO E RETORNA O RESULTADO
    total_comissao = list(
        Venda.objects.filter(funcionario_id__exact=pk).aggregate(
            Sum('valor_venda')).values())[0] * (user.comissao / 100)

    context = {
        "user": user,
        "object_list": queryset,
        "total_comissao": total_comissao
    }

    return render(request, 'vendas/listar_vendas.html', context)


def desativar_ponto(request, funcionario_id, pk):
    PontoFuncionario.objects.filter(pk=pk).update(is_active=False)
    return ponto_info(request, funcionario_id)


def reativar_ponto(request, funcionario_id, pk):
    PontoFuncionario.objects.filter(pk=pk).update(is_active=True)
    return ponto_info(request, funcionario_id)


def deletar_ponto(request, funcionario_id, pk):
    ponto = PontoFuncionario.objects.get(pk=pk)
    ponto.delete()

    return ponto_info(request, funcionario_id)
    #return render(request, 'ponto/ponto_info.html', funcionario)
