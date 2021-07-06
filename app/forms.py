from django.db import models
from app.models import Funcionario, PontoFuncionario
from django.forms import ModelForm


# Create the form class.
class FuncionarioForm(ModelForm):
    class Meta:
        model = Funcionario
        fields = ['nome', 'endereco', 'tipo', 'salario', 'sindicato']


class PontoForm(ModelForm):
    class Meta:
        model = PontoFuncionario
        fields = ['hora_entrada', 'hora_saida', 'data_ponto']
