# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-26 05:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RedeemGamesWEB', '0009_auto_20170426_0212'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jogo',
            name='nomeJogo',
            field=models.CharField(max_length=50),
        ),
    ]
