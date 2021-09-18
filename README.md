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

## Code Smells

- Várias chamadas baseadas na pk (Pirmary Key) em locais diversos, pattern aplicado (Custom Manger):

`general.py`:
```py
def getById(self, pk):
    return self.objects.get(pk=pk)
    ...
```

`vendas.py`:
```py
def remover_pagamento_comissao(funcionario_id, pk):
    instance = getById(Venda, pk)
    user = getById(Funcionario, funcionario_id)
    user.total_a_receber -= (instance.valor_venda * (user.comissao / 100))
    Funcionario.objects.filter(pk=funcionario_id).update(
        total_a_receber=user.total_a_receber)
    ...
```


- Várias chamadas de filtragem em locais diversos, pattern aplicado (Custom Manger):

`general.py`:
```py
def filterById(self, pk):
    return self.objects.filter(pk=pk)
    ...
```

`general.py`:
```py
def desativar(request, pk):
    filterById(Funcionario, pk).update(is_active=False)
    return redirect('home')


def reativar(request, pk):
    filterById(Funcionario, pk).update(is_active=True)
    return redirect('home')

    ...
```

 

- Métodos extensos e complexos, pattern aplicado (Extract Method):


`vendas.py`:
```py
def remover_pagamento_comissao(funcionario_id, pk):
    instance = getById(Venda, pk)
    user = getById(Funcionario, funcionario_id)
    user.total_a_receber -= (instance.valor_venda * (user.comissao / 100))
    Funcionario.objects.filter(pk=funcionario_id).update(
        total_a_receber=user.total_a_receber)
    ...
```

```py
def desativar_venda(request, funcionario_id, pk):
    remover_pagamento_comissao(funcionario_id, pk)
    Venda.objects.filter(pk=pk).update(is_active=False)
    return listar_vendas(request, funcionario_id)
    ...
```

- Muitos atributos semelhantes em classes, pattern aplicado (Mixin patter):

`common_info_model.py`:
```py
class CommonInfo(models.Model):

    funcionario = models.ForeignKey(Funcionario, on_delete=models.CASCADE, blank=True, null=True)
    is_active = models.BooleanField(null=True)
    is_paid = models.BooleanField(null=True)

    class Meta:
        abstract = True

    ...
```
`ponto_funcionario_model.py`:
```py
class PontoFuncionario(CommonInfo):
    data_ponto = models.DateField(null=True)
    hora_entrada = models.TimeField(null=True)
    hora_saida = models.TimeField(null=True)
    horas_trabalhadas = models.IntegerField(null=True)
    mes_ponto = models.IntegerField(null=True)

    ...
```

`venda_funcionario_model.py`:
```py
class Venda(CommonInfo):
    nome_item = models.CharField(max_length=30)
    descricao_item = models.CharField(max_length=1000)
    data_venda = models.DateField(null=True)
    valor_venda = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(99999)])
    mes_venda = models.IntegerField(null=True)
    ...
```

- Segurança das requisições (Decorator pattern) :

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
    ...
```







