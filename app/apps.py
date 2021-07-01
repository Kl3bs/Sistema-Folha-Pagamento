from django.apps import AppConfig
from django.db import models


class AppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'app'

class Funcionario(models.Model) :
    # id_funcionario = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=35)
    endereco = models.CharField(max_length=40)
    tipo = models.CharField(max_length=15)
