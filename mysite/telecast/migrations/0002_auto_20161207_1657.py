# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-12-07 16:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('telecast', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telecast',
            name='broadcastDate',
            field=models.DateField(),
        ),
    ]
