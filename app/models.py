from django.db import models
from django.db.models.enums import Choices

# Create your models here.
class Funcionario(models.Model) :
    nome = models.CharField(max_length=35)
    endereco = models.CharField(max_length=40)
    tipo = models.CharField(max_length=15)
