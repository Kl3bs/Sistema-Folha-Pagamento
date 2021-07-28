from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Funcionario(models.Model):
    nome = models.CharField(max_length=35)
    endereco = models.CharField(max_length=40)
    tipo_prof = models.TextChoices('"Selecionar"',
                                   "HORISTA MENSALISTA COMISSIONADO")
    tipo = models.CharField(blank=True,
                            choices=tipo_prof.choices,
                            max_length=12)
    salario = models.IntegerField(
        default=0,
        validators=[MinValueValidator(0),
                    MaxValueValidator(999999)])
    sindicato = models.BooleanField(null=True)

    tipo_pagamento = models.TextChoices('"Selecionar"',
                                        "CHEQUE CHEQUE-CORREIOS DEPOSITO")
    forma_pagamento = models.CharField(blank=False,
                                       choices=tipo_pagamento.choices,
                                       max_length=20)

    comissao = models.IntegerField(
        default=0, validators=[MinValueValidator(0),
                               MaxValueValidator(100)])

    total_a_receber = models.IntegerField(null=True)

    is_active = models.BooleanField(null=True)

    data_pagamento = models.DateField(null=True)


class PontoFuncionario(models.Model):
    funcionario = models.ForeignKey(Funcionario,
                                    on_delete=models.CASCADE,
                                    blank=True,
                                    null=True)
    data_ponto = models.DateField(null=True)
    hora_entrada = models.TimeField(null=True)
    hora_saida = models.TimeField(null=True)
    horas_trabalhadas = models.IntegerField(null=True)
    is_active = models.BooleanField(null=True)


class Venda(models.Model):
    funcionario = models.ForeignKey(Funcionario,
                                    on_delete=models.CASCADE,
                                    blank=True,
                                    null=True)
    nome_item = models.CharField(max_length=30)
    descricao_item = models.CharField(max_length=1000)
    data_venda = models.DateField(null=True)
    valor_venda = models.IntegerField(
        default=0, validators=[MinValueValidator(0),
                               MaxValueValidator(99999)])
    is_active = models.BooleanField(null=True)
