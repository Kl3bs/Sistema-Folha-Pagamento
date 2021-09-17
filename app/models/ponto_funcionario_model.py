from .imports import *
from .common_info_model import *


class PontoFuncionario(CommonInfo):
    data_ponto = models.DateField(null=True)
    hora_entrada = models.TimeField(null=True)
    hora_saida = models.TimeField(null=True)
    horas_trabalhadas = models.IntegerField(null=True)
    mes_ponto = models.IntegerField(null=True)
