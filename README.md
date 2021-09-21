# Sistema de Pagamento (Projeto de Software-UFAL)


## Installation (Venv)

Esta aplicação necessita que o Python esteja instalado em sua máquina.

Após clonar o projeto, navegue até a pasta dele e abra a pasta raiz do projeto com o terminal e digite o comando a seguir:
```sh
python -m venv venv
```


## Ativando sua venv (Windows)

Navegue até /venv/Scripts, em seguida basta digitar o comando "./activate" (Sem aspas);
 
## Ativando sua venv (MacOS)

Na raiz do projeto, digite: 

```sh
source venv/bin/activate
```
 
## Instalando o django

Após ativar sua venv, execute o seguinte comando:
```sh
pip install django
```

## Executando o projeto

Volte para a pasta raiz do projeto pelo terminal e digite:
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Acesse o endereço localhost:8000, para ver o projeto no browser.


## Padrões Implementados:

- Mixin pattern; 
- Custom manager pattern;
- Decorator pattern;
- Extract method;

A maioria das atualizações foram feitas dentro da view e do model.
Todas as funcionalidades estão implementadas.

## Obs:

Todos os dados e padrões foram baseados no livro: Django Design Patterns and Best Practices.

## Code Smells Encontrados

- Comments: foi utilizado Custom Manager Pattern, onde cada "Manager" pudesser ser de fácil entendimento, excluindo a necessidade de comentários.

`vendas.py`:
```py
def listar_vendas(request, pk):
    user = Funcionario.objects.get(pk=pk)

    proximo_mes= int(user.data_pagamento.month)
    #Atualiza os que já foram pagos
    query = (Q(funcionario_id=pk) & Q(mes_venda__lte=proximo_mes))

    if user.mes_pago:
        Venda.objects.filter(query).update(is_paid=True)

```

`vendas.py (refactored)`:
```py
def listar_vendas(request, pk):
    user = getById(Funcionario, pk)
    proximo_mes = int(user.data_pagamento.month) + 1
    query = (Q(funcionario_id=pk) & Q(mes_venda__lte=proximo_mes))
    if user.mes_pago:
        filterById(Venda, query).update(is_paid=True)
```


- Duplicate code: várias chamadas de filtragem em locais diversose e de difícil compreensão, pattern aplicado (Custom Manger):

`general.py`:
```py
def desativar(request, pk):
    Funcionario.objects.filter(pk=pk).update(is_active=False)
    return redirect('home')
```

`general.py`:

```py
def desativar(request, pk):
    filterById(Funcionario, pk).update(is_active=False)
    return redirect('home')
```


- Long method: Métodos extensos e complexos, pattern aplicado (Extract Method):
`vendas.py`:
```py
def desativar_venda(request, funcionario_id, pk):
    instance = getById(Venda, pk)
    user = getById(Funcionario, funcionario_id)
    user.total_a_receber -= (instance.valor_venda * (user.comissao / 100))
    Funcionario.objects.filter(pk=funcionario_id).update(
        total_a_receber=user.total_a_receber)

    Venda.objects.filter(pk=pk).update(is_active=False)
    return listar_vendas(request, funcionario_id)
```

`vendas.py`:


```py
def desativar_venda(request, funcionario_id, pk):
    remover_pagamento_comissao(funcionario_id, pk)
    Venda.objects.filter(pk=pk).update(is_active=False)
    return listar_vendas(request, funcionario_id)
```


- Large class: muitos atributos semelhantes em classes diferentes, pattern aplicado (Mixin patter):

- Primeiramente foi criada a classe ```CommonInfo``` que abriga as semelhanças:
`common_info_model.py`:
```py
class CommonInfo(models.Model):

    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(null=True)
    is_paid = models.BooleanField(null=True)

    class Meta:
        abstract = True
```

- Após a criação, as classes com atributos em commum têm uma relação com a classe ```CommonInfo``` .

`ponto_funcionario_model.py`:
```py
class PontoFuncionario(CommonInfo):
    data_ponto = models.DateField(null=True)
    hora_entrada = models.TimeField(null=True)
    hora_saida = models.TimeField(null=True)
    horas_trabalhadas = models.IntegerField(null=True)
    mes_ponto = models.IntegerField(null=True)
```

`venda_funcionario_model.py`:
```py
class Venda(CommonInfo):
    nome_item = models.CharField(max_length=30)
    descricao_item = models.CharField(max_length=1000)
    data_venda = models.DateField(null=True)
    valor_venda = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(99999)])
    mes_venda = models.IntegerField(null=True)

```

- Também foi ousado o Decorator pattern, para lidar com as requisições feitas:

`common_info_model.py`:
```py
@csrf_exempt
def aplicar_taxa(request, pk, value):
    funcionario = Funcionario.objects.filter(pk=pk)
    val = (getById(Funcionario, pk).total_a_receber) - value
    if request.is_ajax() and request.POST:
        funcionario.update(taxa_sindicato=value)
        funcionario.update(total_a_receber=val)
        return render(request, 'sindicato/painel_sindicato.html')
    else:
        raise Http404
```

- Além disso, todo o código foi separado por tipo, anteriormente existia um arquivo único para as ```views```  e ```models```:

- Estrutura antiga:

![alt text](https://firebasestorage.googleapis.com/v0/b/teste-e6f39.appspot.com/o/old.PNG?alt=media&token=9d11d2a8-475b-48e7-81c2-0a31e540ab45)

- Estrutura atual (Model):
 ![alt text](https://firebasestorage.googleapis.com/v0/b/teste-e6f39.appspot.com/o/new%20model.PNG?alt=media&token=59d238dd-cd52-4238-b471-c214f3e2080f)


- Estrutura atual (View):
 ![alt text](https://firebasestorage.googleapis.com/v0/b/teste-e6f39.appspot.com/o/new%20view.PNG?alt=media&token=b20766f5-5c80-44fe-b8fd-c8dfe4a49f71)

 
 


