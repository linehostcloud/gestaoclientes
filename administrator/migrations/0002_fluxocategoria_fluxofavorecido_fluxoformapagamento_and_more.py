# Generated by Django 5.0.4 on 2024-04-19 23:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('administrator', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='FluxoCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FluxoFavorecido',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FluxoFormaPagamento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FluxoTransacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='FluxoCaixa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('data_movimentacao', models.DateField(auto_now_add=True)),
                ('valor', models.DecimalField(decimal_places=2, max_digits=10)),
                ('situacao', models.BooleanField(default=False)),
                ('descricao', models.TextField(blank=True, null=True)),
                ('cliente', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrator.cliente')),
                ('categoria', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrator.fluxocategoria')),
                ('favorecido', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrator.fluxofavorecido')),
                ('forma_pagamento', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrator.fluxoformapagamento')),
                ('transacao', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='administrator.fluxotransacao')),
            ],
        ),
    ]
