# Sistema de Pagamento (Projeto de Software-UFAL)


## Padrões Implementados:

Mixin pattern;
Custom manager pattern;
Decorator pattern;
Extract method;

A maioria das atualizações foram feitas dentro da view e do model.
Todas as funcionalidades estão implementadas.

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

## Executando o porjeto

Volte para a pasta raiz do projeto pelo terminal e digite:
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

Acesse o endereço localhost:8000, para ver o projeto no browser.




