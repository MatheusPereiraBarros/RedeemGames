# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-24 14:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('RedeemGamesWEB', '0004_auto_20170424_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='jogochave',
            name='linkDownload',
            field=models.URLField(default='www.example.com.br'),
        ),
    ]
