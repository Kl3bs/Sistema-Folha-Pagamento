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
from app.views import bater_ponto, home, form, create, listar_vendas, view, edit, update, delete, ponto, ponto_info, nova_venda, vendas

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),

    #*USER PATHS
    path('form/', form, name='form'),
    path('create/', create, name='create'),
    path('view/<int:pk>/', view, name='view'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('update/<int:pk>', update, name='update'),
    path('delete/<int:pk>', delete, name='delete'),

    #*PONTO PATHS
    path('ponto/<int:pk>', ponto, name='ponto'),
    path('bater_ponto/<int:pk>', bater_ponto, name='bater_ponto'),
    path('ponto_info/<int:pk>', ponto_info, name='ponto_info'),

    #*VENDAS PATHS
    path('vendas/<int:pk>', vendas, name='vendas'),
    path('nova_venda/<int:pk>', nova_venda, name='nova_venda'),
    path('listar_vendas/<int:pk>', listar_vendas, name='listar_vendas'),
]
