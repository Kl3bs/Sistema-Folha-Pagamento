# Generated by Django 3.2.5 on 2021-09-17 12:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='funcionario',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='pontofuncionario',
            name='is_active',
        ),
        migrations.RemoveField(
            model_name='venda',
            name='is_active',
        ),
    ]