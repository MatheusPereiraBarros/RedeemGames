# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-21 21:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BancoMoedasUsuario',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('saldoMoedas', models.BigIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Jogo',
            fields=[
                ('idJogo', models.AutoField(primary_key=True, serialize=False)),
                ('nomeJogo', models.CharField(max_length=20)),
                ('imagemJogo', models.URLField()),
                ('distribuidora', models.CharField(max_length=50)),
                ('precoJogo', models.BigIntegerField()),
                ('plataformaJogo', models.CharField(max_length=50)),
                ('chaveAcesso', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Pedido',
            fields=[
                ('idPedido', models.AutoField(primary_key=True, serialize=False)),
                ('dataPedido', models.DateTimeField()),
                ('idJogo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RedeemGamesWEB.Jogo')),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('idUsuario', models.AutoField(primary_key=True, serialize=False)),
                ('nomeUsuario', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='pedido',
            name='idUsuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RedeemGamesWEB.Usuario'),
        ),
        migrations.AddField(
            model_name='bancomoedasusuario',
            name='idUsuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RedeemGamesWEB.Usuario'),
        ),
    ]
