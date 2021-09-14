from django.http.response import Http404
from django.shortcuts import redirect, render
from django.http import HttpResponse
from app.forms import FuncionarioForm, PontoForm, VendaForm
from app.models import Funcionario, PontoFuncionario, Venda
from django.db.models import Sum
from django.db.models import F
from datetime import date, datetime
from django.db.models import Q
from django.views.decorators.csrf import csrf_exempt

import pendulum
