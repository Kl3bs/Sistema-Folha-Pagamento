from django.shortcuts import redirect, render
from django.http import HttpResponse
from app.forms import FuncionarioForm
from app.models import Funcionario

# Create your views here.
def home(request):
    data = {}
    data [ 'db' ] = Funcionario.objects.all()  #DATA RECEBE OS VALORES TRAZIDOS DO BANCO EM FORMA DE ARRAY DE OBJETOS
    return render(request, 'index.html', data)


def form(request):
    data = {}
    data['form'] = FuncionarioForm()
    return render(request, 'form.html',data)

def create(request):
    form = FuncionarioForm(request.POST or None) #DADOS QUE VÊM DO FORMULARIO
    if form.is_valid(): #VERIFICA SE TUDO É VÁLIDO
        form.save()  #!SALVA NO BANCO
        return redirect('home') #*REDIRECIONA PARA A HOME

def view(requiest, pk):
    data = {}
    data['db'] = Funcionario.objects.get(pk=pk)
    return render(requiest, 'view.html', data)

def edit(request, pk):
    data = {}
    data['db']  = Funcionario.objects.get(pk=pk)
    data['form']  = FuncionarioForm(instance=data['db'])
    return render(request, 'form.html', data)

def update(request, pk):
    data = {}
    data['db'] = Funcionario.objects.get(pk=pk)
    form = FuncionarioForm(request.POST or None, instance=data['db'])  #Pega os dados do form e atualiza na instância 'db' (Banco de dados)
    if form.is_valid:
        form.save()
        return redirect('home')
