# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 05:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RedeemGamesWEB', '0008_auto_20170426_0211'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogo',
            name='descricaoJogo',
            field=models.CharField(default='', max_length=140),
        ),
    ]
