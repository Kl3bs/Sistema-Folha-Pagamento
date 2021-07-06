from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

# Create your models here.


class Funcionario(models.Model):
    nome = models.CharField(max_length=35)
    endereco = models.CharField(max_length=40)
    tipo_prof = models.TextChoices('"Selecionar"',
                                   'HORISTA MENSALISTA COMISSIONADO')
    tipo = models.CharField(blank=True,
                            choices=tipo_prof.choices,
                            max_length=12)
    salario = models.IntegerField(
        default=1,
        validators=[MinValueValidator(1),
                    MaxValueValidator(999999)])
    sindicato = models.BooleanField(null=True)


class PontoFuncionario(models.Model):
    funcionario = models.ForeignKey("Funcionario",
                                    on_delete=models.CASCADE,
                                    blank=True,
                                    null=True)
    data_ponto = models.DateField(null=True)
    hora_entrada = models.TimeField(null=True)
    hora_saida = models.TimeField(null=True)
