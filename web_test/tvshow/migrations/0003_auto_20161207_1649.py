# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-12-07 16:49
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tvshow', '0002_show_broadcast_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='show',
            name='broadcast_date',
            field=models.DateField(),
        ),
    ]
