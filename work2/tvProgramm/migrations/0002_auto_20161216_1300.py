# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-16 10:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvProgramm', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='programm',
            name='description',
            field=models.CharField(max_length=300),
        ),
        migrations.AlterField(
            model_name='programm',
            name='length',
            field=models.DateTimeField(),
        ),
    ]
