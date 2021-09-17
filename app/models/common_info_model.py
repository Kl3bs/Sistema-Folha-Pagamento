from .imports import *
from .funcionario_model import Funcionario


class CommonInfo(models.Model):

    funcionario = models.ForeignKey(Funcionario,
                                    on_delete=models.CASCADE,
                                    blank=True,
                                    null=True)
    is_active = models.BooleanField(null=True)
    is_paid = models.BooleanField(null=True)

    class Meta:
        abstract = True
