"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from app.views import  agenda_pagamento, aplicar_taxa, bater_ponto, deletar_ponto, desativar, desativar_ponto, desativar_venda, folha_pagamento, home, form, create, listar_vendas, mostrar_funcionarios, reativar, reativar_ponto, reativar_venda, rodar_folha, view, edit, update, delete, ponto, ponto_info, nova_venda, vendas

urlpatterns = [

    path('', include('app.urls')),
    path('admin/', admin.site.urls) 
]
