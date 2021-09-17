from .imports import *
from .common_info_model import *

class Venda(CommonInfo):
  
    nome_item = models.CharField(max_length=30)
    descricao_item = models.CharField(max_length=1000)
    data_venda = models.DateField(null=True)
    valor_venda = models.IntegerField(default=0, validators=[MinValueValidator(0), MaxValueValidator(99999)])
    mes_venda = models.IntegerField(null=True)

 

