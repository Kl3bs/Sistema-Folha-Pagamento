from .imports import *

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
    tipo_pagamento = models.TextChoices('"Selecionar"',"CHEQUE CHEQUE-CORREIOS DEPOSITO")
    forma_pagamento = models.CharField(blank=False, choices=tipo_pagamento.choices, max_length=20)
    comissao = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])
    total_a_receber = models.IntegerField(null=True)
    is_active = models.BooleanField(null=True)
    data_pagamento = models.DateField(null=True)
    taxa_sindicato = models.IntegerField(null=True)
    mes_pago = models.IntegerField(null=True)

 
 