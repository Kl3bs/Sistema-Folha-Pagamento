# Generated by Django 3.2.5 on 2021-07-04 14:37

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210704_1435'),
    ]

    operations = [
        migrations.AddField(
            model_name='funcionario',
            name='salario',
            field=models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(999999)]),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='sindicato',
            field=models.BooleanField(),
        ),
        migrations.AlterField(
            model_name='funcionario',
            name='tipo',
            field=models.CharField(blank=True, choices=[('HORISTA', 'Horista'), ('MENSALISTA', 'Mensalista'), ('COMISSIONADO', 'Comissionado')], max_length=12),
        ),
    ]