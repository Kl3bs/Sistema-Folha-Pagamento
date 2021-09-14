 
from django.urls import path
from app import views
from app.views import  agenda_pagamento, aplicar_taxa, bater_ponto, deletar_ponto, desativar, desativar_ponto, desativar_venda, folha_pagamento, home, form, create, listar_vendas, mostrar_funcionarios, reativar, reativar_ponto, reativar_venda, rodar_folha, view, edit, update, delete, ponto, ponto_info, nova_venda, vendas

urlpatterns = [
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
    path('pagamento/', folha_pagamento, name='pagamento'),
    path('rodar_folha/', rodar_folha, name='rodar_folha'),
    path('agenda_pagamento/<int:pk>/<int:dia>', agenda_pagamento, name='agenda_pagamento'),

 
    #*SINDICATO!
    path('painel_sindicato/', mostrar_funcionarios, name='painel_sindicato'),
    path('painel_sindicato/aplicar_taxa/<int:pk>/<int:value>',
         aplicar_taxa,
         name='aplicar_taxa'),
]
