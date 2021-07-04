from django.db import models
from django.db.models.enums import Choices
from django import forms


# Create your models here.

TITLE_CHOICES = [
    ('MR', 'Mr.'),
    ('MRS', 'Mrs.'),
    ('MS', 'Ms.'),
]
class Funcionario(models.Model) :
    nome = models.CharField(max_length=35)
    endereco = models.CharField(max_length=40)
    #tipo = forms.ChoiceField(widget=forms.Select(attrs={'class': 'selector'}))
    tipo_prof = models.TextChoices('MedalType', 'HORISTA MENSALISTA COMISSIONADO')
    tipo = models.CharField(blank=True, choices=tipo_prof.choices, max_length=12)
