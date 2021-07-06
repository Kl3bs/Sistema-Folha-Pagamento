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
from app.views import bater_ponto, home, form, create, view, edit, update, delete, ponto, ponto_info, nova_venda

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('form/', form, name='form'),
    path('create/', create, name='create'),
    path('view/<int:pk>/', view, name='view'), #Recebe a pimary key como parametro na url
    path('edit/<int:pk>/', edit, name='edit'), #Recebe a pimary key como parametro na url
    path('update/<int:pk>', update, name='update'), #Recebe a pimary key como parametro na url
    path('delete/<int:pk>', delete, name='delete'), #Recebe a pimary key como parametro na url
    path('ponto/<int:pk>', ponto, name='ponto'), #Recebe a pimary key como parametro na url
    path('bater_ponto/<int:pk>', bater_ponto, name='bater_ponto'), #Recebe a pimary key como parametro na url

    path('ponto_info/<int:pk>', ponto_info, name='ponto_info'), #Rezebe a pimary key como parametro na url
    path('nova_venda/<int:pk>', nova_venda, name='nova_venda'),



    
]
