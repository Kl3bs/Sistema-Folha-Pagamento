from .imports import *


def getById(self, pk):
    return self.objects.get(pk=pk)


def filterById(self, pk):
    return self.objects.filter(pk=pk)


#* (CRUD) E MÉTODOS GERAIS
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

            today = pendulum.today()
            instance.data_pagamento = today.add(days=30)

        if instance.tipo == "COMISSIONADO":
            instance.total_a_receber = instance.salario

            today = pendulum.today()
            instance.data_pagamento = today.add(days=15)

        if instance.tipo == "HORISTA":
            instance.total_a_receber = 0

            #BIBLIOTECA PENDULUM CALCULA A DATA DE PAGAMENTO
            instance.data_pagamento = pendulum.now().next(
                pendulum.FRIDAY).strftime('%Y-%m-%d')

        instance.save()  #!SALVA NO BANCO

        return redirect('home')  #*REDIRECIONA PARA A HOME


def view(requiest, pk):
    data = {}
    data['db'] = getById(Funcionario, pk)
    return render(requiest, 'user/view.html', data)


def edit(request, pk):
    data = {}
    data['db'] = getById(Funcionario, pk)
    data['form'] = FuncionarioForm(instance=data['db'])
    return render(request, 'user/form.html', data)


def update(request, pk):
    data = {}
    data['db'] = getById(Funcionario, pk)
    form = FuncionarioForm(
        request.POST or None, instance=data['db']
    )  #Pega os dados do form e atualiza na instância 'db' (Banco de dados)
    if form.is_valid:
        form.save()
        return redirect('home')


def delete(request, pk):
    db = getById(Funcionario, pk)
    db.delete()
    return redirect('home')


def desativar(request, pk):
    filterById(Funcionario, pk).update(is_active=False)
    return redirect('home')


def reativar(request, pk):
    filterById(Funcionario, pk).update(is_active=True)
    return redirect('home')
