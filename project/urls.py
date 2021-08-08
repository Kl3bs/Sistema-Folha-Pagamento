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
from app.views import aplicar_taxa, bater_ponto, deletar_ponto, desativar, desativar_ponto, desativar_venda, home, form, create, listar_vendas, mostrar_funcionarios, reativar, reativar_ponto, reativar_venda, rodar_folha, view, edit, update, delete, ponto, ponto_info, nova_venda, vendas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    #*FUNCIONARIO
    path('form/', form, name='form'),
    path('create/', create, name='create'),
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>', update, name='update'),
    path('delete/<int:pk>', delete, name='delete'),
    path('desativar/<int:pk>', desativar, name='desativar'),
    path('reativar/<int:pk>', reativar, name='reativar'),

    #*PONTO
    path('ponto/<int:pk>', ponto, name='ponto'),
    path('bater_ponto/<int:pk>', bater_ponto, name='bater_ponto'),
    path('ponto_info/<int:pk>', ponto_info, name='ponto_info'),
    path('deletar_ponto/<int:funcionario_id>/<int:pk>',
         deletar_ponto,
         name='deletar_ponto'),
    path('desativar_ponto/<int:funcionario_id>/<int:pk>',
         desativar_ponto,
         name='desativar'),
    path('reativar_ponto/<int:funcionario_id>/<int:pk>',
         reativar_ponto,
         name='reativar'),

    #*VENDAS
    path('vendas/<int:pk>', vendas, name='vendas'),
    path('nova_venda/<int:pk>', nova_venda, name='nova_venda'),
    path('listar_vendas/<int:pk>', listar_vendas, name='listar_vendas'),
    path('desativar_venda/<int:funcionario_id>/<int:pk>',
         desativar_venda,
         name='desativar'),
    path('reativar_venda/<int:funcionario_id>/<int:pk>',
         reativar_venda,
         name='reativar'),

    #*FOLHA DE PAGAMENTO
    path('pagamento/', rodar_folha, name='pagamento'),
 
    #*SINDICATO!
    path('painel_sindicato/', mostrar_funcionarios, name='painel_sindicato'),
    path('painel_sindicato/aplicar_taxa/<int:pk>/<int:value>',
         aplicar_taxa,
         name='aplicar_taxa'),
]
