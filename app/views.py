from django.shortcuts import redirect, render
from django.http import HttpResponse
from app.forms import FuncionarioForm, PontoForm
from app.models import Funcionario, PontoFuncionario


# Create your views here.
def home(request):
    data = {}
    data['db'] = Funcionario.objects.all(
    )  #DATA RECEBE OS VALORES TRAZIDOS DO BANCO EM FORMA DE ARRAY DE OBJETOS
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = FuncionarioForm()
    return render(request, 'form.html', data)


def create(request):
    form = FuncionarioForm(request.POST or None)  #DADOS QUE VÊM DO FORMULARIO
    if form.is_valid():  #VERIFICA SE TUDO É VÁLIDO
        form.save()  #!SALVA NO BANCO
        return redirect('home')  #*REDIRECIONA PARA A HOME


def view(requiest, pk):
    data = {}
    data['db'] = Funcionario.objects.get(pk=pk)
    return render(requiest, 'view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = Funcionario.objects.get(pk=pk)
    data['form'] = FuncionarioForm(instance=data['db'])
    return render(request, 'form.html', data)


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


def ponto(request, pk):
    data = {}
    data['db'] = Funcionario.objects.get(pk=pk)
    # data['pontos'] = PontoFuncionario.objects.get()

    data['ponto_form'] = PontoForm(request.POST or None, instance=data['db'])
    return render(request, 'ponto_horario.html', data)


def bater_ponto(request, pk):
    form = PontoForm(request.POST or None)  #DADOS QUE VÊM DO FORMULARIO
    if form.is_valid():  #VERIFICA SE TUDO É VÁLIDO
        instance = form.save()
        instance.funcionario_id = pk
        instance.save()
        return redirect('home')  #*REDIRECIONA PARA A HOME

def ponto_info(request, pk):
    # data = {}
    # data['db'] = Funcionario.objects.get(pk=pk)
    # tasks= PontoFuncionario.objects.all()
    # return render(request, 'ponto_info.html', {'tasks' : tasks})

    # data = {}
    # data['db'] = Funcionario.objects.get(pk=pk)
    # data['tasks']= PontoFuncionario.objects.all()
    # return render(request, 'ponto_info.html', {'dados' : data})

    user = Funcionario.objects.get(pk=pk)
    queryset = PontoFuncionario.objects.all()
    
    context = {
        "user" : user,
        "object_list" : queryset
    }

    return render(request, 'ponto_info.html', context)
